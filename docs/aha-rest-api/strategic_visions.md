# Strategic visions

## List strategic visions

**GET** `/api/v1/strategy_visions`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/strategy_visions" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "strategy_visions": [
    {
      "id": "262392474",
      "name": "Project 2 Strategy",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "description": null,
      "strategy_vision_components": [],
      "url": "http://company.aha.io/project_strategies/262392474",
      "resource": "http://company.aha.io/project_strategies/262392474",
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
      "id": "613708188",
      "name": "Project 1 Strategy",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "description": null,
      "strategy_vision_components": [
        {
          "id": 669674847,
          "name": "Our market",
          "title": null
        },
        {
          "id": 1055079655,
          "name": "Our strengths",
          "title": null
        }
      ],
      "url": "http://company.aha.io/project_strategies/613708188",
      "resource": "http://company.aha.io/project_strategies/613708188",
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

## Get a specific strategic vision

**GET** `/api/v1/strategy_visions/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the strategic vision

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/strategy_visions/613708188" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "strategy_vision": {
    "id": "613708188",
    "name": "Project 1 Strategy",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "description": null,
    "strategy_vision_components": [
      {
        "id": 669674847,
        "name": "Our market",
        "title": null
      },
      {
        "id": 1055079655,
        "name": "Our strengths",
        "title": null
      }
    ],
    "url": "http://company.aha.io/project_strategies/613708188",
    "resource": "http://company.aha.io/project_strategies/613708188",
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
}
```

---
