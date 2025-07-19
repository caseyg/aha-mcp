# Strategic models

## List strategic models

**GET** `/api/v1/strategy_models`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/strategy_models" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "strategy_models": [
    {
      "id": "111251416",
      "name": "Aha! business model canvas",
      "kind": "Business",
      "components": [
        {
          "id": 62803905,
          "name": "Growth opportunity",
          "description": ""
        }
      ],
      "url": "http://company.aha.io/business_models/111251416",
      "resource": "http://company.aha.io/business_models/111251416",
      "project": {
        "id": "517761884",
        "reference_prefix": "PRJ2",
        "name": "Project 2",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ2"
      }
    },
    {
      "id": "356242517",
      "name": "Aha! business model canvas",
      "kind": "Business",
      "components": [
        {
          "id": 310750587,
          "name": "Value Proposition",
          "description": ""
        }
      ],
      "url": "http://company.aha.io/business_models/356242517",
      "resource": "http://company.aha.io/business_models/356242517",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      }
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

## Get a specific strategic model

**GET** `/api/v1/strategy_models/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the strategic model

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/strategy_models/111251416" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "strategy_model": {
    "id": "111251416",
    "name": "Aha! business model canvas",
    "kind": "Business",
    "components": [
      {
        "id": 62803905,
        "name": "Growth opportunity",
        "description": ""
      }
    ],
    "url": "http://company.aha.io/business_models/111251416",
    "resource": "http://company.aha.io/business_models/111251416",
    "project": {
      "id": "517761884",
      "reference_prefix": "PRJ2",
      "name": "Project 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ2"
    }
  }
}
```

---
