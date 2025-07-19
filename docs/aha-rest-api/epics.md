# Epics

## List epics

**GET** `/api/v1/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `q` () - Optional - Search term to match against epic name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only epics updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only epics with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only epics assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epics": [
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
      "id": "531908612",
      "reference_num": "PRJ2-E-1",
      "name": "An epic in project 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/epics/PRJ2-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ2-E-1"
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
  "pagination": {
    "total_records": 5,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List epics in a release

**GET** `/api/v1/releases/:release_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `q` () - Optional - Search term to match against epic name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only epics updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only epics with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only epics assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/PRJ1-R-1/epics" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epics": [
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
  "pagination": {
    "total_records": 3,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List epics in a product

**GET** `/api/v1/products/:product_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against epic name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only epics updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only epics with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only epics assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/epics" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epics": [
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
  "pagination": {
    "total_records": 3,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List epics associated with a goal

**GET** `/api/v1/goals/:goal_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `goal_id` () - **Required** - Numeric ID of the goal
- `q` () - Optional - Search term to match against epic name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only epics updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only epics with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only epics assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/602095703/epics" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epics": [
    {
      "id": "999605892",
      "reference_num": "PRJ1-E-1",
      "name": "Epic 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
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

## List epics associated with an initiative

**GET** `/api/v1/initiatives/:initiative_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `initiative_id` () - **Required** - Numeric ID of the initiative
- `q` () - Optional - Search term to match against epic name
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only epics updated after the timestamp will be returned
- `tag` () - Optional - String tag value. If provided, only epics with the associated tag will be returned
- `assigned_to_user` () - Optional - ID or email address of a user. If provided, only epics assigned to that user will be returned

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/423077122/epics" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epics": [
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
  "pagination": {
    "total_records": 4,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific epic

**GET** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epic

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics/PRJ1-E-1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Delete an epic

**DELETE** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epic

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create an epic

**POST** `/api/v1/releases/:release_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/epics" -d '{"epic":{"name":"New name","description":"New description","detailed_estimate_text":"58min"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "6776757454430579639",
    "name": "New name",
    "reference_num": "PRJ1-E-251",
    "initiative_reference_num": null,
    "position": 1,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "131414752",
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
      "id": "6776757454437087046",
      "body": "New description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/epics/PRJ1-E-251",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-251",
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
        "status_id": "934242751",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "epic_links": [],
    "master_feature_only_original_estimate": 58,
    "master_feature_only_remaining_estimate": 58,
    "master_feature_only_work_done": null,
    "epic_only_original_estimate": 58,
    "epic_only_remaining_estimate": 58,
    "epic_only_work_done": null
  }
}
```

---

## Create an epic with watchers

**POST** `/api/v1/releases/:release_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/epics" -d '{"epic":{"name":"New epics","description":"New description","detailed_estimate_text":"58min","watchers":"689956296,16338845"},"fields":"*,watchers"}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "6776757454432540112",
    "name": "New epics",
    "reference_num": "PRJ1-E-251",
    "initiative_reference_num": null,
    "position": 1,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "131414752",
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
      "id": "6776757454431607832",
      "body": "New description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/epics/PRJ1-E-251",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-251",
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
        "status_id": "934242751",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "epic_links": [],
    "master_feature_only_original_estimate": 58,
    "master_feature_only_remaining_estimate": 58,
    "master_feature_only_work_done": null,
    "epic_only_original_estimate": 58,
    "epic_only_remaining_estimate": 58,
    "epic_only_work_done": null,
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

## Create an epic with goals

**POST** `/api/v1/releases/:release_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/epics" -d '{"epic":{"name":"New feature","description":"New description","detailed_estimate_text":"58min","workflow_kind":"new","workflow_status":{"name":"Designed"},"goals":"602095703,988418543"},"fields":"*,goals"}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "6776757454432969240",
    "name": "New feature",
    "reference_num": "PRJ1-E-251",
    "initiative_reference_num": null,
    "position": 1,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "131414752",
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
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "description": {
      "id": "6776757454426617099",
      "body": "New description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/epics/PRJ1-E-251",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-251",
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
    "features": [],
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
    "workflow_status_times": [
      {
        "status_id": "962984386",
        "status_name": "Designed",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "epic_links": [],
    "master_feature_only_original_estimate": 58,
    "master_feature_only_remaining_estimate": 58,
    "master_feature_only_work_done": null,
    "epic_only_original_estimate": 58,
    "epic_only_remaining_estimate": 58,
    "epic_only_work_done": null
  }
}
```

---

## Create an epic on behalf of a user

**POST** `/api/v1/releases/:release_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release
- `name` () - **Required** - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1/epics" -d '{"epic":{"name":"New epics","description":"New description","detailed_estimate_text":"58min","created_by":"no-reply@aha.io"},"fields":"*,created_by"}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "6776757454435519853",
    "name": "New epics",
    "reference_num": "PRJ1-E-251",
    "initiative_reference_num": null,
    "position": 1,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": "2019-01-01",
    "created_by_user": {
      "id": "601067208",
      "name": "Jeremy Smith",
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
      "id": "6776757454431800568",
      "body": "New description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/epics/PRJ1-E-251",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-251",
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
        "status_id": "934242751",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "epic_links": [],
    "master_feature_only_original_estimate": 58,
    "master_feature_only_remaining_estimate": 58,
    "master_feature_only_work_done": null,
    "epic_only_original_estimate": 58,
    "epic_only_remaining_estimate": 58,
    "epic_only_work_done": null
  }
}
```

---

## Create an epic in the default release

**POST** `/api/v1/products/:product_id/epics`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `product_id` () - **Required** - Numeric ID,or key of the product
- `name` () - **Required** - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/epics" -d '{"epic":{"name":"New name"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "6776757454427279043",
    "name": "New name",
    "reference_num": "PRJ1-E-251",
    "initiative_reference_num": null,
    "position": 1,
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": null,
    "due_date": null,
    "product_id": "131414752",
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
      "id": "6776757454437373805",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [],
    "url": "http://company.aha.io/epics/PRJ1-E-251",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-251",
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
        "status_id": "934242751",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "epic_links": [],
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

## Update an epic

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"name":"New name","description":"New description"}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "New name",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "New description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "New name",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's custom fields

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"custom_fields":{"priority":"P3"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's tags with comma-separated values

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"tags":"tag2, tag3"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "tag2",
      "tag3"
    ],
    "full_tags": [
      {
        "id": "6776757454425839160",
        "name": "tag3",
        "color": "#bb52e0"
      },
      {
        "id": "6776757454435088477",
        "name": "tag2",
        "color": "#52d3e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's tags with an array

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"tags":["tag2","tag3"]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "tag2",
      "tag3"
    ],
    "full_tags": [
      {
        "id": "6776757454430999804",
        "name": "tag2",
        "color": "#52d3e0"
      },
      {
        "id": "6776757454440974702",
        "name": "tag3",
        "color": "#bb52e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's watchers

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"watchers":[689956296]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's goals

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"goals":[602095703]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's score

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"score_facts":[{"name":"Benefit","value":4},{"name":"Effort","value":5}]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 9,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [
      {
        "id": "6776757454432375882",
        "value": 4,
        "name": "Benefit"
      },
      {
        "id": "6776757454440564006",
        "value": 5,
        "name": "Effort"
      }
    ],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's progress source

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"progress_source":"progress_from_features"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": 0,
    "progress_source": "progress_from_features",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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

## Update an epic's progress

**PUT** `/api/v1/epics/:id`

### Description
Epics belong to releases. This means that if you want to create one then you must scope it to a release.

You can
[list them all](/api/resources/epics/list_epics)
at once, or filter by
[release](/api/resources/epics/list_epics_in_a_release)
or
[product](/api/resources/epics/list_epics_in_a_product).
All these means of listing epics can be further filtered by specific critera like name, modification date, tag, or assignee.

Once you have the id of a specific epic, you can
[inspect](/api/resources/epics/get_a_specific_epic),
[modify](/api/resources/epics/update_an_epic),
or
[delete](/api/resources/epics/delete_an_epic)
them on the root epics resource.


### Parameters
- `id` () - **Required** - Numeric ID or key of the epics
- `name` () - Optional - Name of the epic
- `release` () - Optional - Numeric ID or key of the release the epic should be created in.
- `workflow_status` () - Optional - Status of the epic — must be a valid status for the selected product.
- `description` () - Optional - Description of the epic — may include HTML formatting.
- `created_by` () - Optional - Email address of the user who created the epic.
- `assigned_to_user` () - Optional - Email address of user that is assigned the epic.
- `tags` () - Optional - Tags to add to the epic. Multiple tags must be separated by commas.
- `initial_estimate_text` () - Optional - The initial estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `detailed_estimate_text` () - Optional - The detailed estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `remaining_estimate_text` () - Optional - The remaining estimated effort in time or story points for this epic, depending on the capacity units configured.

For time: use min, h, d, w, m. Example: "2d 1h”.

1d = 8h, 1w = 5d, 1m = 22d.

For story points: Use p to represent points. Example: "4p”.

- `initial_estimate` () - Optional - Set the initial estimated effort in minutes or story points, depending on the capacity units configured.
- `detailed_estimate` () - Optional - Set the detailed estimated effort in minutes or story points, depending on the capacity units configured.
- `remaining_estimate` () - Optional - Set the remaining estimated effort in minutes or story points, depending on the capacity units configured.
- `start_date` () - Optional - Date that work will start on the epic in format YYYY-MM-DD
- `due_date` () - Optional - Date that work is due to be completed on the epic in format YYYY-MM-DD
- `initiative` () - Optional - Name or id of initiative which the epic belongs to
- `progress_source` () - Optional - Source for calculating progress on the epic. Options are: progress_manual, progress_from_features, progress_from_remaining_estimate, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the epic. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and due dates. Options are: duration_manual, duration_from_features.
- `team` () - Optional - Numeric ID or key of the team to assign the epic to.
- `team_workflow_status` () - Optional - Team status of the epic — must be a valid status for the selected team.
- `iteration` () - Optional - ID of sprint to assign the epic to, must belong to the selected team.
- `program_increment` () - Optional - Numeric ID or key of the PI to assign the epic to, must belong to the selected team.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/PRJ1-E-1" -d '{"epic":{"progress":25}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "epic": {
    "id": "999605892",
    "name": "Epic 1",
    "reference_num": "PRJ1-E-1",
    "initiative_reference_num": "PRJ1-S-1",
    "position": 1,
    "score": 42,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": 25,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
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
      "id": "4321567",
      "body": "Body of Epic Description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "790422735",
        "name": "id",
        "value": "433333335",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "907392375",
        "name": "key",
        "value": "JRA-1222223",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/epics/PRJ1-E-1",
    "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
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
    "key_results": [],
    "comments_count": 1,
    "score_facts": [],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1001163083,
        "key": "epic_custom_date",
        "name": "Epic custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1043080183,
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "epic_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "999605892",
          "reference_num": "PRJ1-E-1",
          "name": "Epic 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-1",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "580753216",
          "reference_num": "PRJ1-E-2",
          "name": "Here's another epic",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/epics/PRJ1-E-2",
          "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2",
          "product_id": "131414752"
        }
      }
    ],
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
