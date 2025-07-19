# Identity providers

## List active identity providers that can be used for SSO

**GET** `/api/v1/identity_providers`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/identity_providers" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "identity_providers": [
    {
      "id": "483954339",
      "enabled": true,
      "name": "notebook",
      "sso_endpoint": "https://dev-344119.oktapreview.com/app/nonodev344119_devapp_1/exkakanw6tt4fzIa20h7/sso/saml",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  ]
}
```

---

## Get a specific identity provider

**GET** `/api/v1/identity_providers/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the identity provider

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/identity_providers/483954339" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "identity_provider": {
    "id": "483954339",
    "enabled": true,
    "name": "notebook",
    "sso_endpoint": "https://dev-344119.oktapreview.com/app/nonodev344119_devapp_1/exkakanw6tt4fzIa20h7/sso/saml",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---
