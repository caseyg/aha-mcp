# Strategic positionings

## List strategic positionings

**GET** `/api/v1/strategy_positions`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/strategy_positions" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "strategy_positions": [
    {
      "id": "51832287",
      "name": "Aha! strategic positioning model canvas",
      "kind": "Positioning",
      "components": [
        {
          "id": 260808894,
          "name": "Value Proposition",
          "description": ""
        }
      ],
      "url": "http://company.aha.io/business_models/51832287",
      "resource": "http://company.aha.io/business_models/51832287",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      }
    },
    {
      "id": "453528824",
      "name": "Aha! strategic positioning model canvas",
      "kind": "Positioning",
      "components": [
        {
          "id": 37485938,
          "name": "Growth opportunity",
          "description": ""
        }
      ],
      "url": "http://company.aha.io/business_models/453528824",
      "resource": "http://company.aha.io/business_models/453528824",
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
  ],
  "pagination": {
    "total_records": 2,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific strategic positioning

**GET** `/api/v1/strategy_positions/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the strategic positioning

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/strategy_positions/453528824" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "strategy_positioning": {
    "id": "453528824",
    "name": "Aha! strategic positioning model canvas",
    "kind": "Positioning",
    "components": [
      {
        "id": 37485938,
        "name": "Growth opportunity",
        "description": ""
      }
    ],
    "url": "http://company.aha.io/business_models/453528824",
    "resource": "http://company.aha.io/business_models/453528824",
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
