# Integration fields

## Create an integration field for a feature by integration ID

**POST** `/api/v1/features/:feature_id/integrations/:integration_id/fields`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `integration_id` () - **Required** - Numeric ID of the integration

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/integrations/204584239/fields" -d '{"integration_field":{"name":"key","value":"JRA-34"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration_field": {
    "id": "728894778",
    "name": "key",
    "value": "JRA-34",
    "integration_id": 204584239,
    "service_name": "jira",
    "created_at": "2019-01-01T00:00:00.000Z",
    "integratable": {
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## Create multiple integration fields for a feature by integration ID

**POST** `/api/v1/features/:feature_id/integrations/:integration_id/fields`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `integration_id` () - **Required** - Numeric ID of the integration

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/integrations/204584239/fields" -d '{"integration_fields":[{"name":"key","value":"JRA-34"},{"name":"id","value":"34"}]}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "728894778": null,
  "846945422": null
}
```

---

## Create an integration field for a feature by service name

**POST** `/api/v1/features/:feature_id/integrations/:service_name/fields`

### Additional Information
DEPRECATED: provide :integration_id rather than :service_name to identify the integration.

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `service_name` () - **Required** - Name of the integration service

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/integrations/jira/fields" -d '{"integration_field":{"name":"key","value":"JRA-34"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration_field": {
    "id": "728894778",
    "name": "key",
    "value": "JRA-34",
    "integration_id": 204584239,
    "service_name": "jira",
    "created_at": "2019-01-01T00:00:00.000Z",
    "integratable": {
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## Create multiple integration fields for a feature by service name

**POST** `/api/v1/features/:feature_id/integrations/:service_name/fields`

### Additional Information
DEPRECATED: provide :integration_id rather than :service_name to identify the integration.

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `service_name` () - **Required** - Name of the integration service

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1/integrations/jira/fields" -d '{"integration_fields":[{"name":"key","value":"JRA-34"},{"name":"id","value":"34"}]}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "728894778": null,
  "846945422": null
}
```

---

## Create an integration field for a epic by integration ID

**POST** `/api/v1/epics/:epic_id/integrations/:integration_id/fields`

### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the feature
- `integration_id` () - **Required** - Numeric ID of the integration

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1/integrations/204584239/fields" -d '{"integration_field":{"name":"key","value":"JRA-34"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration_field": {
    "id": "907392375",
    "name": "key",
    "value": "JRA-34",
    "integration_id": 204584239,
    "service_name": "jira",
    "created_at": "2019-01-01T00:00:00.000Z",
    "integratable": {
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
    }
  }
}
```

---

## Create multiple integration fields for a epic by integration ID

**POST** `/api/v1/epics/:epic_id/integrations/:integration_id/fields`

### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the feature
- `integration_id` () - **Required** - Numeric ID of the integration

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1/integrations/204584239/fields" -d '{"integration_fields":[{"name":"key","value":"JRA-34"},{"name":"id","value":"34"}]}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "790422735": null,
  "907392375": null
}
```

---

## Create an integration field for an idea vote

**POST** `/api/v1/idea_endorsements/:idea_endorsement_id/integrations/:integration_id/fields`

### Parameters
- `idea_endorsement_id` () - **Required** - Numeric ID of the idea vote
- `integration_id` () - **Required** - Numeric ID of the integration

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_endorsements/53377392/integrations/204584239/fields" -d '{"integration_field":{"name":"key","value":"JRA-34"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration_field": {
    "id": "975466318",
    "name": "key",
    "value": "JRA-34",
    "integration_id": 204584239,
    "service_name": "jira",
    "created_at": "2019-01-01T00:00:00.000Z",
    "integratable": {
      "url": "http://company.aha.io/ideas/idea_endorsements/53377392",
      "resource": "http://company.aha.io/api/v1/ideas/idea_endorsements/53377392"
    }
  }
}
```

---

## Get a specific integration field value

**GET** `/api/v1/features/:feature_id/integrations/:integration_id/fields/:field_name`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature
- `integration_id` () - **Required** - Numeric ID of the integration
- `field_name` () - **Required** - Name of the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/PRJ1-1/integrations/204584239/fields/key" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "integration_field": {
    "id": "728894778",
    "name": "key",
    "value": "JRA-123",
    "integration_id": 204584239,
    "service_name": "jira",
    "created_at": "2019-01-01T00:00:00.000Z",
    "integratable": {
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## List records with an associated integration field value

**GET** `/api/v1/integrations/:integration_id/fields/:field_name/value/:field_value`

### Additional Information
Possible records are releases, initiatives, features, epics, requirements or idea votes.


### Parameters
- `integration_id` () - **Required** - Numeric ID of the integration
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/integrations/204584239/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [
    {
      "feature": {
        "integration_id": 204584239,
        "service_name": "jira",
        "id": "1007868956",
        "name": "Feature 1",
        "reference_num": "PRJ1-1",
        "initiative_reference_num": "PRJ1-S-1",
        "release_reference_num": "PRJ1-R-1",
        "epic_reference_num": "PRJ1-E-1",
        "position": 1,
        "score": 3,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "start_date": "2019-01-01",
        "due_date": "2019-01-01",
        "product_id": "131414752",
        "progress": null,
        "progress_source": "progress_manual",
        "status_changed_on": null,
        "created_by_user": {
          "id": "16338845",
          "name": "John Smith",
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
          "id": "793547626",
          "body": "Body of note 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": [
            {
              "id": "724655692",
              "download_url": "https://company.aha.io/attachments/724655692/token/aaabbbccc7.download?size=original",
              "created_at": "2019-01-01T00:00:00.000Z",
              "updated_at": "2019-01-01T00:00:00.000Z",
              "original_file_size": 123,
              "content_type": "text/plain",
              "file_name": "uploaded_file_name.txt",
              "file_size": 123
            }
          ]
        },
        "attachments": [],
        "integration_fields": [
          {
            "id": "92040219",
            "name": "url",
            "value": "https://bigaha.atlassian.net/issues/JRA-123",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "728894778",
            "name": "key",
            "value": "JRA-123",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "846945422",
            "name": "id",
            "value": "435",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
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
        "master_feature": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        },
        "belongs_to_release_phase": {
          "id": "20526005",
          "name": "Alpha",
          "start_on": "2019-01-01",
          "end_on": "2019-01-01",
          "type": "phase",
          "release_id": 278327321,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "progress_source": "progress_manual",
          "duration_source": "duration_manual",
          "description": {
            "id": "243384959",
            "body": "Description of release phase 1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          }
        },
        "epic": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        },
        "assigned_to_user": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "default_assignee": false
        },
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
              "id": "6776757454441064437",
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
              "id": "6776757454438120306",
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
        "initiative": {
          "id": "423077122",
          "reference_num": "PRJ1-S-1",
          "name": "Initiative 1",
          "url": "http://company.aha.io/initiatives/PRJ1-S-1",
          "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "description": {
            "id": "673273729",
            "body": "Description of initiative 1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          },
          "integration_fields": [
            {
              "id": "546711007",
              "name": "id",
              "value": "9913333",
              "integration_id": 186281709,
              "service_name": "jira",
              "created_at": "2019-01-01T00:00:00.000Z"
            },
            {
              "id": "966751335",
              "name": "key",
              "value": "JRA-987222",
              "integration_id": 186281709,
              "service_name": "jira",
              "created_at": "2019-01-01T00:00:00.000Z"
            }
          ]
        },
        "goals": [
          {
            "id": "602095703",
            "name": "Goal 1",
            "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
            "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "description": {
              "id": "166463080",
              "body": "Description of goal 1",
              "created_at": "2019-01-01T00:00:00.000Z",
              "updated_at": "2019-01-01T00:00:00.000Z",
              "attachments": []
            }
          }
        ],
        "comments_count": 1,
        "score_facts": [
          {
            "id": "728895917",
            "value": 1,
            "name": "Effort"
          },
          {
            "id": "846938137",
            "value": 2,
            "name": "Benefit"
          }
        ],
        "tags": [
          "Engineering",
          "Infrastructure"
        ],
        "full_tags": [
          {
            "id": 3412727,
            "name": "Engineering",
            "color": "#e09052"
          },
          {
            "id": 775582684,
            "name": "Infrastructure",
            "color": "#7552e0"
          }
        ],
        "custom_fields": [
          {
            "id": 1051489895,
            "key": "equation_specs_field",
            "name": "Equation specs field",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": {
              "values": {
                "123": {
                  "value": 10,
                  "name": "a",
                  "display_value": "10.0"
                },
                "456": {
                  "value": "Foobar",
                  "name": "b",
                  "display_value": "Foobar"
                },
                "789": {
                  "value": null,
                  "name": "789",
                  "display_value": null
                }
              }
            },
            "type": "equation_sheet"
          },
          {
            "id": 621325984,
            "key": "expected_completion_date",
            "name": "Expected completion date",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": "2019-01-01",
            "type": "date"
          },
          {
            "id": 694694494,
            "key": "negative_scorecard",
            "name": "Negative custom scorecard",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": 31,
            "type": "scorecard",
            "score_facts": [
              {
                "id": "462102328",
                "value": 6,
                "name": "Negative default value"
              }
            ]
          },
          {
            "id": 736691743,
            "key": "upload",
            "name": "Upload",
            "updatedAt": "2019-01-01T00:00:00Z",
            "attachments": [
              {
                "id": "471688235",
                "download_url": "https://company.aha.io/attachments/471688235/token/aaabbbccc7.download?size=original",
                "created_at": "2019-01-01T00:00:00.000Z",
                "updated_at": "2019-01-01T00:00:00.000Z",
                "original_file_size": 123,
                "content_type": "text/plain",
                "file_name": "uploaded_file_name.txt",
                "file_size": 123
              }
            ],
            "type": "attachment"
          }
        ],
        "feature_links": [
          {
            "link_type": "Depends on",
            "link_type_id": 20,
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
              "id": "622562724",
              "reference_num": "PRJ1-2",
              "name": "Another Feature",
              "created_at": "2019-01-01T00:00:00.000Z",
              "url": "http://company.aha.io/features/PRJ1-2",
              "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
              "product_id": "131414752"
            }
          }
        ],
        "feature_only_original_estimate": null,
        "feature_only_remaining_estimate": null,
        "feature_only_work_done": null
      }
    },
    {
      "idea_endorsement": {
        "integration_id": 204584239,
        "service_name": "jira",
        "id": "53377392",
        "idea_id": "58056975",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "value": null,
        "link": null,
        "weight": 1,
        "endorsed_by_portal_user": {
          "id": "646391926",
          "name": "John Long",
          "email": "john@long.com",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        "endorsed_by_idea_user": {
          "id": "1056507375",
          "name": "John Long",
          "email": "john@long.com",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        "idea_organization": {
          "id": "138732915",
          "name": "Acme",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/ideas/idea_organizations/138732915",
          "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
        },
        "description": {
          "id": "6776757454434311202",
          "body": "",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "integration_fields": [
          {
            "id": "975466318",
            "name": "key",
            "value": "JRA-123",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "custom_fields": [],
        "idea": {
          "id": "58056975",
          "reference_num": "PRJ1-I-1",
          "name": "Idea 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "workflow_status": {
            "id": "3259216",
            "name": "New",
            "position": 1,
            "complete": false,
            "color": "#dce7c6"
          },
          "description": {
            "id": "103757394",
            "body": "Description of idea 1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          },
          "url": "http://company.aha.io/ideas/ideas/PRJ1-I-1",
          "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-1"
        }
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

## List releases with an associated integration field value

**GET** `/api/v1/releases/fields/:field_name/value/:field_value`

### Parameters
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List initiatives with an associated integration field value

**GET** `/api/v1/initiatives/fields/:field_name/value/:field_value`

### Parameters
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List features with an associated integration field value

**GET** `/api/v1/features/fields/:field_name/value/:field_value`

### Parameters
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [
    {
      "feature": {
        "integration_id": 204584239,
        "service_name": "jira",
        "id": "1007868956",
        "name": "Feature 1",
        "reference_num": "PRJ1-1",
        "initiative_reference_num": "PRJ1-S-1",
        "release_reference_num": "PRJ1-R-1",
        "epic_reference_num": "PRJ1-E-1",
        "position": 1,
        "score": 3,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "start_date": "2019-01-01",
        "due_date": "2019-01-01",
        "product_id": "131414752",
        "progress": null,
        "progress_source": "progress_manual",
        "status_changed_on": null,
        "created_by_user": {
          "id": "16338845",
          "name": "John Smith",
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
          "id": "793547626",
          "body": "Body of note 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": [
            {
              "id": "724655692",
              "download_url": "https://company.aha.io/attachments/724655692/token/aaabbbccc7.download?size=original",
              "created_at": "2019-01-01T00:00:00.000Z",
              "updated_at": "2019-01-01T00:00:00.000Z",
              "original_file_size": 123,
              "content_type": "text/plain",
              "file_name": "uploaded_file_name.txt",
              "file_size": 123
            }
          ]
        },
        "attachments": [],
        "integration_fields": [
          {
            "id": "92040219",
            "name": "url",
            "value": "https://bigaha.atlassian.net/issues/JRA-123",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "728894778",
            "name": "key",
            "value": "JRA-123",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "846945422",
            "name": "id",
            "value": "435",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
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
        "master_feature": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        },
        "belongs_to_release_phase": {
          "id": "20526005",
          "name": "Alpha",
          "start_on": "2019-01-01",
          "end_on": "2019-01-01",
          "type": "phase",
          "release_id": 278327321,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "progress_source": "progress_manual",
          "duration_source": "duration_manual",
          "description": {
            "id": "243384959",
            "body": "Description of release phase 1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          }
        },
        "epic": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        },
        "assigned_to_user": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "default_assignee": false
        },
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
              "id": "6776757454428574024",
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
              "id": "6776757454431604199",
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
        "initiative": {
          "id": "423077122",
          "reference_num": "PRJ1-S-1",
          "name": "Initiative 1",
          "url": "http://company.aha.io/initiatives/PRJ1-S-1",
          "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "description": {
            "id": "673273729",
            "body": "Description of initiative 1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          },
          "integration_fields": [
            {
              "id": "546711007",
              "name": "id",
              "value": "9913333",
              "integration_id": 186281709,
              "service_name": "jira",
              "created_at": "2019-01-01T00:00:00.000Z"
            },
            {
              "id": "966751335",
              "name": "key",
              "value": "JRA-987222",
              "integration_id": 186281709,
              "service_name": "jira",
              "created_at": "2019-01-01T00:00:00.000Z"
            }
          ]
        },
        "goals": [
          {
            "id": "602095703",
            "name": "Goal 1",
            "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
            "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "description": {
              "id": "166463080",
              "body": "Description of goal 1",
              "created_at": "2019-01-01T00:00:00.000Z",
              "updated_at": "2019-01-01T00:00:00.000Z",
              "attachments": []
            }
          }
        ],
        "comments_count": 1,
        "score_facts": [
          {
            "id": "728895917",
            "value": 1,
            "name": "Effort"
          },
          {
            "id": "846938137",
            "value": 2,
            "name": "Benefit"
          }
        ],
        "tags": [
          "Engineering",
          "Infrastructure"
        ],
        "full_tags": [
          {
            "id": 3412727,
            "name": "Engineering",
            "color": "#e09052"
          },
          {
            "id": 775582684,
            "name": "Infrastructure",
            "color": "#7552e0"
          }
        ],
        "custom_fields": [
          {
            "id": 1051489895,
            "key": "equation_specs_field",
            "name": "Equation specs field",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": {
              "values": {
                "123": {
                  "value": 10,
                  "name": "a",
                  "display_value": "10.0"
                },
                "456": {
                  "value": "Foobar",
                  "name": "b",
                  "display_value": "Foobar"
                },
                "789": {
                  "value": null,
                  "name": "789",
                  "display_value": null
                }
              }
            },
            "type": "equation_sheet"
          },
          {
            "id": 621325984,
            "key": "expected_completion_date",
            "name": "Expected completion date",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": "2019-01-01",
            "type": "date"
          },
          {
            "id": 694694494,
            "key": "negative_scorecard",
            "name": "Negative custom scorecard",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": 31,
            "type": "scorecard",
            "score_facts": [
              {
                "id": "462102328",
                "value": 6,
                "name": "Negative default value"
              }
            ]
          },
          {
            "id": 736691743,
            "key": "upload",
            "name": "Upload",
            "updatedAt": "2019-01-01T00:00:00Z",
            "attachments": [
              {
                "id": "471688235",
                "download_url": "https://company.aha.io/attachments/471688235/token/aaabbbccc7.download?size=original",
                "created_at": "2019-01-01T00:00:00.000Z",
                "updated_at": "2019-01-01T00:00:00.000Z",
                "original_file_size": 123,
                "content_type": "text/plain",
                "file_name": "uploaded_file_name.txt",
                "file_size": 123
              }
            ],
            "type": "attachment"
          }
        ],
        "feature_links": [
          {
            "link_type": "Depends on",
            "link_type_id": 20,
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
              "id": "622562724",
              "reference_num": "PRJ1-2",
              "name": "Another Feature",
              "created_at": "2019-01-01T00:00:00.000Z",
              "url": "http://company.aha.io/features/PRJ1-2",
              "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
              "product_id": "131414752"
            }
          }
        ],
        "feature_only_original_estimate": null,
        "feature_only_remaining_estimate": null,
        "feature_only_work_done": null
      }
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

## List epics with an associated integration field value

**GET** `/api/v1/epics/fields/:field_name/value/:field_value`

### Parameters
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List requirements with an associated integration field value

**GET** `/api/v1/requirements/fields/:field_name/value/:field_value`

### Parameters
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/requirements/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List idea votes with an associated integration field value

**GET** `/api/v1/idea_endorsements/fields/:field_name/value/:field_value`

### Parameters
- `field_name` () - **Required** - Name of the integration field
- `field_value` () - **Required** - Value that matching records must have in the integration field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_endorsements/fields/key/value/JRA-123" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "records": [
    {
      "idea_endorsement": {
        "integration_id": 204584239,
        "service_name": "jira",
        "id": "53377392",
        "idea_id": "58056975",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "value": null,
        "link": null,
        "weight": 1,
        "endorsed_by_portal_user": {
          "id": "646391926",
          "name": "John Long",
          "email": "john@long.com",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        "endorsed_by_idea_user": {
          "id": "1056507375",
          "name": "John Long",
          "email": "john@long.com",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        "idea_organization": {
          "id": "138732915",
          "name": "Acme",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/ideas/idea_organizations/138732915",
          "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
        },
        "description": {
          "id": "6776757454439265148",
          "body": "",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "integration_fields": [
          {
            "id": "975466318",
            "name": "key",
            "value": "JRA-123",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "custom_fields": [],
        "idea": {
          "id": "58056975",
          "reference_num": "PRJ1-I-1",
          "name": "Idea 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "workflow_status": {
            "id": "3259216",
            "name": "New",
            "position": 1,
            "complete": false,
            "color": "#dce7c6"
          },
          "description": {
            "id": "103757394",
            "body": "Description of idea 1",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          },
          "url": "http://company.aha.io/ideas/ideas/PRJ1-I-1",
          "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-1"
        }
      }
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

## Delete an integration field

**DELETE** `/api/v1/integration_fields/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the integration field

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/integration_fields/728894778" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
