# Integrations

## Create an integration for an account

**POST** `/api/v1/integrations`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `service_name` () - **Required** - Service name in snake_case format
- `integration_version` () - Optional - Integer 1 or 2. Defaults to 1

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/integrations" -d '{"integration":{"service_name":"zendesk","enabled":true}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "6776757454440039674",
    "service_name": "zendesk",
    "template_id": null,
    "name": "Zendesk",
    "enabled": true,
    "callback_token": "5e0be1000087c7f9",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/6776757454440039674",
    "resource": "http://company.aha.io/api/v1/integrations/6776757454440039674",
    "owner": {
      "type": "Account",
      "id": "303742481",
      "url": "http://company.aha.io/account/303742481",
      "resource": "http://company.aha.io/account/303742481"
    }
  }
}
```

---

## List integrations for an account

**GET** `/api/v1/integrations`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/integrations" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integrations": [
    {
      "id": "79015308",
      "name": "Salesforce",
      "service_name": "salesforce",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "84619270",
      "name": "Salesforce V2",
      "service_name": "salesforce",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "163322775",
      "name": "Activity webhook",
      "service_name": "audit_webhook",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "241856910",
      "name": "Trello",
      "service_name": "trello",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "390243673",
      "name": "Zendesk",
      "service_name": "zendesk",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "578818383",
      "name": "Aha! (to Slack)",
      "service_name": "slack",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "828392279",
      "name": "Security webhook",
      "service_name": "security_webhook",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "922472543",
      "name": "Aha! (from Slack)",
      "service_name": "slack_commands",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "938531265",
      "name": "Aha! (from Slack)",
      "service_name": "slack_commands",
      "created_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "pagination": {
    "total_records": 9,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Create an integration for a product

**POST** `/api/v1/products/:product_id/integrations`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `service_name` () - **Required** - Service name in snake_case format
- `integration_version` () - Optional - Integer 1 or 2. Defaults to 1

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/integrations" -d '{"integration":{"service_name":"zendesk","enabled":true}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "6776757454437868293",
    "service_name": "zendesk",
    "template_id": null,
    "name": "Zendesk",
    "enabled": true,
    "callback_token": "5e0be10000f2be23",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/6776757454437868293",
    "resource": "http://company.aha.io/api/v1/integrations/6776757454437868293",
    "owner": {
      "type": "Project",
      "id": "131414752",
      "url": "http://company.aha.io/projects/PRJ1",
      "resource": "http://company.aha.io/projects/PRJ1"
    }
  }
}
```

---

## Create an integration based on a template for a product

**POST** `/api/v1/products/:product_id/integrations`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `service_name` () - **Required** - Service name in snake_case format
- `integration_version` () - Optional - Integer 1 or 2. Defaults to 1

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/integrations" -d '{"integration":{"service_name":"jira","enabled":true,"template_id":204584239}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "6776757454439134601",
    "service_name": "jira",
    "template_id": null,
    "name": "Jira",
    "enabled": true,
    "callback_token": "5e0be10000b1e19f",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/6776757454439134601",
    "resource": "http://company.aha.io/api/v1/integrations/6776757454439134601",
    "owner": {
      "type": "Project",
      "id": "131414752",
      "url": "http://company.aha.io/projects/PRJ1",
      "resource": "http://company.aha.io/projects/PRJ1"
    }
  }
}
```

---

## List integrations for a product

**GET** `/api/v1/products/:product_id/integrations`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/integrations" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integrations": [
    {
      "id": "31907509",
      "name": "Rally",
      "service_name": "rally",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "36231792",
      "name": "GitHub Issues",
      "service_name": "github_issues",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "186281709",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "202598724",
      "name": "Jira via Connect",
      "service_name": "jira_connect",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "204584239",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "207648948",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "222276392",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "322044925",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "342659513",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "386928799",
      "name": "Azure DevOps Services",
      "service_name": "vsts",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "413207847",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "453754848",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "550349479",
      "name": "Jira via Connect",
      "service_name": "jira_connect",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "583937884",
      "name": "Jira template (visible to all)",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "706216981",
      "name": "Rally",
      "service_name": "rally",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "791044582",
      "name": "Azure DevOps Services",
      "service_name": "vsts",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "804274302",
      "name": "Jira V2 Disabled",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "846899991",
      "name": "Azure DevOps Services",
      "service_name": "tfs",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "868040294",
      "name": "Rally",
      "service_name": "rally",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "945767377",
      "name": "Trello",
      "service_name": "trello",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "952935179",
      "name": "Jira",
      "service_name": "jira",
      "created_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "pagination": {
    "total_records": 21,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific integration

**GET** `/api/v1/products/:product_id/integrations/:integration_id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `service_name` () - **Required** - Numeric ID of the integration

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/integrations/204584239" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "204584239",
    "service_name": "jira",
    "template_id": null,
    "name": "Jira",
    "enabled": true,
    "callback_token": "22b7893e7fa1c4c60847090f78fbf0ec",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/204584239",
    "resource": "http://company.aha.io/api/v1/integrations/204584239",
    "owner": {
      "type": "Project",
      "id": "131414752",
      "url": "http://company.aha.io/projects/PRJ1",
      "resource": "http://company.aha.io/projects/PRJ1"
    }
  }
}
```

---

## Enable integration

**PUT** `/api/v1/products/:product_id/integrations/:integration_id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `service_name` () - **Required** - Numeric ID of the integration
- `integration` () - **Required** - Integration object

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/integrations/204584239" -d '{"integration":{"enabled":true}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "204584239",
    "service_name": "jira",
    "template_id": null,
    "name": "Jira",
    "enabled": true,
    "callback_token": "22b7893e7fa1c4c60847090f78fbf0ec",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/204584239",
    "resource": "http://company.aha.io/api/v1/integrations/204584239",
    "owner": {
      "type": "Project",
      "id": "131414752",
      "url": "http://company.aha.io/projects/PRJ1",
      "resource": "http://company.aha.io/projects/PRJ1"
    }
  }
}
```

**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/integrations/204584239" -d '{"integration":{"enabled":true}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "204584239",
    "service_name": "jira",
    "template_id": null,
    "name": "Jira",
    "enabled": true,
    "callback_token": "22b7893e7fa1c4c60847090f78fbf0ec",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/204584239",
    "resource": "http://company.aha.io/api/v1/integrations/204584239",
    "owner": {
      "type": "Project",
      "id": "131414752",
      "url": "http://company.aha.io/projects/PRJ1",
      "resource": "http://company.aha.io/projects/PRJ1"
    }
  }
}
```

---

## Get a specific integration by service name

**GET** `/api/v1/products/:product_id/integrations/:service_name`

### Additional Information
DEPRECATED: provide :integration_id rather than :service_name to identify the integration.

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `service_name` () - **Required** - Service name of the integration

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/integrations/jira" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration": {
    "id": "204584239",
    "service_name": "jira",
    "template_id": null,
    "name": "Jira",
    "enabled": true,
    "callback_token": "22b7893e7fa1c4c60847090f78fbf0ec",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "last_error_at": null,
    "last_webhook_request_at": null,
    "url": "http://company.aha.io/integrations/204584239",
    "resource": "http://company.aha.io/api/v1/integrations/204584239",
    "owner": {
      "type": "Project",
      "id": "131414752",
      "url": "http://company.aha.io/projects/PRJ1",
      "resource": "http://company.aha.io/projects/PRJ1"
    }
  }
}
```

---
