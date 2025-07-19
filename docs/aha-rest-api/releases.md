# Releases

## Create a release

**POST** `/api/v1/products/:product_id/releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases" -d '{"release":{"owner":"no-reply@aha.io","initiatives":"Initiative 1","name":"Release 3","status":"New","theme":"Our first big release","external_date_resolution":"month"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "6776757454440696808",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-5",
    "name": "Release 3",
    "start_date": null,
    "end_date": null,
    "development_started_on": null,
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "February FY25",
    "external_date_resolution": "month",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": 1,
    "progress": 0,
    "progress_source": "progress_from_features_completed",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
    "theme": {
      "id": "6776757454436246773",
      "body": "Our first big release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-5",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-5",
    "integration_fields": [],
    "custom_fields": [],
    "comments_count": 0,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "goals": [],
    "key_results": [],
    "initiatives": [
      {
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
      }
    ],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status_times": [
      {
        "status_id": "738862546",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Create a parking lot release

**POST** `/api/v1/products/:product_id/releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases" -d '{"release":{"owner":"no-reply@aha.io","initiatives":[],"name":"Release 3","status":"New","theme":"Our first big release","external_date_resolution":"week","parking_lot":true}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "6776757454427254871",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-5",
    "name": "Release 3",
    "released": false,
    "parking_lot": true,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": 1,
    "progress": 0,
    "progress_source": "progress_from_features_completed",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
    "theme": {
      "id": "6776757454434654022",
      "body": "Our first big release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-5",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-5",
    "integration_fields": [],
    "custom_fields": [],
    "comments_count": 0,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "goals": [],
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status_times": [
      {
        "status_id": "738862546",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Create a release with watchers

**POST** `/api/v1/products/:product_id/releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases" -d '{"release":{"owner":"no-reply@aha.io","initiatives":[],"name":"Release 3","watchers":"689956296,16338845"},"fields":"*,watchers"}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "6776757454432279496",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-5",
    "name": "Release 3",
    "start_date": null,
    "end_date": null,
    "development_started_on": null,
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 28, 2025",
    "external_date_resolution": "sync",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": 1,
    "progress": 0,
    "progress_source": "progress_from_features_completed",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
    "theme": {
      "id": "6776757454430318369",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-5",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-5",
    "integration_fields": [],
    "custom_fields": [],
    "comments_count": 0,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "goals": [],
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status_times": [
      {
        "status_id": "738862546",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "watchers": [
      {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    ]
  }
}
```

---

## Create a release with goals

**POST** `/api/v1/products/:product_id/releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases" -d '{"release":{"owner":"no-reply@aha.io","initiatives":[],"name":"Release 3","goals":"602095703,988418543"},"fields":"*,goals"}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "6776757454433000588",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-5",
    "name": "Release 3",
    "start_date": null,
    "end_date": null,
    "development_started_on": null,
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 28, 2025",
    "external_date_resolution": "sync",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": 1,
    "progress": 0,
    "progress_source": "progress_from_features_completed",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
    "theme": {
      "id": "6776757454435770968",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-5",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-5",
    "integration_fields": [],
    "custom_fields": [],
    "comments_count": 0,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
      },
      {
        "id": "988418543",
        "name": "Goal 2",
        "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-2",
        "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "1055602421",
          "body": "Description of goal 2",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      }
    ],
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status_times": [
      {
        "status_id": "738862546",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Create a release with initiatives

**POST** `/api/v1/products/:product_id/releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases" -d '{"release":{"owner":"no-reply@aha.io","initiatives":"423077122,4125886","name":"Release 3"},"fields":"*,initiatives"}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "6776757454437639323",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-5",
    "name": "Release 3",
    "start_date": null,
    "end_date": null,
    "development_started_on": null,
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 28, 2025",
    "external_date_resolution": "sync",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": 1,
    "progress": 0,
    "progress_source": "progress_from_features_completed",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
    "theme": {
      "id": "6776757454439279115",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-5",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-5",
    "integration_fields": [],
    "custom_fields": [],
    "comments_count": 0,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "goals": [],
    "key_results": [],
    "initiatives": [
      {
        "id": "4125886",
        "reference_num": "PRJ1-S-2",
        "name": "Initiative 2",
        "url": "http://company.aha.io/initiatives/PRJ1-S-2",
        "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "824706757",
          "body": "Description of initiative 2",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "integration_fields": []
      },
      {
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
      }
    ],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status_times": [
      {
        "status_id": "738862546",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## List releases in a product

**GET** `/api/v1/products/:product_id/releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against release name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only releases updated after the timestamp will be returned.
- `parking_lot` () - Optional - When true, only parking lot releases will be returned.
- `exclude_shipped` () - Optional - When true, shipped releases will be excluded. By default, all releases will be returned regardless of shipped status.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/releases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "releases": [
    {
      "id": "141021264",
      "reference_num": "PRJ1-MR-2",
      "name": "Roll-up Release 2",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/master_releases/PRJ1-MR-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-2",
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
    {
      "id": "161456549",
      "reference_num": "PRJ1-R-2",
      "name": "Release 2",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ1-R-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-2",
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
    {
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
    {
      "id": "292454904",
      "reference_num": "PRJ1-MR-1",
      "name": "Roll-up Release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/master_releases/PRJ1-MR-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-1",
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
    {
      "id": "325518644",
      "reference_num": "PRJ1-R-4",
      "name": "Sub release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ1-R-4",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-4",
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
      },
      "parent": {
        "id": "141021264",
        "reference_num": "PRJ1-MR-2",
        "name": "Roll-up Release 2",
        "start_date": "2019-01-01",
        "release_date": "2019-01-01",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/master_releases/PRJ1-MR-2",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-2"
      }
    },
    {
      "id": "1050186040",
      "reference_num": "PRJ1-R-3",
      "name": "Release 3",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [
        {
          "id": "453734818",
          "name": "id",
          "value": "4221",
          "integration_id": 342659513,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "url": "http://company.aha.io/releases/PRJ1-R-3",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-3",
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
    }
  ],
  "pagination": {
    "total_records": 6,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List releases associated with a goal

**GET** `/api/v1/goals/:goal_id/releases`

### Parameters
- `goal_id` () - **Required** - Numeric ID of the goal
- `q` () - Optional - Search term to match against release name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only releases updated after the timestamp will be returned.
- `parking_lot` () - Optional - When true, only parking lot releases will be returned.
- `exclude_shipped` () - Optional - When true, shipped releases will be excluded. By default, all releases will be returned regardless of shipped status.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/602095703/releases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "releases": [
    {
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

## List releases associated with an initiative

**GET** `/api/v1/initiatives/:initiative_id/releases`

### Parameters
- `initiative_id` () - **Required** - Numeric ID of the initiative to get releases for
- `q` () - Optional - Search term to match against release name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only releases updated after the timestamp will be returned.
- `parking_lot` () - Optional - When true, only parking lot releases will be returned.
- `exclude_shipped` () - Optional - When true, shipped releases will be excluded. By default, all releases will be returned regardless of shipped status.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/423077122/releases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "releases": [
    {
      "id": "161456549",
      "reference_num": "PRJ1-R-2",
      "name": "Release 2",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ1-R-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-2",
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
    {
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

## List releases under a roll-up release

**GET** `/api/v1/releases/:release_id/releases`

### Parameters
- `release_id` () - **Required** - Numeric ID of the roll-up release to get releases for
- `q` () - Optional - Search term to match against release name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only releases updated after the timestamp will be returned.
- `parking_lot` () - Optional - When true, only parking lot releases will be returned.
- `exclude_shipped` () - Optional - When true, shipped releases will be excluded. By default, all releases will be returned regardless of shipped status.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/141021264/releases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "releases": [
    {
      "id": "325518644",
      "reference_num": "PRJ1-R-4",
      "name": "Sub release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ1-R-4",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-4",
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
      },
      "parent": {
        "id": "141021264",
        "reference_num": "PRJ1-MR-2",
        "name": "Roll-up Release 2",
        "start_date": "2019-01-01",
        "release_date": "2019-01-01",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/master_releases/PRJ1-MR-2",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-2"
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

## List releases under a roll-up release

**GET** `/api/v1/roll_up_releases/:release_id/releases`

### Parameters
- `release_id` () - **Required** - Numeric ID of the roll-up release to get releases for
- `q` () - Optional - Search term to match against release name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only releases updated after the timestamp will be returned.
- `parking_lot` () - Optional - When true, only parking lot releases will be returned.
- `exclude_shipped` () - Optional - When true, shipped releases will be excluded. By default, all releases will be returned regardless of shipped status.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/roll_up_releases/141021264/releases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "releases": [
    {
      "id": "85510963",
      "reference_num": "PRJ4-R-4",
      "name": "Parking lot for Project 4",
      "parking_lot": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "935317104",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ4-R-4",
      "resource": "http://company.aha.io/api/v1/releases/PRJ4-R-4",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "935317104",
        "reference_prefix": "PRJ4",
        "name": "Project 4",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ4"
      }
    },
    {
      "id": "141021264",
      "reference_num": "PRJ1-MR-2",
      "name": "Roll-up Release 2",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/master_releases/PRJ1-MR-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-2",
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
    {
      "id": "161456549",
      "reference_num": "PRJ1-R-2",
      "name": "Release 2",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ1-R-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-2",
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
    {
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
    {
      "id": "292454904",
      "reference_num": "PRJ1-MR-1",
      "name": "Roll-up Release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/master_releases/PRJ1-MR-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-1",
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
    {
      "id": "325518644",
      "reference_num": "PRJ1-R-4",
      "name": "Sub release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ1-R-4",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-4",
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
      },
      "parent": {
        "id": "141021264",
        "reference_num": "PRJ1-MR-2",
        "name": "Roll-up Release 2",
        "start_date": "2019-01-01",
        "release_date": "2019-01-01",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/master_releases/PRJ1-MR-2",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-2"
      }
    },
    {
      "id": "342040612",
      "reference_num": "PRJ3-R-1",
      "name": "Release 3 Project 3",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "702241743",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ3-R-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ3-R-1",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "702241743",
        "reference_prefix": "PRJ3",
        "name": "Project 3",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ3"
      }
    },
    {
      "id": "414276209",
      "reference_num": "PRJ4-R-3",
      "name": "Release month old (shipped)",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "935317104",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ4-R-3",
      "resource": "http://company.aha.io/api/v1/releases/PRJ4-R-3",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "935317104",
        "reference_prefix": "PRJ4",
        "name": "Project 4",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ4"
      }
    },
    {
      "id": "637342960",
      "reference_num": "PRJ2-R-2",
      "name": "Parking lot for Project 2",
      "parking_lot": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "517761884",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ2-R-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ2-R-2",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
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
      "id": "800484072",
      "reference_num": "PRJ4-R-2",
      "name": "Release week old (shipped)",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "935317104",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ4-R-2",
      "resource": "http://company.aha.io/api/v1/releases/PRJ4-R-2",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "935317104",
        "reference_prefix": "PRJ4",
        "name": "Project 4",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ4"
      }
    },
    {
      "id": "918502240",
      "reference_num": "PRJ4-R-1",
      "name": "Release 4",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "935317104",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ4-R-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ4-R-1",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "935317104",
        "reference_prefix": "PRJ4",
        "name": "Project 4",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ4"
      }
    },
    {
      "id": "946589036",
      "reference_num": "PRJe-R-4",
      "name": "Parking lot",
      "parking_lot": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "702241743",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJe-R-4",
      "resource": "http://company.aha.io/api/v1/releases/PRJe-R-4",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "702241743",
        "reference_prefix": "PRJ3",
        "name": "Project 3",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ3"
      }
    },
    {
      "id": "1000426269",
      "reference_num": "PRJ2-R-1",
      "name": "Release 2",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "517761884",
      "integration_fields": [],
      "url": "http://company.aha.io/releases/PRJ2-R-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ2-R-1",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
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
      "id": "1050186040",
      "reference_num": "PRJ1-R-3",
      "name": "Release 3",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [
        {
          "id": "453734818",
          "name": "id",
          "value": "4221",
          "integration_id": 342659513,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "url": "http://company.aha.io/releases/PRJ1-R-3",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-3",
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
    }
  ],
  "pagination": {
    "total_records": 14,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific release

**GET** `/api/v1/releases/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/PRJ1-R-1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": "2019-01-01",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "initiatives": [
      {
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
      }
    ],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Duplicate a release

**POST** `/api/v1/releases/:id/duplicate`

### Parameters
- `id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/duplicate" -d '' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "6776757454433986171",
    "name": "[Copy] Release 1"
  }
}
```

---

## Update a release

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[],"name":"Smarter release"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Smarter release",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Update a release's initiatives

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[4125886]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "initiatives": [
      {
        "id": "4125886",
        "reference_num": "PRJ1-S-2",
        "name": "Initiative 2",
        "url": "http://company.aha.io/initiatives/PRJ1-S-2",
        "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "824706757",
          "body": "Description of initiative 2",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "integration_fields": []
      }
    ],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Update a release's watchers

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[],"watchers":[689956296]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Update a release's goals

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[],"goals":[602095703]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Update a release's progress source

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[],"progress_source":"progress_from_features"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": 0,
    "progress_source": "progress_from_features",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Update a release's progress

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[],"progress":25}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": 25,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Add a release to a roll up release

**PUT** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release
- `name` () - Optional - Name of the release
- `owner` () - Optional - Email or ID of the user that will own this release
- `initiatives` () - Optional - Array of names or ids of initiatives which this release is associated with.
- `workflow_status` () - Optional - Status of the release — must be a valid status for the selected product.
- `parent_id` () - Optional - Numeric ID of the roll-up release of the release if present
- `theme` () - Optional - Theme of the release — may include HTML formatting.
- `start_date` () - Optional - Start date of the release in format YYYY-MM-DD
- `end_date` () - Optional - End date of the release in format YYYY-MM-DD
- `release_date` () - Optional - Release date of the release in format YYYY-MM-DD
- `development_started_on` () - Optional - Date development started in format YYYY-MM-DD
- `parking_lot` () - Optional - Sets whether this release is a parking lot. Use true to represent a parking lot release
- `external_release_date` () - Optional - The external release date for this release in format YYYY-MM-DD
- `external_date_resolution` () - Optional - Rounds the external release date to the nearest resolution value. This must be specified along with an external release date and must be one of: sync, exact, week, month, quarter, half, year
- `capacity_units` () - Optional - The units for this release — must be either "time" or "story_points".
- `total_capacity_text` () - Optional - The total capacity in time or story points for this release, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `progress_source` () - Optional - Source for calculating progress on the release. Options are: progress_manual, progress_from_features, progress_from_release_phases, progress_from_todos, progress_from_remaining_estimate, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the release — may only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_release_phases_features, duration_from_sub_releases.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/278327321" -d '{"release":{"initiatives":[],"parent_id":292454904}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
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
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
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
    "key_results": [],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "parent": {
      "id": "292454904",
      "reference_num": "PRJ1-MR-1",
      "name": "Roll-up Release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/master_releases/PRJ1-MR-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Delete a release

**DELETE** `/api/v1/products/:product_id/releases/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/releases/161456549" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
