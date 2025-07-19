# Idea organizations

## List idea organizations

**GET** `/api/v1/idea_organizations`

### Parameters
- `q` () - Optional - Search term to match against organization name
- `email_domain` () - Optional - If provided returns organiazations with a matching email domain

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_organizations" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_organizations": [
    {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    {
      "id": "290305227",
      "name": "FaceTube",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/290305227",
      "resource": "http://company.aha.io/api/v1/idea_organizations/290305227"
    }
  ],
  "pagination": {
    "total_records": 2,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific organization

**GET** `/api/v1/idea_organizations/:id`

### Parameters
- `id` () - **Required** - Numeric ID organization

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_organizations/138732915" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_organization": {
    "id": "138732915",
    "name": "Acme",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/ideas/idea_organizations/138732915",
    "description": {
      "id": "6776757454426790234",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "endorsements_count": 2,
    "email_domains": "",
    "revenue": null,
    "custom_fields": [
      {
        "id": 957991743,
        "key": "org_equation_field",
        "name": "Org equation field",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "test": {
              "value": 10,
              "name": "a",
              "display_value": "10.0"
            }
          }
        },
        "type": "equation_sheet"
      }
    ],
    "integration_fields": []
  }
}
```

---

## Update organization

**PUT** `/api/v1/idea_organizations/:id`

### Parameters
- `id` () - **Required** - Numeric ID organization
- `name` () - Optional - Name of the organization
- `email_domains` () - Optional - Email domains
- `revenue` () - Optional - Numeric revenue value that is tied to the organization. Can include decimals.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_organizations/138732915" -d '{"idea_organization":{"name":"A new name"}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_organization": {
    "id": "138732915",
    "name": "A new name",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/ideas/idea_organizations/138732915",
    "description": {
      "id": "",
      "body": "#<note:0x00007fff6d2c0500></note:0x00007fff6d2c0500>",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "endorsements_count": 2,
    "email_domains": "",
    "revenue": null,
    "custom_fields": [
      {
        "id": 957991743,
        "key": "org_equation_field",
        "name": "Org equation field",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "test": {
              "value": 10,
              "name": "a",
              "display_value": "10.0"
            }
          }
        },
        "type": "equation_sheet"
      }
    ],
    "integration_fields": []
  }
}
```

---

## Update organization custom fields

**PUT** `/api/v1/idea_organizations/:id`

### Parameters
- `id` () - **Required** - Numeric ID organization
- `name` () - Optional - Name of the organization
- `email_domains` () - Optional - Email domains
- `revenue` () - Optional - Numeric revenue value that is tied to the organization. Can include decimals.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_organizations/138732915" -d '{"idea_organization":{"custom_fields":{"industry":"retail"}}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_organization": {
    "id": "138732915",
    "name": "Acme",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/ideas/idea_organizations/138732915",
    "description": {
      "id": "",
      "body": "#<note:0x00007fff6d324ed8></note:0x00007fff6d324ed8>",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "endorsements_count": 2,
    "email_domains": "",
    "revenue": null,
    "custom_fields": [
      {
        "id": "6776757454435871695",
        "key": "industry",
        "name": "Industry",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "retail",
        "type": "string"
      },
      {
        "id": 957991743,
        "key": "org_equation_field",
        "name": "Org equation field",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "test": {
              "value": 10,
              "name": "a",
              "display_value": "10.0"
            }
          }
        },
        "type": "equation_sheet"
      }
    ],
    "integration_fields": []
  }
}
```

---

## Create an idea organization

**POST** `/api/v1/idea_organizations`

### Parameters
- `name` () - **Required** - Name of the organization
- `email_domains` () - Optional - Email domains
- `revenue` () - Optional - Numeric revenue value that is tied to the organization. Can include decimals.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_organizations" -d '{"idea_organization":{"name":"My organization","email_domains":"example.com, example.org","revenue":"55000"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_organization": {
    "id": "6776757454438843973",
    "name": "My organization",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/ideas/idea_organizations/6776757454438843973",
    "description": {
      "id": "6776757454431831157",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "created_by_user": {
      "id": "1049303076",
      "name": "George Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsements_count": 0,
    "email_domains": "example.com, example.org",
    "revenue": "55000.0",
    "custom_fields": [],
    "integration_fields": []
  }
}
```

---

## Delete organization

**DELETE** `/api/v1/idea_organizations/:id`

### Parameters
- `id` () - **Required** - Numeric ID organization
- `delete_proxy_votes` () - Optional - Boolean to delete the idea organization even if it has proxy votes

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_organizations/138732915" -d '' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
