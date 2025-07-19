# Features

## Create a feature

**POST** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -d '{"feature":{"name":"New name","workflow_kind":"new","workflow_status":{"name":"Designed"},"description":"\u003cp\u003eThis is the description\u003c/p\u003e","assigned_to_user":{"email":"no-reply@aha.io"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454426194661",
    "name": "New name",
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
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
      "id": "6776757454428226645",
      "body": "<p>This is the description</p>",
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
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "requirements": [],
    "goals": [],
    "key_results": [],
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "feature_links": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
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

## Create a feature with an assignee

**POST** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -d '{"feature":{"name":"New feature","workflow_kind":"new","workflow_status":{"name":"Designed"},"assigned_to_user":"no-reply@aha.io"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454433077587",
    "name": "New feature",
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
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
      "id": "6776757454437052878",
      "body": "",
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
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "requirements": [],
    "goals": [],
    "key_results": [],
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "feature_links": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
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

## Create a feature with tags

**POST** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -d '{"feature":{"name":"New feature","workflow_kind":"new","workflow_status":{"name":"Designed"},"tags":"tag1, tag2"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454434468014",
    "name": "New feature",
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
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
      "id": "6776757454439903095",
      "body": "",
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
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": true
    },
    "requirements": [],
    "goals": [],
    "key_results": [],
    "comments_count": 0,
    "score_facts": [],
    "tags": [
      "tag1",
      "tag2"
    ],
    "full_tags": [
      {
        "id": "6776757454428864050",
        "name": "tag2",
        "color": "#52d3e0"
      },
      {
        "id": "6776757454431745052",
        "name": "tag1",
        "color": "#52e077"
      }
    ],
    "custom_fields": [],
    "feature_links": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
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

## Create a feature with watchers

**POST** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -d '{"fields":"*,watchers","feature":{"name":"New feature","workflow_kind":"new","workflow_status":{"name":"Designed"},"watchers":"689956296,16338845"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454440958043",
    "name": "New feature",
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
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
      "id": "6776757454431754259",
      "body": "",
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
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": true
    },
    "requirements": [],
    "goals": [],
    "key_results": [],
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "feature_links": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "feature_only_original_estimate": null,
    "feature_only_remaining_estimate": null,
    "feature_only_work_done": null,
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

## Create a feature with goals

**POST** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -d '{"fields":"*,goals","feature":{"name":"New feature","workflow_kind":"new","workflow_status":{"name":"Designed"},"goals":"602095703,988418543"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454426902278",
    "name": "New feature",
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
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
      "id": "6776757454436213613",
      "body": "",
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
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": true
    },
    "requirements": [],
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
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "feature_links": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
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

## Create a feature with a score

**POST** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -d '{"feature":{"name":"New feature","workflow_kind":"new","workflow_status":{"name":"Designed"},"score_facts":[{"name":"Benefit","value":10},{"name":"Effort","value":3}]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "6776757454438730193",
    "name": "New feature",
    "reference_num": "PRJ1-251",
    "initiative_reference_num": null,
    "release_reference_num": "PRJ1-R-1",
    "epic_reference_num": null,
    "position": 1,
    "score": 13,
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
      "id": "962984386",
      "name": "Designed",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
      "id": "6776757454436000744",
      "body": "",
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
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": true
    },
    "requirements": [],
    "goals": [],
    "key_results": [],
    "comments_count": 0,
    "score_facts": [
      {
        "id": "6776757454426554593",
        "value": 3,
        "name": "Effort"
      },
      {
        "id": "6776757454431948385",
        "value": 10,
        "name": "Benefit"
      }
    ],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "feature_links": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
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

## List features

**GET** `/api/v1/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `q` () - Optional - Search term to match against feature name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only features updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only features with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only features assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "features": [
    {
      "id": "101074039",
      "reference_num": "PRJ2-1",
      "name": "A feature in project 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ2-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ2-1",
      "product_id": "517761884"
    },
    {
      "id": "209201304",
      "reference_num": "PRJ1-4",
      "name": "Another Fourth Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-4",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-4",
      "product_id": "131414752"
    },
    {
      "id": "229579240",
      "reference_num": "PRJ3-1",
      "name": "Feature without Requirements",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ3-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ3-1",
      "product_id": "702241743"
    },
    {
      "id": "303873333",
      "reference_num": "PRJ1-3",
      "name": "Another Third Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-3",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-3",
      "product_id": "131414752"
    },
    {
      "id": "622562724",
      "reference_num": "PRJ1-2",
      "name": "Another Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-2",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
      "product_id": "131414752"
    },
    {
      "id": "959120953",
      "reference_num": "PRJ3-2",
      "name": "A third Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ3-2",
      "resource": "http://company.aha.io/api/v1/features/PRJ3-2",
      "product_id": "702241743"
    },
    {
      "id": "998184963",
      "reference_num": "PRJ1-5",
      "name": "Another Fifth Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-5",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-5",
      "product_id": "131414752"
    },
    {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    }
  ],
  "pagination": {
    "total_records": 8,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List features in an epic

**GET** `/api/v1/epics/:epic_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the epic
- `q` () - Optional - Search term to match against feature name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only features updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only features with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only features assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics/PRJ1-E-1/features" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "features": [
    {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
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

## List features in a release

**GET** `/api/v1/releases/:release_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `q` () - Optional - Search term to match against feature name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only features updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only features with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only features assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/PRJ1-R-1/features" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "features": [
    {
      "id": "209201304",
      "reference_num": "PRJ1-4",
      "name": "Another Fourth Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-4",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-4",
      "product_id": "131414752"
    },
    {
      "id": "303873333",
      "reference_num": "PRJ1-3",
      "name": "Another Third Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-3",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-3",
      "product_id": "131414752"
    },
    {
      "id": "622562724",
      "reference_num": "PRJ1-2",
      "name": "Another Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-2",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
      "product_id": "131414752"
    },
    {
      "id": "998184963",
      "reference_num": "PRJ1-5",
      "name": "Another Fifth Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-5",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-5",
      "product_id": "131414752"
    },
    {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    }
  ],
  "pagination": {
    "total_records": 5,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List features in a product

**GET** `/api/v1/products/:product_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against feature name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only features updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only features with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only features assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/features" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "features": [
    {
      "id": "209201304",
      "reference_num": "PRJ1-4",
      "name": "Another Fourth Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-4",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-4",
      "product_id": "131414752"
    },
    {
      "id": "303873333",
      "reference_num": "PRJ1-3",
      "name": "Another Third Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-3",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-3",
      "product_id": "131414752"
    },
    {
      "id": "622562724",
      "reference_num": "PRJ1-2",
      "name": "Another Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-2",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
      "product_id": "131414752"
    },
    {
      "id": "998184963",
      "reference_num": "PRJ1-5",
      "name": "Another Fifth Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-5",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-5",
      "product_id": "131414752"
    },
    {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    }
  ],
  "pagination": {
    "total_records": 5,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List features associated with a goal

**GET** `/api/v1/goals/:goal_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `goal_id` () - **Required** - Numeric ID of the goal
- `q` () - Optional - Search term to match against feature name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only features updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only features with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only features assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/602095703/features" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "features": [
    {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
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

## List features associated with an initiative

**GET** `/api/v1/initiatives/:initiative_id/features`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `initiative_id` () - **Required** - Numeric ID of the initiative
- `q` () - Optional - Search term to match against feature name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only features updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only features with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only features assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/423077122/features" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "features": [
    {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
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

## Get a specific feature

**GET** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/PRJ1-1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454429178725",
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
          "id": "6776757454427092506",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Update a feature

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"name":"New name","description":"New description"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "1007868956",
    "name": "New name",
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
      "body": "New description",
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
          "id": "6776757454432854833",
          "body": "",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "feature": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "New name",
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
          "name": "New name",
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
          "id": "6776757454439619655",
          "body": "",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "feature": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "New name",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
          "name": "New name",
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
```

---

## Update a feature's custom fields

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"custom_fields":{"priority":"P3"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454441676553",
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
          "id": "6776757454432084573",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
        "id": "6776757454438660320",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
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
```

---

## Update a feature's custom fields with tag-like value

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"custom_fields":{"tags":["tag2","tag,3"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454438850529",
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
          "id": "6776757454428946155",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
        "id": "6776757454439325694",
        "key": "tags",
        "name": "Custom field items",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": [
          "tag2",
          "tag,3"
        ],
        "type": "array"
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
```

---

## Update a feature's custom worksheet fields

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"custom_fields":{"equation_custom_field":{"6651670327076753738":777.0,"6651670366942086967":432.0}}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454432214854",
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
          "id": "6776757454430230748",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
        "id": "6776757454425816373",
        "key": "equation_custom_field",
        "name": "Equation custom field",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "6651670327076753738": {
              "value": 777,
              "name": "Revenue",
              "display_value": "$777.00"
            },
            "6651670366942086967": {
              "value": 432,
              "name": "Expenses",
              "display_value": "$432.00"
            },
            "6651670393424268679": {
              "value": 345,
              "name": "Profit",
              "display_value": "$345.00"
            }
          }
        },
        "type": "equation_sheet"
      },
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
```

---

## Update a feature's tags with comma-separated values

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"tags":"tag2, tag3"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454428858890",
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
          "id": "6776757454427638125",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
      "tag2",
      "tag3"
    ],
    "full_tags": [
      {
        "id": "6776757454435763182",
        "name": "tag3",
        "color": "#bb52e0"
      },
      {
        "id": "6776757454436520885",
        "name": "tag2",
        "color": "#52d3e0"
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
```

---

## Update a feature's tags with an array

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"tags":["tag2","tag3"]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454426524088",
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
          "id": "6776757454427616132",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
      "tag2",
      "tag3"
    ],
    "full_tags": [
      {
        "id": "6776757454425509383",
        "name": "tag3",
        "color": "#bb52e0"
      },
      {
        "id": "6776757454429614112",
        "name": "tag2",
        "color": "#52d3e0"
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
```

---

## Update a feature's watchers

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"watchers":[689956296]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454441034188",
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
          "id": "6776757454433962325",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Update a feature's goals

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"goals":[602095703]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454428981840",
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
          "id": "6776757454429638084",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Update a feature's score

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"score_facts":[{"name":"Benefit","value":4},{"name":"Effort","value":5}]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "1007868956",
    "name": "Feature 1",
    "reference_num": "PRJ1-1",
    "initiative_reference_num": "PRJ1-S-1",
    "release_reference_num": "PRJ1-R-1",
    "epic_reference_num": "PRJ1-E-1",
    "position": 1,
    "score": 9,
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
          "id": "6776757454434883798",
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
          "id": "6776757454432116596",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
      }
    ],
    "comments_count": 1,
    "score_facts": [
      {
        "id": "728895917",
        "value": 5,
        "name": "Effort"
      },
      {
        "id": "846938137",
        "value": 4,
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
```

---

## Update a feature's epic

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"epic":"PRJ1-E-1"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
          "id": "6776757454441809536",
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
          "id": "6776757454425454575",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Update a feature's release

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"release":"PRJ1-R-2"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "1007868956",
    "name": "Feature 1",
    "reference_num": "PRJ1-1",
    "initiative_reference_num": "PRJ1-S-1",
    "release_reference_num": "PRJ1-R-2",
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
        "release_id": 161456549,
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
          "id": "6776757454436372509",
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
        "release_id": 161456549,
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
        "release_id": 161456549,
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
          "id": "6776757454431671342",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Update a feature's progress source

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"progress_source":"progress_from_requirements"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
    "progress": 33,
    "progress_source": "progress_from_requirements",
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
          "id": "6776757454432429187",
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
          "id": "6776757454436096429",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Update a feature's progress

**PUT** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `name` () - Optional - Name of the feature
- `workflow_kind` () - Optional - Type of feature
- `workflow_status` () - Optional - Status of the feature — must be a valid status for the selected product.
- `release` () - Optional - Numeric ID or key of the release the feature should be created in.
- `description` () - Optional - Description of the feature — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the feature.
- `assigned_to_user` () - Optional - Email address of user that is assigned the feature.
- `tags` () - Optional - Tags to add to the feature. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this feature, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the feature in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the feature in format YYYY-MM-DD
- `release_phase` () - Optional - Name or id of release phase which the feature belongs to
- `initiative` () - Optional - Name or id of initiative which the feature belongs to
- `epic` () - Optional - Name or id of epic which the feature belongs to
- `progress_source` () - Optional - Source for calculating progress on the feature. Options are: progress_manual, progress_from_requirements, progress_from_remaining_estimate, progress_from_todos.
- `progress` () - Optional - Progress completed on the feature. May only be set when the progress_source is manual.
- `team` () - Optional - Numeric ID or key of the team to assign the feature to.
- `team_workflow_status` () - Optional - Team status of the feature — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the feature to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the feature to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"progress":25}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
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
    "progress": 25,
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
          "id": "6776757454426014205",
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
          "id": "6776757454432511226",
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
    "key_results": [
      {
        "id": "631791848",
        "name": "KR 1",
        "reference_num": "DEMOENT-G-1-KR-1",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-1",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": "100%",
        "starting_metric": "5%",
        "current_metric": "20%"
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
```

---

## Delete a feature

**DELETE** `/api/v1/features/:id`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Convert a feature to an epic

**POST** `/api/v1/features/:id/convert_to_epic`

### Description
Features belong to releases.
This means that if you want to
[create one](/api/resources/features/create_a_feature) then
you must scope it to a release.

You can return a result set which is unfiltered, or filter by
[release](/api/resources/features/list_features_in_a_release)
, [product](/api/resources/features/list_features_in_a_product)
, or [epic](/api/resources/features/list_features_in_an_epic).
All these means of listing features can be further filtered by specific criteria like name, modification date, tag, or assignee.

Once you have the id of a specific feature, you can
[inspect](/api/resources/features/get_a_specific_feature),
[modify](/api/resources/features/update_a_feature),
or
[delete](/api/resources/features/delete_a_feature)
them on the root features resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ2-1/convert_to_epic" -d '' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "": {
    "id": "6776757454425734692",
    "name": "A feature in project 2",
    "reference_num": "PRJ2-E-251",
    "initiative_reference_num": null,
    "position": 1000,
    "score": 0,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "517761884",
    "progress": 0,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
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
    "project": {
      "id": "517761884",
      "reference_prefix": "PRJ2",
      "name": "Project 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ2"
    },
    "description": {
      "id": "6776757454429457454",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/epics/PRJ2-E-251",
    "resource": "http://company.aha.io/api/v1/epics/PRJ2-E-251",
    "release": {
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
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "features": [],
    "goals": [],
    "key_results": [],
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "_links": [],
    "master_feature_only_original_estimate": null,
    "master_feature_only_remaining_estimate": null,
    "master_feature_only_work_done": null,
    "epic_only_original_estimate": null,
    "epic_only_remaining_estimate": null,
    "epic_only_work_done": null
  }
}
```

---
