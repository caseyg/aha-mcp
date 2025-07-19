# Me

## Get the current user

**GET** `/api/v1/me`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/me" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab"
```

**Response:**
```json
{
  "user": {
    "id": "1020675218",
    "name": "Mary Humpty",
    "email": "no-reply@aha.io",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "accessed_at": "2019-01-01T00:00:00.000Z",
    "product_roles": [
      {
        "role": 20,
        "role_description": "Owner",
        "product_id": "517761884",
        "product_name": "Project 2"
      },
      {
        "role": 20,
        "role_description": "Owner",
        "product_id": "610602692",
        "product_name": "Product Line 1"
      },
      {
        "role": 20,
        "role_description": "Owner",
        "product_id": "131414752",
        "product_name": "Project 1"
      }
    ],
    "preferences": {
      "current_product_id": 12123897
    },
    "accounts": [
      {
        "account": {
          "name": "Account 1",
          "domain": "company",
          "logo": null,
          "alt_logo": null,
          "enabled": true
        }
      }
    ]
  }
}
```

---

## List records assigned to the current user

**GET** `/api/v1/me/assigned`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/me/assigned" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab"
```

**Response:**
```json
{
  "assigned": [
    {
      "record_type": "Ideas::Idea",
      "id": 58056975,
      "name": "Idea 1",
      "reference_num": "PRJ1-I-1",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      }
    },
    {
      "record_type": "Release",
      "id": 278327321,
      "name": "Release 1",
      "reference_num": "PRJ1-R-1",
      "workflow_status": {
        "id": "738862546",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      }
    },
    {
      "record_type": "Requirement",
      "id": 483368544,
      "name": "Body of requirement 1",
      "reference_num": "PRJ1-1-1",
      "workflow_status": {
        "id": "934242751",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      }
    },
    {
      "record_type": "Task",
      "id": 748715293,
      "name": "Task name",
      "status": "partially_complete",
      "due_date": "2019-01-01",
      "current_task_user": {
        "id": "6776757454431529338",
        "status": "pending"
      }
    },
    {
      "record_type": "Epic",
      "id": 999605892,
      "name": "Epic 1",
      "reference_num": "PRJ1-E-1",
      "workflow_status": {
        "id": "934242751",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      }
    },
    {
      "record_type": "Feature",
      "id": 1007868956,
      "name": "Feature 1",
      "reference_num": "PRJ1-1",
      "workflow_status": {
        "id": "934242751",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      }
    }
  ]
}
```

---

## List pending tasks assigned to the current user

**GET** `/api/v1/me/tasks`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/me/tasks" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "6776757454436626281",
      "name": "Review first widget",
      "due_date": null,
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
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
