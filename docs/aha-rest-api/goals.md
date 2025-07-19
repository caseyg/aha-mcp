# Goals

## Create a goal

**POST** `/api/v1/products/:product_id/goals`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `project_id` () - **Required** - Numeric ID or key of the project the goals should be created in
- `name` () - **Required** - Name of the goal
- `description` () - Optional - Description of the goal — may include HTML formatting.
- `effort` () - Optional - Value between 1 and 100 describing the goal's position on the effort axis in the goal chart
- `value` () - Optional - Value between 1 and 100 describing the goal's position on the value axis in the goal chart
- `parent_id` () - Optional - ID of a goal to roll up to in the parent line, Roll up a goal to a parent line goal by 1) creating a goal for the parent line 2) choosing that goal in this control. You can then visualize how releases relate to your strategic goals throughout Aha!
- `success_metric_name` () - **Required** - Name of the Metric that will be used to measure this goal's success
- `success_metric_description` () - **Required** - Description of the success metric
- `workflow_status` () - **Required** - Status of the goal
- `time_frame` () - Optional - Name or ID of time frame for this goal
- `progress_source` () - Optional - Source for calculating progress on the goal. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_initiatives, progress_from_descendants, progress_from_features_completed, progress_from_epics, progress_from_key_results.
- `progress` () - Optional - Progress completed on the goal. May only be set when the progress_source is manual.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals" -d '{"goal":{"name":"Goal 3","success_metric":{"name":"FooBar","description":"Foo Bar","workflow_status":"Not Started"},"time_frame":{"name":"2015"},"description":"Our first big goal","effort":15,"value":5}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "6776881149488045145",
    "name": "Goal 3",
    "reference_num": "PRJ1-G-1",
    "effort": 15,
    "value": 5,
    "color": "#397e82",
    "position": 6,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/PRJ1-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/PRJ1-G-1",
    "description": {
      "id": "6776881149491007680",
      "body": "Our first big goal",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "FooBar",
      "description": {
        "id": "6776881149493505600",
        "body": "Foo Bar",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "412273758",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "workflow_status_times": [
        {
          "status_id": "412273758",
          "status_name": "Not Started",
          "started_at": "2019-01-01T00:00:00.000Z",
          "ended_at": null
        }
      ]
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
    "time_frame": {
      "id": 813624702,
      "name": "2015"
    },
    "initiatives": [],
    "key_results": [],
    "comments_count": 0,
    "features": [],
    "releases": [],
    "custom_fields": []
  }
}
```

---

## Create a goal with watchers

**POST** `/api/v1/products/:product_id/goals`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `project_id` () - **Required** - Numeric ID or key of the project the goals should be created in
- `name` () - **Required** - Name of the goal
- `description` () - Optional - Description of the goal — may include HTML formatting.
- `effort` () - Optional - Value between 1 and 100 describing the goal's position on the effort axis in the goal chart
- `value` () - Optional - Value between 1 and 100 describing the goal's position on the value axis in the goal chart
- `parent_id` () - Optional - ID of a goal to roll up to in the parent line, Roll up a goal to a parent line goal by 1) creating a goal for the parent line 2) choosing that goal in this control. You can then visualize how releases relate to your strategic goals throughout Aha!
- `success_metric_name` () - **Required** - Name of the Metric that will be used to measure this goal's success
- `success_metric_description` () - **Required** - Description of the success metric
- `workflow_status` () - **Required** - Status of the goal
- `time_frame` () - Optional - Name or ID of time frame for this goal
- `progress_source` () - Optional - Source for calculating progress on the goal. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_initiatives, progress_from_descendants, progress_from_features_completed, progress_from_epics, progress_from_key_results.
- `progress` () - Optional - Progress completed on the goal. May only be set when the progress_source is manual.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals" -d '{"fields":"*,watchers","goal":{"name":"Goal 3","success_metric":{"name":"FooBar","description":"Foo Bar","workflow_status":"Not Started"},"watchers":"689956296,16338845"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "6776881149493942444",
    "name": "Goal 3",
    "reference_num": "PRJ1-G-1",
    "effort": 95,
    "value": 21,
    "color": "#397e82",
    "position": 6,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/PRJ1-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/PRJ1-G-1",
    "description": {
      "id": "6776881149495211846",
      "body": "",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "FooBar",
      "description": {
        "id": "6776881149489732632",
        "body": "Foo Bar",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "412273758",
        "name": "Not Started",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "workflow_status_times": [
        {
          "status_id": "412273758",
          "status_name": "Not Started",
          "started_at": "2019-01-01T00:00:00.000Z",
          "ended_at": null
        }
      ]
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
    "initiatives": [],
    "key_results": [],
    "comments_count": 0,
    "features": [],
    "releases": [],
    "custom_fields": [],
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

## List goals

**GET** `/api/v1/goals`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goals": [
    {
      "id": "111739083",
      "name": "Goal 5",
      "reference_num": "DEMOENT-G-5",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 5,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-5",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-5",
      "description": {
        "id": "996214770",
        "body": "Description of project1_strategic_imperative5_archived_epoch",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 5",
        "description": {
          "id": "429990377",
          "body": "Description of project1_strategic_imperative5_archived_epoch_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "time_frame": {
        "id": 834757622,
        "name": "2018"
      },
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "242586561",
      "name": "Goal 3",
      "reference_num": "PRJ3-G-1",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "702241743",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/PRJ3-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/PRJ3-G-1",
      "description": {
        "id": "186725916",
        "body": "Description of project3_strategic_imperative1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 4",
        "description": {
          "id": "646872120",
          "body": "Description of project3_strategic_imperative1_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      },
      "project": {
        "id": "702241743",
        "reference_prefix": "PRJ3",
        "name": "Project 3",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ3"
      },
      "parent": {
        "id": "352745835",
        "name": "Product Line Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
        "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "79634897",
          "body": "Description of project2_strategic_imperative1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      },
      "parents": [
        {
          "id": "352745835",
          "name": "Product Line Goal 1",
          "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
          "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "description": {
            "id": "79634897",
            "body": "Description of project2_strategic_imperative1",
            "editor_version": 1,
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          }
        }
      ],
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "352745835",
      "name": "Product Line Goal 1",
      "reference_num": "PL1-G-1",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "610602692",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/PL1-G-1",
      "description": {
        "id": "79634897",
        "body": "Description of project2_strategic_imperative1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 3",
        "description": {
          "id": "909973229",
          "body": "Description of project2_strategic_imperative1_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      },
      "project": {
        "id": "610602692",
        "reference_prefix": "PL1",
        "name": "Product Line 1",
        "product_line": true,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PL1"
      },
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "394052101",
      "name": "Goal 4",
      "reference_num": "PRJ3-G-1",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 2,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "702241743",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/PRJ3-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/PRJ3-G-1",
      "description": {
        "id": "921393880",
        "body": "Description of project3_strategic_imperative2",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 5",
        "description": {
          "id": "96979861",
          "body": "Description of project3_strategic_imperative2_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      },
      "project": {
        "id": "702241743",
        "reference_prefix": "PRJ3",
        "name": "Project 3",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ3"
      },
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "599777734",
      "name": "Goal 6",
      "reference_num": "PRJ5-G-1",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "12123897",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/PRJ5-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/PRJ5-G-1",
      "description": {
        "id": "133581930",
        "body": "Description of project5_strategic_imperative1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 7",
        "description": {
          "id": "508822721",
          "body": "Description of project5_strategic_imperative1_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      },
      "project": {
        "id": "12123897",
        "reference_prefix": "PRJ5",
        "name": "Project 5",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ5"
      },
      "parent": {
        "id": "352745835",
        "name": "Product Line Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
        "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "79634897",
          "body": "Description of project2_strategic_imperative1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      },
      "parents": [
        {
          "id": "352745835",
          "name": "Product Line Goal 1",
          "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
          "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "description": {
            "id": "79634897",
            "body": "Description of project2_strategic_imperative1",
            "editor_version": 1,
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          }
        }
      ],
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "602095703",
      "name": "Goal 1",
      "reference_num": "DEMOENT-G-1",
      "effort": 10,
      "value": 70,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "description": {
        "id": "166463080",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 1",
        "description": {
          "id": "546284368",
          "body": "Description of goal 1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
            "editor_version": 1,
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
        },
        {
          "id": "1017196896",
          "name": "KR 2",
          "reference_num": "DEMOENT-G-1-KR-2",
          "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
          "position": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "target_metric": null,
          "starting_metric": null,
          "current_metric": null
        }
      ],
      "comments_count": 1,
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
      "custom_fields": []
    },
    {
      "id": "712130641",
      "name": "Goal 3",
      "reference_num": "DEMOENT-G-3",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 2,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-3",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-3",
      "description": {
        "id": "568840458",
        "body": "Description of project1_strategic_imperative3_no_epoch",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 3",
        "description": {
          "id": "668008103",
          "body": "Description of project1_strategic_imperative3_no_epoch_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "926116263",
      "name": "Goal 4",
      "reference_num": "DEMOENT-G-4",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 4,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-4",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-4",
      "description": {
        "id": "308494954",
        "body": "Description of project1_strategic_imperative4_active_epoch",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 4",
        "description": {
          "id": "330355042",
          "body": "Description of project1_strategic_imperative4_active_epoch_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "time_frame": {
        "id": 273422810,
        "name": "2017"
      },
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "952896276",
      "name": "Goal 5",
      "reference_num": "PRJ4-G-1",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "935317104",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/PRJ4-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/PRJ4-G-1",
      "description": {
        "id": "141056933",
        "body": "Description of project4_strategic_imperative1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 6",
        "description": {
          "id": "250048102",
          "body": "Description of project4_strategic_imperative1_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      },
      "project": {
        "id": "935317104",
        "reference_prefix": "PRJ4",
        "name": "Project 4",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ4"
      },
      "parent": {
        "id": "352745835",
        "name": "Product Line Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
        "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "79634897",
          "body": "Description of project2_strategic_imperative1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      },
      "parents": [
        {
          "id": "352745835",
          "name": "Product Line Goal 1",
          "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
          "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "description": {
            "id": "79634897",
            "body": "Description of project2_strategic_imperative1",
            "editor_version": 1,
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "attachments": []
          }
        }
      ],
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "988418543",
      "name": "Goal 2",
      "reference_num": "DEMOENT-G-2",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 3,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-2",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-2",
      "description": {
        "id": "1055602421",
        "body": "Description of goal 2",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 2",
        "description": {
          "id": "394826695",
          "body": "Description of goal 2",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "initiatives": [],
      "key_results": [
        {
          "id": "195428809",
          "name": "KR 3",
          "reference_num": "DEMOENT-G-1-KR-3",
          "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-3",
          "position": 3,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "target_metric": null,
          "starting_metric": null,
          "current_metric": null
        }
      ],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
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

## List goals in a product

**GET** `/api/v1/products/:product_id/goals`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/goals" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goals": [
    {
      "id": "111739083",
      "name": "Goal 5",
      "reference_num": "DEMOENT-G-5",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 5,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-5",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-5",
      "description": {
        "id": "996214770",
        "body": "Description of project1_strategic_imperative5_archived_epoch",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 5",
        "description": {
          "id": "429990377",
          "body": "Description of project1_strategic_imperative5_archived_epoch_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "time_frame": {
        "id": 834757622,
        "name": "2018"
      },
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "602095703",
      "name": "Goal 1",
      "reference_num": "DEMOENT-G-1",
      "effort": 10,
      "value": 70,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "description": {
        "id": "166463080",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 1",
        "description": {
          "id": "546284368",
          "body": "Description of goal 1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
            "editor_version": 1,
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
        },
        {
          "id": "1017196896",
          "name": "KR 2",
          "reference_num": "DEMOENT-G-1-KR-2",
          "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
          "position": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "target_metric": null,
          "starting_metric": null,
          "current_metric": null
        }
      ],
      "comments_count": 1,
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
      "custom_fields": []
    },
    {
      "id": "712130641",
      "name": "Goal 3",
      "reference_num": "DEMOENT-G-3",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 2,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-3",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-3",
      "description": {
        "id": "568840458",
        "body": "Description of project1_strategic_imperative3_no_epoch",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 3",
        "description": {
          "id": "668008103",
          "body": "Description of project1_strategic_imperative3_no_epoch_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "926116263",
      "name": "Goal 4",
      "reference_num": "DEMOENT-G-4",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 4,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-4",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-4",
      "description": {
        "id": "308494954",
        "body": "Description of project1_strategic_imperative4_active_epoch",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 4",
        "description": {
          "id": "330355042",
          "body": "Description of project1_strategic_imperative4_active_epoch_strategic_imperative_metric",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "time_frame": {
        "id": 273422810,
        "name": "2017"
      },
      "initiatives": [],
      "key_results": [],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
    },
    {
      "id": "988418543",
      "name": "Goal 2",
      "reference_num": "DEMOENT-G-2",
      "effort": 40,
      "value": 30,
      "color": "#bada55",
      "position": 3,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-2",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-2",
      "description": {
        "id": "1055602421",
        "body": "Description of goal 2",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 2",
        "description": {
          "id": "394826695",
          "body": "Description of goal 2",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
      "initiatives": [],
      "key_results": [
        {
          "id": "195428809",
          "name": "KR 3",
          "reference_num": "DEMOENT-G-1-KR-3",
          "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-3",
          "position": 3,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "target_metric": null,
          "starting_metric": null,
          "current_metric": null
        }
      ],
      "comments_count": 0,
      "features": [],
      "releases": [],
      "custom_fields": []
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

## List goals associated with an initiative

**GET** `/api/v1/initiatives/:initiative_id/goals`

### Parameters
- `initiative_id` () - **Required** - Numeric ID of the initiative

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/423077122/goals" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goals": [
    {
      "id": "602095703",
      "name": "Goal 1",
      "reference_num": "DEMOENT-G-1",
      "effort": 10,
      "value": 70,
      "color": "#bada55",
      "position": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "progress": null,
      "progress_source": "progress_manual",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "description": {
        "id": "166463080",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "success_metric": {
        "name": "Metric 1",
        "description": {
          "id": "546284368",
          "body": "Description of goal 1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "workflow_status": {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
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
            "editor_version": 1,
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
        },
        {
          "id": "1017196896",
          "name": "KR 2",
          "reference_num": "DEMOENT-G-1-KR-2",
          "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
          "position": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "progress": null,
          "target_metric": null,
          "starting_metric": null,
          "current_metric": null
        }
      ],
      "comments_count": 1,
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
      "custom_fields": []
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

## Get a specific goal

**GET** `/api/v1/goals/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the goal

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/6776881149493103487" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "6776881149493103487",
    "name": "Goal 001",
    "reference_num": "PRJ3-G-1",
    "effort": 10,
    "value": 70,
    "color": "#397e82",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "702241743",
    "progress": 0,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/PRJ3-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/PRJ3-G-1",
    "description": {
      "id": "6776881149495498605",
      "body": "",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "Metric 001",
      "description": {
        "id": "6776881149486351445",
        "body": "",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "396368932",
        "name": "On Track",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "workflow_status_times": [
        {
          "status_id": "396368932",
          "status_name": "On Track",
          "started_at": "2019-01-01T00:00:00.000Z",
          "ended_at": null
        }
      ]
    },
    "project": {
      "id": "702241743",
      "reference_prefix": "PRJ3",
      "name": "Project 3",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ3"
    },
    "parent": {
      "id": "352745835",
      "name": "Product Line Goal 1",
      "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
      "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "description": {
        "id": "79634897",
        "body": "Description of project2_strategic_imperative1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    "parents": [
      {
        "id": "352745835",
        "name": "Product Line Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/PL1-G-1",
        "resource": "http://company.aha.io/api/v1/goals/PL1-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "79634897",
          "body": "Description of project2_strategic_imperative1",
          "editor_version": 1,
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      }
    ],
    "initiatives": [],
    "key_results": [],
    "comments_count": 0,
    "features": [],
    "releases": [],
    "custom_fields": []
  }
}
```

---

## Update a goal

**PUT** `/api/v1/products/:product_id/goals/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the goal
- `project_id` () - Optional - Numeric ID or key of the project the goals should be created in
- `name` () - Optional - Name of the goal
- `description` () - Optional - Description of the goal — may include HTML formatting.
- `effort` () - Optional - Value between 1 and 100 describing the goal's position on the effort axis in the goal chart
- `value` () - Optional - Value between 1 and 100 describing the goal's position on the value axis in the goal chart
- `parent_id` () - Optional - ID of a goal to roll up to in the parent line, Roll up a goal to a parent line goal by 1) creating a goal for the parent line 2) choosing that goal in this control. You can then visualize how releases relate to your strategic goals throughout Aha!
- `success_metric_name` () - Optional - Name of the Metric that will be used to measure this goal's success
- `success_metric_description` () - Optional - Description of the success metric
- `workflow_status` () - Optional - Status of the goal
- `time_frame` () - Optional - Name or ID of time frame for this goal
- `progress_source` () - Optional - Source for calculating progress on the goal. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_initiatives, progress_from_descendants, progress_from_features_completed, progress_from_epics, progress_from_key_results.
- `progress` () - Optional - Progress completed on the goal. May only be set when the progress_source is manual.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals/602095703" -d '{"goal":{"description":"An even smarter goal.","workflow_status":"On Track"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "602095703",
    "name": "Goal 1",
    "reference_num": "DEMOENT-G-1",
    "effort": 10,
    "value": 70,
    "color": "#bada55",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "description": {
      "id": "166463080",
      "body": "An even smarter goal.",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "Metric 1",
      "description": {
        "id": "546284368",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "396368932",
        "name": "On Track",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
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
          "editor_version": 1,
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
      },
      {
        "id": "1017196896",
        "name": "KR 2",
        "reference_num": "DEMOENT-G-1-KR-2",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
        "position": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": null,
        "starting_metric": null,
        "current_metric": null
      }
    ],
    "comments_count": 1,
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
    "custom_fields": []
  }
}
```

---

## Update a goal's watchers

**PUT** `/api/v1/products/:product_id/goals/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the goal
- `project_id` () - Optional - Numeric ID or key of the project the goals should be created in
- `name` () - Optional - Name of the goal
- `description` () - Optional - Description of the goal — may include HTML formatting.
- `effort` () - Optional - Value between 1 and 100 describing the goal's position on the effort axis in the goal chart
- `value` () - Optional - Value between 1 and 100 describing the goal's position on the value axis in the goal chart
- `parent_id` () - Optional - ID of a goal to roll up to in the parent line, Roll up a goal to a parent line goal by 1) creating a goal for the parent line 2) choosing that goal in this control. You can then visualize how releases relate to your strategic goals throughout Aha!
- `success_metric_name` () - Optional - Name of the Metric that will be used to measure this goal's success
- `success_metric_description` () - Optional - Description of the success metric
- `workflow_status` () - Optional - Status of the goal
- `time_frame` () - Optional - Name or ID of time frame for this goal
- `progress_source` () - Optional - Source for calculating progress on the goal. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_initiatives, progress_from_descendants, progress_from_features_completed, progress_from_epics, progress_from_key_results.
- `progress` () - Optional - Progress completed on the goal. May only be set when the progress_source is manual.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals/602095703" -d '{"goal":{"watchers":[689956296]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "602095703",
    "name": "Goal 1",
    "reference_num": "DEMOENT-G-1",
    "effort": 10,
    "value": 70,
    "color": "#bada55",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "description": {
      "id": "166463080",
      "body": "Description of goal 1",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "Metric 1",
      "description": {
        "id": "546284368",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "396368932",
        "name": "On Track",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
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
          "editor_version": 1,
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
      },
      {
        "id": "1017196896",
        "name": "KR 2",
        "reference_num": "DEMOENT-G-1-KR-2",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
        "position": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": null,
        "starting_metric": null,
        "current_metric": null
      }
    ],
    "comments_count": 1,
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
    "custom_fields": []
  }
}
```

---

## Update a goal's progress source

**PUT** `/api/v1/products/:product_id/goals/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the goal
- `project_id` () - Optional - Numeric ID or key of the project the goals should be created in
- `name` () - Optional - Name of the goal
- `description` () - Optional - Description of the goal — may include HTML formatting.
- `effort` () - Optional - Value between 1 and 100 describing the goal's position on the effort axis in the goal chart
- `value` () - Optional - Value between 1 and 100 describing the goal's position on the value axis in the goal chart
- `parent_id` () - Optional - ID of a goal to roll up to in the parent line, Roll up a goal to a parent line goal by 1) creating a goal for the parent line 2) choosing that goal in this control. You can then visualize how releases relate to your strategic goals throughout Aha!
- `success_metric_name` () - Optional - Name of the Metric that will be used to measure this goal's success
- `success_metric_description` () - Optional - Description of the success metric
- `workflow_status` () - Optional - Status of the goal
- `time_frame` () - Optional - Name or ID of time frame for this goal
- `progress_source` () - Optional - Source for calculating progress on the goal. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_initiatives, progress_from_descendants, progress_from_features_completed, progress_from_epics, progress_from_key_results.
- `progress` () - Optional - Progress completed on the goal. May only be set when the progress_source is manual.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals/602095703" -d '{"goal":{"progress_source":"progress_from_features"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "602095703",
    "name": "Goal 1",
    "reference_num": "DEMOENT-G-1",
    "effort": 10,
    "value": 70,
    "color": "#bada55",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_from_features",
    "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "description": {
      "id": "166463080",
      "body": "Description of goal 1",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "Metric 1",
      "description": {
        "id": "546284368",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "396368932",
        "name": "On Track",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
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
          "editor_version": 1,
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
      },
      {
        "id": "1017196896",
        "name": "KR 2",
        "reference_num": "DEMOENT-G-1-KR-2",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
        "position": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": null,
        "starting_metric": null,
        "current_metric": null
      }
    ],
    "comments_count": 1,
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
    "custom_fields": []
  }
}
```

---

## Update a goal's progress

**PUT** `/api/v1/products/:product_id/goals/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the goal
- `project_id` () - Optional - Numeric ID or key of the project the goals should be created in
- `name` () - Optional - Name of the goal
- `description` () - Optional - Description of the goal — may include HTML formatting.
- `effort` () - Optional - Value between 1 and 100 describing the goal's position on the effort axis in the goal chart
- `value` () - Optional - Value between 1 and 100 describing the goal's position on the value axis in the goal chart
- `parent_id` () - Optional - ID of a goal to roll up to in the parent line, Roll up a goal to a parent line goal by 1) creating a goal for the parent line 2) choosing that goal in this control. You can then visualize how releases relate to your strategic goals throughout Aha!
- `success_metric_name` () - Optional - Name of the Metric that will be used to measure this goal's success
- `success_metric_description` () - Optional - Description of the success metric
- `workflow_status` () - Optional - Status of the goal
- `time_frame` () - Optional - Name or ID of time frame for this goal
- `progress_source` () - Optional - Source for calculating progress on the goal. Options are: progress_manual, progress_from_features, progress_from_releases, progress_from_initiatives, progress_from_descendants, progress_from_features_completed, progress_from_epics, progress_from_key_results.
- `progress` () - Optional - Progress completed on the goal. May only be set when the progress_source is manual.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals/602095703" -d '{"goal":{"progress":25}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "602095703",
    "name": "Goal 1",
    "reference_num": "DEMOENT-G-1",
    "effort": 10,
    "value": 70,
    "color": "#bada55",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": 25,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "description": {
      "id": "166463080",
      "body": "Description of goal 1",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "Metric 1",
      "description": {
        "id": "546284368",
        "body": "Description of goal 1",
        "editor_version": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "396368932",
        "name": "On Track",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
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
          "editor_version": 1,
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
      },
      {
        "id": "1017196896",
        "name": "KR 2",
        "reference_num": "DEMOENT-G-1-KR-2",
        "url": "http://company.aha.io/key_results/DEMOENT-G-1-KR-2",
        "position": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "progress": null,
        "target_metric": null,
        "starting_metric": null,
        "current_metric": null
      }
    ],
    "comments_count": 1,
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
    "custom_fields": []
  }
}
```

---

## Delete a goal

**DELETE** `/api/v1/products/:product_id/goals/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the goal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/goals/602095703" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
