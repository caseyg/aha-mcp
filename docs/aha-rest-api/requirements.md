# Requirements

## List requirements for a feature

**GET** `/api/v1/features/:feature_id/requirements`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `q` () - Optional - Search term to match against requirement name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only requirements updated after the timestamp will be returned.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/PRJ1-1/requirements" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirements": [
    {
      "id": "96915428",
      "name": "Body of requirement 2",
      "reference_num": "PRJ1-1-2",
      "position": 2,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "release_id": 278327321,
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "workflow_status": {
        "id": "1025247908",
        "name": "Shipped",
        "position": 5,
        "complete": true,
        "color": "#ecdd8f"
      },
      "url": "http://company.aha.io/requirements/PRJ1-1-2",
      "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-2",
      "description": {
        "id": "6776757454426170483",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "feature": {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "attachments": [],
      "tags": [],
      "full_tags": [],
      "custom_fields": [],
      "integration_fields": [],
      "comments_count": 0
    },
    {
      "id": "483368544",
      "name": "Body of requirement 1",
      "reference_num": "PRJ1-1-1",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "release_id": 278327321,
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "workflow_status": {
        "id": "934242751",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "url": "http://company.aha.io/requirements/PRJ1-1-1",
      "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1",
      "description": {
        "id": "910541534",
        "body": "Body of requirement 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "feature": {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "attachments": [],
      "tags": [],
      "full_tags": [],
      "custom_fields": [
        {
          "id": 848810602,
          "key": "expected_completion_date",
          "name": "Expected completion date",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "2019-01-01",
          "type": "date"
        },
        {
          "id": 731808726,
          "key": "requested_by",
          "name": "Requested By",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "TK",
          "type": "string"
        }
      ],
      "integration_fields": [
        {
          "id": "32487847",
          "name": "key",
          "value": "JRA-987",
          "integration_id": 342659513,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        {
          "id": "417785887",
          "name": "id",
          "value": "991",
          "integration_id": 342659513,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        {
          "id": "803330186",
          "name": "aha::remote_entity",
          "value": "issue_10100",
          "integration_id": 342659513,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "comments_count": 1
    },
    {
      "id": "851574643",
      "name": "Body of requirement 3",
      "reference_num": "PRJ1-1-3",
      "position": 3,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "release_id": 278327321,
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "workflow_status": {
        "id": "922838743",
        "name": "Not started",
        "position": 8,
        "complete": false,
        "color": "#dce790"
      },
      "url": "http://company.aha.io/requirements/PRJ1-1-3",
      "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-3",
      "description": {
        "id": "6776757454439190872",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "feature": {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "attachments": [],
      "tags": [],
      "full_tags": [],
      "custom_fields": [],
      "integration_fields": [],
      "comments_count": 0
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

## Get requirements updated after a certain time

**GET** `/api/v1/features/:feature_id/requirements`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `q` () - Optional - Search term to match against requirement name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only requirements updated after the timestamp will be returned.
- `updated_since` () - Optional - Filter to all requirements updated after this DateTime. Should be specified as an ISO8601 string

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/PRJ1-1/requirements?updated_since=2019-01-01T16%3A09%3A29Z" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirements": [
    {
      "id": "96915428",
      "name": "Body of requirement 2",
      "reference_num": "PRJ1-1-2",
      "position": 2,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "release_id": 278327321,
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "workflow_status": {
        "id": "1025247908",
        "name": "Shipped",
        "position": 5,
        "complete": true,
        "color": "#ecdd8f"
      },
      "url": "http://company.aha.io/requirements/PRJ1-1-2",
      "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-2",
      "description": {
        "id": "6776757454435715611",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "feature": {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "attachments": [],
      "tags": [],
      "full_tags": [],
      "custom_fields": [],
      "integration_fields": [],
      "comments_count": 0
    },
    {
      "id": "851574643",
      "name": "Body of requirement 3",
      "reference_num": "PRJ1-1-3",
      "position": 3,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "release_id": 278327321,
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "workflow_status": {
        "id": "922838743",
        "name": "Not started",
        "position": 8,
        "complete": false,
        "color": "#dce790"
      },
      "url": "http://company.aha.io/requirements/PRJ1-1-3",
      "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-3",
      "description": {
        "id": "6776757454432452959",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "feature": {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "attachments": [],
      "tags": [],
      "full_tags": [],
      "custom_fields": [],
      "integration_fields": [],
      "comments_count": 0
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

## Create a requirement

**POST** `/api/v1/features/:feature_id/requirements`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/requirements" -d '{"requirement":{"name":"New name","workflow_status":{"name":"Designed"},"description":"\u003cp\u003eThis is the description\u003c/p\u003e","assigned_to_user":{"email":"no-reply@aha.io"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirement": {
    "id": "6776757454437184390",
    "name": "New name",
    "reference_num": "PRJ1-1-4",
    "position": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "release_id": 278327321,
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_status": {
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "url": "http://company.aha.io/requirements/PRJ1-1-4",
    "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-4",
    "description": {
      "id": "6776757454426351941",
      "body": "<p>This is the description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "assigned_to_user": {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "attachments": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "integration_fields": [],
    "comments_count": 0,
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ]
  }
}
```

---

## Get a specific requirement

**GET** `/api/v1/requirements/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/requirements/PRJ1-1-1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirement": {
    "id": "483368544",
    "name": "Body of requirement 1",
    "reference_num": "PRJ1-1-1",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "release_id": 278327321,
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "url": "http://company.aha.io/requirements/PRJ1-1-1",
    "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1",
    "description": {
      "id": "910541534",
      "body": "Body of requirement 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "attachments": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [
      {
        "id": 848810602,
        "key": "expected_completion_date",
        "name": "Expected completion date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 731808726,
        "key": "requested_by",
        "name": "Requested By",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "TK",
        "type": "string"
      }
    ],
    "integration_fields": [
      {
        "id": "32487847",
        "name": "key",
        "value": "JRA-987",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "417785887",
        "name": "id",
        "value": "991",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "803330186",
        "name": "aha::remote_entity",
        "value": "issue_10100",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "comments_count": 1
  }
}
```

---

## Update a requirement

**PUT** `/api/v1/requirements/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/PRJ1-1-1" -d '{"requirement":{"name":"Another name","workflow_status":{"name":"Designed"},"description":"\u003cp\u003enew description\u003c/p\u003e"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirement": {
    "id": "483368544",
    "name": "Another name",
    "reference_num": "PRJ1-1-1",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "release_id": 278327321,
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_status": {
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "url": "http://company.aha.io/requirements/PRJ1-1-1",
    "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1",
    "description": {
      "id": "910541534",
      "body": "<p>new description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "attachments": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [
      {
        "id": 848810602,
        "key": "expected_completion_date",
        "name": "Expected completion date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 731808726,
        "key": "requested_by",
        "name": "Requested By",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "TK",
        "type": "string"
      }
    ],
    "integration_fields": [
      {
        "id": "32487847",
        "name": "key",
        "value": "JRA-987",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "417785887",
        "name": "id",
        "value": "991",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "803330186",
        "name": "aha::remote_entity",
        "value": "issue_10100",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "comments_count": 1,
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ]
  }
}
```

---

## Update a requirement's custom fields

**PUT** `/api/v1/requirements/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/PRJ1-1-1" -d '{"requirement":{"custom_fields":{"priority":"P3"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirement": {
    "id": "483368544",
    "name": "Body of requirement 1",
    "reference_num": "PRJ1-1-1",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "release_id": 278327321,
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "url": "http://company.aha.io/requirements/PRJ1-1-1",
    "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1",
    "description": {
      "id": "910541534",
      "body": "Body of requirement 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "attachments": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [
      {
        "id": 848810602,
        "key": "expected_completion_date",
        "name": "Expected completion date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": "6776757454425980250",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      },
      {
        "id": 731808726,
        "key": "requested_by",
        "name": "Requested By",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "TK",
        "type": "string"
      }
    ],
    "integration_fields": [
      {
        "id": "32487847",
        "name": "key",
        "value": "JRA-987",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "417785887",
        "name": "id",
        "value": "991",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "803330186",
        "name": "aha::remote_entity",
        "value": "issue_10100",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "comments_count": 1
  }
}
```

---

## Convert a requirement to a feature

**POST** `/api/v1/requirements/:id/convert_to_feature`

### Parameters
- `id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/PRJ1-1-1/convert_to_feature" -d '' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454429592749",
    "name": "Body of requirement 1",
    "reference_num": "PRJ1-251",
    "initiative_reference_num": null,
    "release_reference_num": "PRJ1-R-1",
    "epic_reference_num": null,
    "position": 1,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_manual",
    "status_changed_on": "2019-01-01",
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_kind": {
      "id": "98484309",
      "name": "New"
    },
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "description": {
      "id": "910541534",
      "body": "Body of requirement 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/features/PRJ1-251",
    "resource": "http://company.aha.io/api/v1/features/PRJ1-251",
    "release": {
      "id": "278327321",
      "reference_num": "PRJ1-R-1",
      "name": "Release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [
        {
          "id": "68217473",
          "name": "id",
          "value": "777",
          "integration_id": 204584239,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "url": "http://company.aha.io/releases/PRJ1-R-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
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
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "requirements": [],
    "goals": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [
      {
        "id": "6776757454437225729",
        "key": "expected_completion_date",
        "name": "Expected completion date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ],
    "feature_links": [
      {
        "link_type": "Relates to",
        "link_type_id": 10,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "Feature 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-1",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "6776757454429592749",
          "reference_num": "PRJ1-251",
          "name": "Body of requirement 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-251",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-251",
          "product_id": "131414752"
        }
      }
    ],
    "workflow_status_times": [
      {
        "status_id": "934242751",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "feature_only_original_estimate": null,
    "feature_only_remaining_estimate": null,
    "feature_only_work_done": null
  }
}
```

---

## Delete a requirement

**DELETE** `/api/v1/requirements/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/PRJ1-1-1" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
