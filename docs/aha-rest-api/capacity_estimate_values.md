# Capacity estimate values

## Create estimate values for a capacity investment

**POST** `/api/v1/capacity_investments/:id/estimate_values`

### Additional Information
Estimate value objects should include the following keys: `team_id`, `period_start`, and `total`. This endpoint uses an "upsert" flow, updating existing records, or creating new ones if they do not exist. Returns all updated and destroyed estimate values, including computed sums and ignored values.

### Parameters
- `id` () - **Required** - Numeric ID of the capacity investment
- `estimate_values` () - **Required** - An array (or object) of estimate values to create/update.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/capacity_investments/756888381/estimate_values" -d '{"estimate_values":[{"team_id":949295028,"period_start":"2019-01-01","total":5},{"team_id":949295028,"period_start":"2019-01-01","total":10},{"team_id":563889676,"period_start":"2019-01-01","total":15},{"team_id":563889676,"period_start":"2019-01-01","total":20}]}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "updated": [
    {
      "id": "6776757454429507403",
      "team_id": 563889676,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 15,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454431187018",
      "team_id": 563889676,
      "team_membership_id": null,
      "period_start": null,
      "total": 35,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454432001078",
      "team_id": null,
      "team_membership_id": null,
      "period_start": null,
      "total": 50,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454432404946",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 25,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454432818342",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 5,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454434050607",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 5,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454435601712",
      "team_id": 563889676,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 20,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454436580757",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": null,
      "total": 15,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454440008335",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 10,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454441112000",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 20,
      "computed": true,
      "ignored": false
    }
  ],
  "destroyed": []
}
```

---

## List estimate values for a capacity investment

**GET** `/api/v1/capacity_investments/:id/estimate_values`

### Parameters
- `id` () - **Required** - Numeric ID of the capacity investment

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/capacity_investments/756888381/estimate_values" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "estimate_values": [
    {
      "id": "6776757454425444038",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 5,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454427101009",
      "team_id": 563889676,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 20,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454429237268",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 10,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454429653768",
      "team_id": 563889676,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 15,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454436513154",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 20,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454438999366",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 5,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454439734229",
      "team_id": 563889676,
      "team_membership_id": null,
      "period_start": null,
      "total": 35,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454440093884",
      "team_id": null,
      "team_membership_id": null,
      "period_start": null,
      "total": 50,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454440558858",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 25,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454440784576",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": null,
      "total": 15,
      "computed": true,
      "ignored": false
    }
  ],
  "pagination": {
    "total_records": 10,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Update an estimate value

**PUT** `/api/v1/estimate_values/:id`

### Additional Information
Returns all updated estimate values, including computed sums and ignored values.

### Parameters
- `id` () - **Required** - Numeric ID of the estimate value

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/estimate_values/6776757454432999030" -d '{"estimate_value":{"total":20}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "updated": [
    {
      "id": "6776757454429344017",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": null,
      "total": 25,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454432677207",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 35,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454432999030",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 20,
      "computed": false,
      "ignored": false
    },
    {
      "id": "6776757454434437219",
      "team_id": null,
      "team_membership_id": null,
      "period_start": null,
      "total": 60,
      "computed": true,
      "ignored": false
    }
  ],
  "destroyed": []
}
```

---

## Delete an estimate value

**DELETE** `/api/v1/estimate_values/:id`

### Additional Information
Returns all updated and destroyed estimate values, including computed sums and ignored values.

### Parameters
- `id` () - **Required** - Numeric ID of the estimate value

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/estimate_values/6776757454428129123" -d '{}' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "updated": [
    {
      "id": "6776757454433616842",
      "team_id": null,
      "team_membership_id": null,
      "period_start": null,
      "total": 40,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454435310863",
      "team_id": null,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 15,
      "computed": true,
      "ignored": false
    },
    {
      "id": "6776757454438130820",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": null,
      "total": 5,
      "computed": true,
      "ignored": false
    }
  ],
  "destroyed": [
    {
      "id": "6776757454428129123",
      "team_id": 949295028,
      "team_membership_id": null,
      "period_start": "2019-01-01",
      "total": 10,
      "computed": false,
      "ignored": false
    }
  ]
}
```

---
