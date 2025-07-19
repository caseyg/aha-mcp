# Audits

## Retrieve record history

**GET** `/api/v1/audits`

### Description
Audit records describe historical changes to records in Aha! and are created automatically when a record is created, updated, or deleted. Audits are immutable and cannot be modified or deleted.

Audits are stored not only for first-class objects such as Features or Release, but also for secondary objects attached to those records such as custom field values, equation field values, descriptions, and record links.

Audit records are only available for the last 12 calendar months. After that, they must be accessed using the [Historical Audits](/api/resources/historical_audits/create_an_audit_search/) endpoint.

The performance of the Audits API can be improved by judicious use of the `created_since` and `created_before` parameters. Since this is high-volume timeseries data, these parameters should be used when attempting to scan through record activity, and the `after_id` parameter should be used in lieu of pagination.


### Parameters
- `auditable_id` () - Optional - Numeric ID of the record for which history should be retrieved
- `auditable_type` () - Optional - String identifier of the type of record for which history should be retrieved
- `associated_id` () - Optional - Numeric ID of the primary record for which history should be retrieved. This value is required if :associated_type is also provided. Use these parameters to fetch only the history for secondary records, like descriptions and custom field values.
- `associated_type` () - Optional - String identifier of the type of the primary record for which history should be retrieved
- `audit_action` () - Optional - Type of action. Options are 'create', 'update', and 'destroy'
- `created_since` () - Optional - ISO8601 timestamp determining the beginning of the search range for historical changes
- `created_before` () - Optional - ISO8601 timestamp determining the end of the search window for historical changes
- `after_id` () - Optional - Numeric identifier which filters result record to only records with ID larger than the parameter. This can be used for cursor-based searches, and is more efficient than pagination for large data sets.
- `user_id` () - Optional - Numeric user ID, which searches only for audit records where one particular user was the actor

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/audits?auditable_id=1007868956&auditable_type=Feature" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "audits": [
    {
      "id": "6776757454428206157",
      "audit_action": "update",
      "created_at": "2019-01-01T00:00:00.000Z",
      "interesting": true,
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "contributors": [
        {
          "user": {
            "id": "1049303076",
            "name": "George Gently",
            "email": "no-reply@aha.io",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z"
          }
        }
      ],
      "auditable_type": "note",
      "auditable_id": 793547626,
      "associated_type": "feature",
      "associated_id": 1007868956,
      "description": "updated feature PRJ1-1 Changed feature name",
      "auditable_url": "https://company.aha.io:8338/features/PRJ1-1",
      "changes": [
        {
          "field_name": "Description",
          "value": "<div class=\"user-content\"><span class=\"deleted\">Body of note 1</span><span class=\"inserted\">Changed description</span></div>"
        }
      ]
    },
    {
      "id": "6776757454436663266",
      "audit_action": "update",
      "created_at": "2019-01-01T00:00:00.000Z",
      "interesting": true,
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "contributors": [
        {
          "user": {
            "id": "1049303076",
            "name": "George Gently",
            "email": "no-reply@aha.io",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z"
          }
        }
      ],
      "auditable_type": "feature",
      "auditable_id": 1007868956,
      "associated_type": "release",
      "associated_id": 278327321,
      "description": "updated feature PRJ1-1 Changed feature name",
      "auditable_url": "https://company.aha.io:8338/features/PRJ1-1",
      "changes": [
        {
          "field_name": "Name",
          "value": "Feature 1 &rarr; Changed feature name"
        }
      ]
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

## Retrieve the history of only the description of a record

**GET** `/api/v1/audits`

### Description
Audit records describe historical changes to records in Aha! and are created automatically when a record is created, updated, or deleted. Audits are immutable and cannot be modified or deleted.

Audits are stored not only for first-class objects such as Features or Release, but also for secondary objects attached to those records such as custom field values, equation field values, descriptions, and record links.

Audit records are only available for the last 12 calendar months. After that, they must be accessed using the [Historical Audits](/api/resources/historical_audits/create_an_audit_search/) endpoint.

The performance of the Audits API can be improved by judicious use of the `created_since` and `created_before` parameters. Since this is high-volume timeseries data, these parameters should be used when attempting to scan through record activity, and the `after_id` parameter should be used in lieu of pagination.


### Parameters
- `auditable_id` () - Optional - Numeric ID of the record for which history should be retrieved
- `auditable_type` () - Optional - String identifier of the type of record for which history should be retrieved
- `associated_id` () - Optional - Numeric ID of the primary record for which history should be retrieved. This value is required if :associated_type is also provided. Use these parameters to fetch only the history for secondary records, like descriptions and custom field values.
- `associated_type` () - Optional - String identifier of the type of the primary record for which history should be retrieved
- `audit_action` () - Optional - Type of action. Options are 'create', 'update', and 'destroy'
- `created_since` () - Optional - ISO8601 timestamp determining the beginning of the search range for historical changes
- `created_before` () - Optional - ISO8601 timestamp determining the end of the search window for historical changes
- `after_id` () - Optional - Numeric identifier which filters result record to only records with ID larger than the parameter. This can be used for cursor-based searches, and is more efficient than pagination for large data sets.
- `user_id` () - Optional - Numeric user ID, which searches only for audit records where one particular user was the actor

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/audits?associated_id=1007868956&associated_type=Feature&auditable_type=Note" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "audits": [
    {
      "id": "6776757454435854279",
      "audit_action": "update",
      "created_at": "2019-01-01T00:00:00.000Z",
      "interesting": true,
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "contributors": [
        {
          "user": {
            "id": "1049303076",
            "name": "George Gently",
            "email": "no-reply@aha.io",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z"
          }
        }
      ],
      "auditable_type": "note",
      "auditable_id": 793547626,
      "associated_type": "feature",
      "associated_id": 1007868956,
      "description": "updated feature PRJ1-1 Changed feature name",
      "auditable_url": "https://company.aha.io:8338/features/PRJ1-1",
      "changes": [
        {
          "field_name": "Description",
          "value": "<div class=\"user-content\"><span class=\"deleted\">Body of note 1</span><span class=\"inserted\">Changed description</span></div>"
        }
      ]
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
