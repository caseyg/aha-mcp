# Key results

## List key results for a goal

**GET** `/api/v1/goals/:goal_id/key_results`

### Parameters
- `goal_id` () - **Required** - Numeric ID or key of the goal

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/DEMOENT-G-1/key_results" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "key_results": [
    {
      "id": "631791848",
      "name": "KR 1",
      "reference_num": "DEMOENT-G-1-KR-1",
      "position": 2,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "target_metric": "100%",
      "starting_metric": "5%",
      "current_metric": "20%",
      "description": {
        "id": "6776757454425693046",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "assigned_to_user": null,
      "workflow_status": {
        "id": "934242751",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "custom_fields": []
    },
    {
      "id": "1017196896",
      "name": "KR 2",
      "reference_num": "DEMOENT-G-1-KR-2",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "target_metric": null,
      "starting_metric": null,
      "current_metric": null,
      "description": {
        "id": "6776757454425388265",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "assigned_to_user": null,
      "workflow_status": {
        "id": "934242751",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "custom_fields": []
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

## Get a specific key result

**GET** `/api/v1/key_results/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the key results

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/key_results/DEMOENT-G-1-KR-1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "key_result": {
    "id": "631791848",
    "name": "KR 1",
    "reference_num": "DEMOENT-G-1-KR-1",
    "position": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": null,
    "target_metric": "100%",
    "starting_metric": "5%",
    "current_metric": "20%",
    "description": {
      "id": "6776757454427543858",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "assigned_to_user": null,
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "custom_fields": []
  }
}
```

---

## Update a key result

**PUT** `/api/v1/key_results/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the key result

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/key_results/DEMOENT-G-1-KR-1" -d '{"key_result":{"name":"Another name","workflow_status":{"name":"On track"},"watchers":[689956296],"description":"\u003cp\u003enew description\u003c/p\u003e","current_metric":"30%"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "key_result": {
    "id": "631791848",
    "name": "Another name",
    "reference_num": "DEMOENT-G-1-KR-1",
    "position": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": null,
    "target_metric": "100%",
    "starting_metric": "5%",
    "current_metric": "30%",
    "description": {
      "id": "6776757454427142951",
      "body": "<p>new description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "assigned_to_user": null,
    "workflow_status": {
      "id": "76947914",
      "name": "On Track",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "custom_fields": []
  }
}
```

---

## Update a key result's custom fields

**PUT** `/api/v1/key_results/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the key result

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/key_results/DEMOENT-G-1-KR-1" -d '{"key_result":{"custom_fields":{"stretch_goal":"my metric"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "key_result": {
    "id": "631791848",
    "name": "KR 1",
    "reference_num": "DEMOENT-G-1-KR-1",
    "position": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": null,
    "target_metric": "100%",
    "starting_metric": "5%",
    "current_metric": "20%",
    "description": {
      "id": "",
      "body": "#<note:0x00007fff6d2494c8></note:0x00007fff6d2494c8>",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "assigned_to_user": null,
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "custom_fields": [
      {
        "id": "6776757454438848098",
        "key": "stretch_goal",
        "name": "Stretch goal",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "my metric",
        "type": "string"
      }
    ]
  }
}
```

---

## Create a key result

**POST** `/api/v1/goals/:goal_id/key_results`

### Parameters
- `goal_id` () - **Required** - Numeric ID or key of the goal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/goals/DEMOENT-G-1/key_results" -d '{"key_result":{"name":"New name","workflow_status":{"name":"On track"},"description":"\u003cp\u003eThis is the description\u003c/p\u003e","assigned_to_user":{"email":"no-reply@aha.io"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "key_result": {
    "id": "6776757454425500445",
    "name": "New name",
    "reference_num": "DEMOENT-G-1-KR-1",
    "position": 3,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": 0,
    "target_metric": null,
    "starting_metric": null,
    "current_metric": null,
    "description": {
      "id": "6776757454430143412",
      "body": "<p>This is the description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "assigned_to_user": {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "workflow_status": {
      "id": "76947914",
      "name": "On Track",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "custom_fields": []
  }
}
```

---

## Delete a key result

**DELETE** `/api/v1/key_results/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the key_result

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/key_results/DEMOENT-G-1-KR-1" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
