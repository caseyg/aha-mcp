import { Request, Response } from "express";
import crypto from "crypto";

export interface OAuthConfig {
  clientId?: string;
  clientSecret?: string;
  redirectUri?: string;
  ahaDomain?: string;
  serverUrl?: string; // The canonical URL of this MCP server
}

export interface TokenStore {
  [sessionId: string]: {
    accessToken: string;
    subdomain: string;
    expiresAt?: Date;
  };
}

export class OAuthHandler {
  private config: OAuthConfig;
  private tokens: TokenStore = {};
  private pendingStates: Map<string, { sessionId: string; codeVerifier: string; state: string }> = new Map();
  private readonly PKCE_CHALLENGE_METHOD = 'S256';

  constructor(config: OAuthConfig) {
    this.config = config;
  }

  /**
   * Generate OAuth authorization URL with PKCE
   */
  getAuthorizationUrl(sessionId: string, subdomain?: string): string {
    const state = crypto.randomBytes(32).toString('hex');
    
    // Generate PKCE parameters
    const codeVerifier = this.generateCodeVerifier();
    const codeChallenge = this.generateCodeChallenge(codeVerifier);
    
    this.pendingStates.set(state, { sessionId, codeVerifier, state });
    
    // Clean up old states after 10 minutes
    setTimeout(() => {
      this.pendingStates.delete(state);
    }, 10 * 60 * 1000);

    const baseUrl = subdomain 
      ? `https://${subdomain}.aha.io/oauth/authorize`
      : (this.config.ahaDomain 
        ? `https://${this.config.ahaDomain}.aha.io/oauth/authorize`
        : `https://secure.aha.io/oauth/authorize`);
    
    const params = new URLSearchParams({
      client_id: this.config.clientId || '',
      redirect_uri: this.config.redirectUri || '',
      response_type: 'code',
      state,
      code_challenge: codeChallenge,
      code_challenge_method: this.PKCE_CHALLENGE_METHOD
    });

    // Add resource parameter if server URL is configured
    if (this.config.serverUrl) {
      params.append('resource', this.config.serverUrl);
    }

    return `${baseUrl}?${params}`;
  }

  /**
   * Generate PKCE code verifier
   */
  private generateCodeVerifier(): string {
    return crypto.randomBytes(32).toString('base64url');
  }

  /**
   * Generate PKCE code challenge using S256 method
   */
  private generateCodeChallenge(verifier: string): string {
    return crypto.createHash('sha256').update(verifier).digest('base64url');
  }

  /**
   * Handle OAuth callback
   */
  async handleCallback(req: Request, res: Response): Promise<void> {
    const { code, state, account_subdomain } = req.query;

    if (!code || !state || typeof code !== 'string' || typeof state !== 'string') {
      res.status(400).json({ error: 'Missing required parameters' });
      return;
    }

    const stateData = this.pendingStates.get(state);
    if (!stateData) {
      res.status(400).json({ error: 'Invalid state parameter' });
      return;
    }

    const { sessionId, codeVerifier } = stateData;
    this.pendingStates.delete(state);

    try {
      // Exchange code for access token with PKCE
      const subdomain = account_subdomain || this.config.ahaDomain;
      const tokenResponse = await this.exchangeCodeForToken(code, subdomain as string, codeVerifier);
      
      // Store token
      this.tokens[sessionId] = {
        accessToken: tokenResponse.access_token,
        subdomain: subdomain as string,
        expiresAt: new Date(Date.now() + 24 * 60 * 60 * 1000) // 24 hours
      };

      // Redirect back to success page or close window
      res.send(`
        <html>
          <body>
            <h2>Authentication Successful!</h2>
            <p>You can now close this window and return to your application.</p>
            <script>
              // Send message to opener if available
              if (window.opener) {
                window.opener.postMessage({ type: 'oauth-success', sessionId: '${sessionId}' }, '*');
              }
              // Close window after 2 seconds
              setTimeout(() => window.close(), 2000);
            </script>
          </body>
        </html>
      `);
    } catch (error) {
      console.error('OAuth token exchange failed:', error);
      res.status(500).json({ error: 'Failed to exchange authorization code' });
    }
  }

  /**
   * Exchange authorization code for access token with PKCE
   */
  private async exchangeCodeForToken(code: string, subdomain: string, codeVerifier: string): Promise<any> {
    const tokenUrl = `https://${subdomain}.aha.io/oauth/token`;
    
    const params = new URLSearchParams({
      code,
      client_id: this.config.clientId || '',
      client_secret: this.config.clientSecret || '',
      grant_type: 'authorization_code',
      redirect_uri: this.config.redirectUri || '',
      code_verifier: codeVerifier
    });

    // Add resource parameter if configured
    if (this.config.serverUrl) {
      params.append('resource', this.config.serverUrl);
    }

    const response = await fetch(tokenUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: params
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`Token exchange failed: ${error}`);
    }

    return response.json();
  }

  /**
   * Get token for session
   */
  getToken(sessionId: string): string | null {
    const tokenData = this.tokens[sessionId];
    if (!tokenData) {
      return null;
    }

    // Check if token is expired
    if (tokenData.expiresAt && tokenData.expiresAt < new Date()) {
      delete this.tokens[sessionId];
      return null;
    }

    return tokenData.accessToken;
  }

  /**
   * Get subdomain for session
   */
  getSubdomain(sessionId: string): string | null {
    const tokenData = this.tokens[sessionId];
    return tokenData?.subdomain || null;
  }

  /**
   * Check if session is authenticated
   */
  isAuthenticated(sessionId: string): boolean {
    return this.getToken(sessionId) !== null;
  }

  /**
   * Clear token for session
   */
  clearToken(sessionId: string): void {
    delete this.tokens[sessionId];
  }

  /**
   * Clear all expired tokens
   */
  cleanupExpiredTokens(): void {
    const now = new Date();
    for (const [sessionId, tokenData] of Object.entries(this.tokens)) {
      if (tokenData.expiresAt && tokenData.expiresAt < now) {
        delete this.tokens[sessionId];
      }
    }
  }
}