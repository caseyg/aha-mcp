# Capacity scenarios

## List capacity scenarios

**GET** `/api/v1/capacity_scenarios`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/capacity_scenarios" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_scenarios": [
    {
      "id": 16603097,
      "name": "Custom test scenario",
      "planning_interval": "month",
      "planning_start_date": "2019-01-01",
      "planning_end_date": "2019-01-01",
      "estimate_value_layout": "team_by_time",
      "data_entry_units": "custom",
      "archived": false
    },
    {
      "id": 454855257,
      "name": "Second test scenario",
      "planning_interval": "month",
      "planning_start_date": "2019-01-01",
      "planning_end_date": "2019-01-01",
      "estimate_value_layout": "team_by_time",
      "data_entry_units": "headcount",
      "archived": false
    },
    {
      "id": 997808419,
      "name": "Default test scenario",
      "planning_interval": "month",
      "planning_start_date": "2019-01-01",
      "planning_end_date": "2019-01-01",
      "estimate_value_layout": "team_by_time",
      "data_entry_units": "headcount",
      "archived": false
    }
  ],
  "pagination": {
    "total_records": 3,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a capacity scenario

**GET** `/api/v1/capacity_scenarios/:id`

### Parameters
- `id` () - Optional - Id

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/capacity_scenarios/997808419" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_scenario": {
    "id": 997808419,
    "name": "Default test scenario",
    "planning_interval": "month",
    "planning_start_date": "2019-01-01",
    "planning_end_date": "2019-01-01",
    "estimate_value_layout": "team_by_time",
    "data_entry_units": "headcount",
    "archived": false
  }
}
```

---
