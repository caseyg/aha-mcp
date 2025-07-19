# Capacity investments

## Create a capacity investment on an initiative

**POST** `/api/v1/initiatives/:initiative_id/capacity_investments`

### Parameters
- `initiative_id` () - **Required** - Numeric ID or key of the initiative
- `start_date` () - Optional - The start date for the capacity investment in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the capacity investment in format YYYY-MM-DD
- `date_source` () - Optional - The date source for the capacity investment, can be one of: `manual_dates`, `capacity_plannable`
- `estimate_source` () - Optional - The estimate source for the capacity investment, can be one of: `manual_estimate`, `features`, `epics`
- `capacity_scenario_id` () - Optional - Numeric ID of the capacity scenario

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/initiatives/PL1-S-1/capacity_investments" -d '{"capacity_investment":{"start_date":"2019-01-01","end_date":"2019-01-01","date_source":"manual_dates","estimate_source":"epics"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "6776757454426063757",
    "capacity_scenario_id": "997808419",
    "total": 0,
    "estimate_source": "epics",
    "date_source": "manual_dates",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "initiative": {
      "id": "1042392694",
      "reference_num": "PL1-S-1",
      "name": "Workspace line initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/initiatives/PL1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PL1-S-1"
    },
    "estimate_values": [
      {
        "id": "6776757454428757103",
        "team_id": null,
        "team_membership_id": null,
        "period_start": null,
        "total": 0,
        "computed": true,
        "ignored": false
      }
    ],
    "custom_fields": []
  }
}
```

---

## Create a capacity investment on an epic

**POST** `/api/v1/epics/:epic_id/capacity_investments`

### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the epic
- `start_date` () - Optional - The start date for the capacity investment in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the capacity investment in format YYYY-MM-DD
- `date_source` () - Optional - The date source for the capacity investment, can be one of: `manual_dates`, `capacity_plannable`
- `estimate_source` () - Optional - The estimate source for the capacity investment, can be one of: `manual_estimate`, `features`, `epics`
- `capacity_scenario_id` () - Optional - Numeric ID of the capacity scenario

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1/capacity_investments" -d '{"capacity_investment":{"start_date":"2019-01-01","end_date":"2019-01-01","date_source":"manual_dates","estimate_source":"features"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "6776757454435339103",
    "capacity_scenario_id": "997808419",
    "total": 0,
    "estimate_source": "features",
    "date_source": "manual_dates",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "master_feature": {
      "id": "999605892",
      "reference_num": "PRJ1-E-1",
      "name": "Epic 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
    },
    "epic": {
      "id": "999605892",
      "reference_num": "PRJ1-E-1",
      "name": "Epic 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
    },
    "estimate_values": [
      {
        "id": "6776757454438616702",
        "team_id": null,
        "team_membership_id": null,
        "period_start": null,
        "total": 0,
        "computed": true,
        "ignored": false
      }
    ],
    "custom_fields": []
  }
}
```

---

## Create a Capacity Investment with custom fields

**POST** `/api/v1/features/:feature_id/capacity_investments`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `start_date` () - Optional - The start date for the capacity investment in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the capacity investment in format YYYY-MM-DD
- `date_source` () - Optional - The date source for the capacity investment, can be one of: `manual_dates`, `capacity_plannable`
- `estimate_source` () - Optional - The estimate source for the capacity investment, can be one of: `manual_estimate`, `features`, `epics`
- `capacity_scenario_id` () - Optional - Numeric ID of the capacity scenario

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/capacity_investments" -d '{"capacity_investment":{"start_date":"2019-01-01","end_date":"2019-01-01","date_source":"manual_dates","custom_fields":{"priority":"P3"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "6776757454432476020",
    "capacity_scenario_id": "997808419",
    "total": null,
    "estimate_source": "manual_estimate",
    "date_source": "manual_dates",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "estimate_values": [],
    "custom_fields": [
      {
        "id": "6776757454428080736",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ]
  }
}
```

---

## Create a capacity investment on a feature

**POST** `/api/v1/features/:feature_id/capacity_investments`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `start_date` () - Optional - The start date for the capacity investment in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the capacity investment in format YYYY-MM-DD
- `date_source` () - Optional - The date source for the capacity investment, can be one of: `manual_dates`, `capacity_plannable`
- `estimate_source` () - Optional - The estimate source for the capacity investment, can be one of: `manual_estimate`, `features`, `epics`
- `capacity_scenario_id` () - Optional - Numeric ID of the capacity scenario

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/capacity_investments" -d '{"capacity_investment":{"start_date":"2019-01-01","end_date":"2019-01-01","date_source":"manual_dates","estimate_source":"manual_estimate","estimate_values":[{"team_id":949295028,"period_start":"2019-01-01","total":5},{"team_id":949295028,"period_start":"2019-01-01","total":10},{"team_id":563889676,"period_start":"2019-01-01","total":15},{"team_id":563889676,"period_start":"2019-01-01","total":20}]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "6776757454438949536",
    "capacity_scenario_id": "997808419",
    "total": null,
    "estimate_source": "manual_estimate",
    "date_source": "manual_dates",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "estimate_values": [],
    "custom_fields": []
  }
}
```

---

## List capacity investments for a product

**GET** `/api/v1/products/:product_id/capacity_investments`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/capacity_investments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investments": [
    {
      "id": "756888381",
      "capacity_scenario_id": "997808419",
      "total": null
    },
    {
      "id": "873751177",
      "capacity_scenario_id": "997808419",
      "total": 100
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

## List capacity investments for an initiative

**GET** `/api/v1/initiatives/:initiative_id/capacity_investments`

### Parameters
- `initiative_id` () - **Required** - Numeric ID or key of the initiative

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/PRJ1-S-1/capacity_investments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investments": [
    {
      "id": "756888381",
      "capacity_scenario_id": "997808419",
      "total": null
    }
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List capacity investments for an epic

**GET** `/api/v1/epics/:epic_id/capacity_investments`

### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the epic

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics/PRJ1-E-1/capacity_investments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investments": [
    {
      "id": "6776757454436984798",
      "capacity_scenario_id": "997808419",
      "total": null
    }
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List capacity investments for a feature

**GET** `/api/v1/features/:feature_id/capacity_investments`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/PRJ1-1/capacity_investments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investments": [
    {
      "id": "6776757454440832494",
      "capacity_scenario_id": "997808419",
      "total": null
    }
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a capacity investment

**GET** `/api/v1/capacity_investments/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the capacity investment

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/capacity_investments/6776757454434119448" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "6776757454434119448",
    "capacity_scenario_id": "997808419",
    "total": 50,
    "estimate_source": "manual_estimate",
    "date_source": "capacity_plannable",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "estimate_values": [
      {
        "id": "6776757454426052428",
        "team_id": null,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 20,
        "computed": true,
        "ignored": false
      },
      {
        "id": "6776757454427431419",
        "team_id": null,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 5,
        "computed": true,
        "ignored": false
      },
      {
        "id": "6776757454429265039",
        "team_id": null,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 25,
        "computed": true,
        "ignored": false
      },
      {
        "id": "6776757454431413411",
        "team_id": 949295028,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 5,
        "computed": false,
        "ignored": false
      },
      {
        "id": "6776757454433361039",
        "team_id": 563889676,
        "team_membership_id": null,
        "period_start": null,
        "total": 35,
        "computed": true,
        "ignored": false
      },
      {
        "id": "6776757454434557336",
        "team_id": 949295028,
        "team_membership_id": null,
        "period_start": null,
        "total": 15,
        "computed": true,
        "ignored": false
      },
      {
        "id": "6776757454435055775",
        "team_id": 949295028,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 10,
        "computed": false,
        "ignored": false
      },
      {
        "id": "6776757454438272224",
        "team_id": null,
        "team_membership_id": null,
        "period_start": null,
        "total": 50,
        "computed": true,
        "ignored": false
      },
      {
        "id": "6776757454439437930",
        "team_id": 563889676,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 20,
        "computed": false,
        "ignored": false
      },
      {
        "id": "6776757454441108665",
        "team_id": 563889676,
        "team_membership_id": null,
        "period_start": "2019-01-01",
        "total": 15,
        "computed": false,
        "ignored": false
      }
    ],
    "custom_fields": [
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ]
  }
}
```

---

## Update a capacity investment's custom fields

**PUT** `/api/v1/capacity_investments/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the capacity investment
- `start_date` () - Optional - The start date for the capacity investment in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the capacity investment in format YYYY-MM-DD
- `date_source` () - Optional - The date source for the capacity investment, can be one of: `manual_dates`, `capacity_plannable`
- `estimate_source` () - Optional - The estimate source for the capacity investment, can be one of: `manual_estimate`, `features`, `epics`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/capacity_investments/756888381" -d '{"capacity_investment":{"start_date":"2019-01-01","end_date":"2019-01-01","date_source":"manual_dates","custom_fields":{"priority":"P3"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "756888381",
    "capacity_scenario_id": "997808419",
    "total": null,
    "estimate_source": "manual_estimate",
    "date_source": "manual_dates",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "initiative": {
      "id": "423077122",
      "reference_num": "PRJ1-S-1",
      "name": "Initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1"
    },
    "estimate_values": [],
    "custom_fields": [
      {
        "id": "6776757454439611637",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ]
  }
}
```

---

## Update a capacity investment

**PUT** `/api/v1/capacity_investments/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the capacity investment
- `start_date` () - Optional - The start date for the capacity investment in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the capacity investment in format YYYY-MM-DD
- `date_source` () - Optional - The date source for the capacity investment, can be one of: `manual_dates`, `capacity_plannable`
- `estimate_source` () - Optional - The estimate source for the capacity investment, can be one of: `manual_estimate`, `features`, `epics`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/capacity_investments/756888381" -d '{"capacity_investment":{"date_source":"manual_dates","start_date":"2019-01-01","end_date":"2019-01-01"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "capacity_investment": {
    "id": "756888381",
    "capacity_scenario_id": "997808419",
    "total": null,
    "estimate_source": "manual_estimate",
    "date_source": "manual_dates",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "initiative": {
      "id": "423077122",
      "reference_num": "PRJ1-S-1",
      "name": "Initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1"
    },
    "estimate_values": [],
    "custom_fields": []
  }
}
```

---
