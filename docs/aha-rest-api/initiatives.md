# Initiatives

## Create an initiative

**POST** `/api/v1/products/:product_id/initiatives`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the initiative
- `workflow_status` () - **Required** - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives" -d '{"initiative":{"name":"Initiative 3","workflow_status":{"name":"Not Started"},"description":"Our first big initiative","time_frame":{"id":813624702},"effort":15,"value":5,"presented":true}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "6776757454433322781",
    "name": "Initiative 3",
    "reference_num": "PRJ1-S-251",
    "status": "not_started",
    "effort": 15,
    "value": 5,
    "presented": true,
    "color": "#397e82",
    "start_date": null,
    "end_date": null,
    "position": 3,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-251",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-251",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776757454436551858",
      "body": "Our first big initiative",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": true
    },
    "time_frame": {
      "id": 813624702,
      "name": "2015"
    },
    "comments_count": 0,
    "goals": [],
    "key_results": [],
    "score_facts": [],
    "integration_fields": [],
    "workflow_status_times": [
      {
        "status_id": "53968949",
        "status_name": "Not Started",
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

## Create an initiative with watchers

**POST** `/api/v1/products/:product_id/initiatives`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the initiative
- `workflow_status` () - **Required** - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives" -d '{"fields":"*,watchers","initiative":{"name":"Initiative 3","watchers":"689956296,16338845"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "6776757454433309187",
    "name": "Initiative 3",
    "reference_num": "PRJ1-S-251",
    "status": "not_started",
    "effort": 95,
    "value": 88,
    "presented": true,
    "color": "#397e82",
    "start_date": null,
    "end_date": null,
    "position": 3,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-251",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-251",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776757454441253585",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": true
    },
    "comments_count": 0,
    "goals": [],
    "key_results": [],
    "score_facts": [],
    "integration_fields": [],
    "workflow_status_times": [
      {
        "status_id": "53968949",
        "status_name": "Not Started",
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

## List initiatives

**GET** `/api/v1/initiatives`

### Parameters
- `q` () - Optional - Search term to match against initiative name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only initiatives updated after the timestamp will be returned.
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, returns only initiatives assigned to that user.
- `only_active` () - Optional - When true, returns only active initiatives.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiatives": [
    {
      "id": "4125886",
      "name": "Initiative 2",
      "reference_num": "PRJ1-S-2",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-2",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-2",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "824706757",
        "body": "Description of initiative 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": [],
      "created_by_user": {
        "id": "82352673",
        "name": "Bob Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "219956332",
      "name": "Initiative 3",
      "reference_num": "PRJ1-S-3",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-3",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-3",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "338250583",
        "body": "Description of project1_initiative3_no_epoch",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "259736534",
      "name": "Initiative 5",
      "reference_num": "PRJ1-S-5",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-5",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-5",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "1040636124",
        "body": "Description of project1_initiative5_archived_epoch",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "time_frame": {
        "id": 834757622,
        "name": "2018"
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "330016191",
      "name": "Initiative 4",
      "reference_num": "PRJ1-S-4",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-4",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-4",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "999437064",
        "body": "Description of project1_initiative4_active_epoch",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "time_frame": {
        "id": 273422810,
        "name": "2017"
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "423077122",
      "name": "Initiative 1",
      "reference_num": "PRJ1-S-1",
      "status": "not_started",
      "effort": 30,
      "value": 50,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 1,
      "score": 4,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "673273729",
        "body": "Description of initiative 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "comments_count": 1,
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
      "score_facts": [],
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
      "master_features": [
        {
          "id": "269219656",
          "reference_num": "PRJ3-E-3",
          "name": "A different project epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ3-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
        },
        {
          "id": "362457003",
          "reference_num": "PRJ1-E-3",
          "name": "And a third",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
        },
        {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
        },
        {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        }
      ],
      "epic": [
        {
          "id": "269219656",
          "reference_num": "PRJ3-E-3",
          "name": "A different project epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ3-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
        },
        {
          "id": "362457003",
          "reference_num": "PRJ1-E-3",
          "name": "And a third",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
        },
        {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
        },
        {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        }
      ],
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
      ],
      "custom_fields": [
        {
          "id": 973371762,
          "key": "initiative_custom_date",
          "name": "Initiative custom date",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "2019-01-01",
          "type": "date"
        },
        {
          "id": 1073063442,
          "key": "initiative_priority",
          "name": "Initiative priority",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "P2",
          "type": "string"
        }
      ],
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "595848429",
      "name": "Initiative complete",
      "reference_num": "PRJ1-S-11",
      "status": "done",
      "effort": 10,
      "value": 70,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 1,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-11",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-11",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "509459046",
        "name": "Done",
        "position": 4,
        "complete": true,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "6776757454435235544",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "1042392694",
      "name": "Workspace line initiative 1",
      "reference_num": "PL1-S-1",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 1,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "610602692",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PL1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PL1-S-1",
      "project": {
        "id": "610602692",
        "reference_prefix": "PL1",
        "name": "Product Line 1",
        "product_line": true,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PL1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "133079347",
        "body": "Description of product_line1_initiative1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": null,
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    }
  ],
  "pagination": {
    "total_records": 7,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List initiatives associated with a goal

**GET** `/api/v1/goals/:goal_id/initiatives`

### Parameters
- `goal_id` () - **Required** - Numeric ID of the goal
- `q` () - Optional - Search term to match against initiative name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only initiatives updated after the timestamp will be returned.
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, returns only initiatives assigned to that user.
- `only_active` () - Optional - When true, returns only active initiatives.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/602095703/initiatives" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiatives": [
    {
      "id": "423077122",
      "name": "Initiative 1",
      "reference_num": "PRJ1-S-1",
      "status": "not_started",
      "effort": 30,
      "value": 50,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 1,
      "score": 4,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "673273729",
        "body": "Description of initiative 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "comments_count": 1,
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
      "score_facts": [],
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
      "master_features": [
        {
          "id": "269219656",
          "reference_num": "PRJ3-E-3",
          "name": "A different project epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ3-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
        },
        {
          "id": "362457003",
          "reference_num": "PRJ1-E-3",
          "name": "And a third",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
        },
        {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
        },
        {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        }
      ],
      "epic": [
        {
          "id": "269219656",
          "reference_num": "PRJ3-E-3",
          "name": "A different project epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ3-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
        },
        {
          "id": "362457003",
          "reference_num": "PRJ1-E-3",
          "name": "And a third",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
        },
        {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
        },
        {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        }
      ],
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
      ],
      "custom_fields": [
        {
          "id": 973371762,
          "key": "initiative_custom_date",
          "name": "Initiative custom date",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "2019-01-01",
          "type": "date"
        },
        {
          "id": 1073063442,
          "key": "initiative_priority",
          "name": "Initiative priority",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "P2",
          "type": "string"
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
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List initiatives in a product

**GET** `/api/v1/products/:product_id/initiatives`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against initiative name.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only initiatives updated after the timestamp will be returned.
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, returns only initiatives assigned to that user.
- `only_active` () - Optional - When true, returns only active initiatives.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/initiatives" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiatives": [
    {
      "id": "4125886",
      "name": "Initiative 2",
      "reference_num": "PRJ1-S-2",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-2",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-2",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "824706757",
        "body": "Description of initiative 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": [],
      "created_by_user": {
        "id": "82352673",
        "name": "Bob Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "219956332",
      "name": "Initiative 3",
      "reference_num": "PRJ1-S-3",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-3",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-3",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "338250583",
        "body": "Description of project1_initiative3_no_epoch",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "259736534",
      "name": "Initiative 5",
      "reference_num": "PRJ1-S-5",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-5",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-5",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "1040636124",
        "body": "Description of project1_initiative5_archived_epoch",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "time_frame": {
        "id": 834757622,
        "name": "2018"
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "330016191",
      "name": "Initiative 4",
      "reference_num": "PRJ1-S-4",
      "status": "not_started",
      "effort": 40,
      "value": 30,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 2,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-4",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-4",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "999437064",
        "body": "Description of project1_initiative4_active_epoch",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "time_frame": {
        "id": 273422810,
        "name": "2017"
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
    },
    {
      "id": "423077122",
      "name": "Initiative 1",
      "reference_num": "PRJ1-S-1",
      "status": "not_started",
      "effort": 30,
      "value": 50,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 1,
      "score": 4,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "53968949",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "673273729",
        "body": "Description of initiative 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": false
      },
      "comments_count": 1,
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
      "score_facts": [],
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
      "master_features": [
        {
          "id": "269219656",
          "reference_num": "PRJ3-E-3",
          "name": "A different project epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ3-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
        },
        {
          "id": "362457003",
          "reference_num": "PRJ1-E-3",
          "name": "And a third",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
        },
        {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
        },
        {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        }
      ],
      "epic": [
        {
          "id": "269219656",
          "reference_num": "PRJ3-E-3",
          "name": "A different project epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ3-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
        },
        {
          "id": "362457003",
          "reference_num": "PRJ1-E-3",
          "name": "And a third",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-3",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
        },
        {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
        },
        {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
        }
      ],
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
      ],
      "custom_fields": [
        {
          "id": 973371762,
          "key": "initiative_custom_date",
          "name": "Initiative custom date",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "2019-01-01",
          "type": "date"
        },
        {
          "id": 1073063442,
          "key": "initiative_priority",
          "name": "Initiative priority",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "P2",
          "type": "string"
        }
      ],
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "595848429",
      "name": "Initiative complete",
      "reference_num": "PRJ1-S-11",
      "status": "done",
      "effort": 10,
      "value": 70,
      "presented": true,
      "color": "#bada55",
      "start_date": null,
      "end_date": null,
      "position": 1,
      "score": 0,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "url": "http://company.aha.io/initiatives/PRJ1-S-11",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-11",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      },
      "workflow_status": {
        "id": "509459046",
        "name": "Done",
        "position": 4,
        "complete": true,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "6776757454432442872",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "attachments": [],
      "assigned_to_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "default_assignee": true
      },
      "comments_count": 0,
      "goals": [],
      "key_results": [],
      "score_facts": [],
      "integration_fields": []
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

## Get a specific initiative

**GET** `/api/v1/initiatives/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the initiative

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/423077122" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Initiative 1",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
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
    "score_facts": [],
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
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
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
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
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

## Update an initiative

**PUT** `/api/v1/products/:product_id/initiatives/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the initiative
- `name` () - Optional - Name of the initiative
- `workflow_status` () - Optional - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives/423077122" -d '{"initiative":{"name":"Smarter initiative"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Smarter initiative",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
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
    "score_facts": [],
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
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
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
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
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

## Update an initiative's custom fields

**PUT** `/api/v1/products/:product_id/initiatives/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the initiative
- `name` () - Optional - Name of the initiative
- `workflow_status` () - Optional - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives/423077122" -d '{"initiative":{"custom_fields":[{"key":"initiative_custom_date","value":"2019-01-01"}]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Initiative 1",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
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
    "score_facts": [],
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
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
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
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
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

## Update an initiative's watchers

**PUT** `/api/v1/products/:product_id/initiatives/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the initiative
- `name` () - Optional - Name of the initiative
- `workflow_status` () - Optional - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives/423077122" -d '{"initiative":{"watchers":[689956296]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Initiative 1",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
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
    "score_facts": [],
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
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
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
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
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

## Update an initiative's progress source

**PUT** `/api/v1/products/:product_id/initiatives/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the initiative
- `name` () - Optional - Name of the initiative
- `workflow_status` () - Optional - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives/423077122" -d '{"initiative":{"progress_source":"progress_from_features"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Initiative 1",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_from_features",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
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
    "score_facts": [],
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
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
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
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
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

## Update an initiative's progress

**PUT** `/api/v1/products/:product_id/initiatives/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the initiative
- `name` () - Optional - Name of the initiative
- `workflow_status` () - Optional - Status of the initiative.
- `description` () - Optional - Description of the initiative — may include HTML formatting.
- `effort` () - Optional - Effort required for the initiative
- `value` () - Optional - Value the initiative brings to the business
- `parent_id` () - Optional - ID of an initiative to roll up to in the parent line, Roll up an initiative to a parent line initiative by 1) creating an initiative for the parent line 2) choosing that initiative in this control. You can then visualize how releases relate to your strategic initiatives throughout Aha!
- `position` () - Optional - Used to sort initiatives
- `presented` () - Optional - Whether this initiative is shown on charts
- `start_date` () - Optional - Start date for the initiative in format YYYY-MM-DD
- `end_date` () - Optional - End date for the initiative in format YYYY-MM-DD
- `time_frame` () - Optional - Name or ID of time frame for this initiative
- `progress_source` () - Optional - Source for calculating progress on the initiative. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_children, progress_from_features_completed, progress_from_epics.
- `progress` () - Optional - Progress completed on the initiative. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end dates. Options are: duration_manual, duration_from_children, duration_from_releases, duration_from_features_epics.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives/423077122" -d '{"initiative":{"progress":25}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Initiative 1",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 25,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
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
    "score_facts": [],
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
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
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
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
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

## Delete an initiative

**DELETE** `/api/v1/products/:product_id/initiatives/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the initiative

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/initiatives/423077122" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
