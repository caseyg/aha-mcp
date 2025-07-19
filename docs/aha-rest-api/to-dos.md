# To-dos

## Create a task

**POST** `/api/v1/tasks`

### Parameters
- `name` () - **Required** - The name of the task
- `body` () - **Required** - The description of the task
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `type` () - Optional - The type of the task. `type` can be one of the following:

- Task
- Approval
- WorkRequest

- `assigned_to_users` () - Optional - Email addresses of assigned users
- `due_date` () - Optional - The date the task is due

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks" -d '{"task":{"name":"Review press release","body":"\u003cp\u003eCan you please review the press release\u003c/p\u003e","assigned_to_users":[{"email":"no-reply@aha.io"}]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "6776757454436626281",
    "name": "Review press release",
    "body": "<p>Can you please review the press release</p>",
    "due_date": null,
    "status": "pending",
    "position": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "6776757454431529338",
        "status": "pending",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/6776757454436626281",
    "resource": "http://company.aha.io/api/v1/tasks/6776757454436626281",
    "comments_count": 0
  }
}
```

---

## Create a to-do without an associated record

**POST** `/api/v1/tasks`

### Parameters
- `name` () - **Required** - The name of the task
- `body` () - **Required** - The description of the task
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `type` () - Optional - The type of the task. `type` can be one of the following:

- Task
- Approval
- WorkRequest

- `assigned_to_users` () - Optional - Email addresses of assigned users
- `due_date` () - Optional - The date the task is due

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks" -d '{"task":{"name":"Review press release","body":"\u003cp\u003eCan you please review the press release\u003c/p\u003e","assigned_to_users":[{"email":"no-reply@aha.io"}]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "6776757454427990963",
    "name": "Review press release",
    "body": "<p>Can you please review the press release</p>",
    "due_date": null,
    "status": "pending",
    "position": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "6776757454435007688",
        "status": "pending",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/6776757454427990963",
    "resource": "http://company.aha.io/api/v1/tasks/6776757454427990963",
    "comments_count": 0
  }
}
```

---

## Create a to-do with a due date

**POST** `/api/v1/tasks`

### Parameters
- `name` () - **Required** - The name of the task
- `body` () - **Required** - The description of the task
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `type` () - Optional - The type of the task. `type` can be one of the following:

- Task
- Approval
- WorkRequest

- `assigned_to_users` () - Optional - Email addresses of assigned users
- `due_date` () - Optional - The date the task is due

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks" -d '{"task":{"name":"Review press release","body":"\u003cp\u003eCan you please review the press release\u003c/p\u003e","assigned_to_users":[{"email":"no-reply@aha.io"}],"due_date":"2019-01-01"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "6776757454440871378",
    "name": "Review press release",
    "body": "<p>Can you please review the press release</p>",
    "due_date": "2019-01-01",
    "status": "pending",
    "position": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "6776757454428883981",
        "status": "pending",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/6776757454440871378",
    "resource": "http://company.aha.io/api/v1/tasks/6776757454440871378",
    "comments_count": 0
  }
}
```

---

## Create a to-do associated with a feature

**POST** `/api/v1/tasks`

### Parameters
- `name` () - **Required** - The name of the task
- `body` () - **Required** - The description of the task
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `type` () - Optional - The type of the task. `type` can be one of the following:

- Task
- Approval
- WorkRequest

- `assigned_to_users` () - Optional - Email addresses of assigned users
- `due_date` () - Optional - The date the task is due

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks" -d '{"task":{"name":"Review press release","body":"\u003cp\u003eCan you please review the press release\u003c/p\u003e","taskable_type":"Feature","taskable_id":1007868956}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "6776757454426745348",
    "name": "Review press release",
    "body": "<p>Can you please review the press release</p>",
    "due_date": null,
    "status": "pending",
    "position": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "assigned_to_users": [],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/6776757454426745348",
    "resource": "http://company.aha.io/api/v1/tasks/6776757454426745348",
    "comments_count": 0,
    "taskable": {
      "type": "Feature",
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## Create an approval associated with a feature

**POST** `/api/v1/tasks`

### Parameters
- `name` () - **Required** - The name of the task
- `body` () - **Required** - The description of the task
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `type` () - Optional - The type of the task. `type` can be one of the following:

- Task
- Approval
- WorkRequest

- `assigned_to_users` () - Optional - Email addresses of assigned users
- `due_date` () - Optional - The date the task is due

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks" -d '{"task":{"name":"Approve press release","body":"\u003cp\u003eCan you please approve the press release\u003c/p\u003e","taskable_type":"Feature","taskable_id":1007868956,"type":"Approval"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "6776757454426175834",
    "name": "Approve press release",
    "body": "<p>Can you please approve the press release</p>",
    "due_date": null,
    "status": "pending",
    "position": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "assigned_to_users": [],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/6776757454426175834",
    "resource": "http://company.aha.io/api/v1/tasks/6776757454426175834",
    "comments_count": 0,
    "taskable": {
      "type": "Feature",
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## Create a to-do with multiple assignees

**POST** `/api/v1/tasks`

### Parameters
- `name` () - **Required** - The name of the task
- `body` () - **Required** - The description of the task
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `taskable_type` () - Optional - The type of record the task belongs to. `taskable_type` can be one of the following:

- BusinessModel
- Competitor
- CreativeBrief
- Epic
- Feature
- Ideas::FeedbackCampaign
- Ideas::Idea
- Ideas::IdeaSession
- Initiative
- Iteration
- MasterRelease
- Page
- ProjectStrategyComponent
- Persona
- Project
- ProjectStrategy
- Publish::Notebook
- Release
- ReleasePhase
- Requirement
- StrategicImperative
- StrategicImperativeBackground

- `taskable_id` () - Optional - The reference number or ID of the record the task belongs to
- `type` () - Optional - The type of the task. `type` can be one of the following:

- Task
- Approval
- WorkRequest

- `assigned_to_users` () - Optional - Email addresses of assigned users
- `due_date` () - Optional - The date the task is due

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks" -d '{"task":{"name":"Review press release","body":"\u003cp\u003eCan you please review the press release\u003c/p\u003e","assigned_to_users":[{"email":"no-reply@aha.io"},{"email":"sally.sane@account2.com"}]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "6776757454426073507",
    "name": "Review press release",
    "body": "<p>Can you please review the press release</p>",
    "due_date": null,
    "status": "pending",
    "position": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "6776757454438153817",
        "status": "pending",
        "user": {
          "id": "349538572",
          "name": "Sally Sane",
          "email": "sally.sane@account2.com",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      },
      {
        "id": "6776757454436876355",
        "status": "pending",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/6776757454426073507",
    "resource": "http://company.aha.io/api/v1/tasks/6776757454426073507",
    "comments_count": 0
  }
}
```

---

## List to-dos

**GET** `/api/v1/tasks`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "270131066",
      "name": "Do this thing.",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "486361616",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "491284354",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "644916258",
      "name": "Task name 1",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "654705094",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "664116853",
      "name": "Overdue task",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "742756265",
      "name": "Get it done",
      "due_date": "2019-01-01",
      "status": "partially_complete",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "748715293",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "completed",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "785584324",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "896534432",
      "name": "Annotations task",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "937465541",
      "name": "Task name 2",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "1041191038",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "partially_complete",
      "created_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "pagination": {
    "total_records": 12,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get tasks updated after a certain time

**GET** `/api/v1/tasks`

### Parameters
- `updated_since` () - Optional - Filter to all to-dos updated after this DateTime. Should be specified as an ISO8601 string

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/tasks?updated_since=2019-01-01T18%3A39%3A35Z" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "270131066",
      "name": "Do this thing.",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "486361616",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "491284354",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "644916258",
      "name": "Task name 1",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "654705094",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "664116853",
      "name": "Overdue task",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "742756265",
      "name": "Get it done",
      "due_date": "2019-01-01",
      "status": "partially_complete",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "785584324",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "896534432",
      "name": "Annotations task",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "937465541",
      "name": "Task name 2",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "1041191038",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "partially_complete",
      "created_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "pagination": {
    "total_records": 11,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List approvals

**GET** `/api/v1/tasks`

### Parameters
- `type` () - Optional - Type of to-do (Task or Approval)

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/tasks?type=Approval" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "568474467",
      "name": "Task name",
      "due_date": "2019-01-01",
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

## List to-dos associated with a feature

**GET** `/api/v1/features/:feature_id/tasks`

### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/PRJ1-1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "748715293",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "completed",
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

## List to-dos associated with an epic

**GET** `/api/v1/epics/:epic_id/tasks`

### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the epic

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics/PRJ1-E-1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "486361616",
      "name": "Task name",
      "due_date": "2019-01-01",
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

## List to-dos associated with a release

**GET** `/api/v1/releases/:release_id/tasks`

### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/PRJ1-R-1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List to-dos associated with an idea

**GET** `/api/v1/ideas/:idea_id/tasks`

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List to-dos associated with a requirement

**GET** `/api/v1/requirements/:requirement_id/tasks`

### Parameters
- `requirement_id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/requirements/PRJ1-1-1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "270131066",
      "name": "Do this thing.",
      "due_date": "2019-01-01",
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

## List to-dos associated with a product

**GET** `/api/v1/products/:product_id/tasks`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [
    {
      "id": "270131066",
      "name": "Do this thing.",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "486361616",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "491284354",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "644916258",
      "name": "Task name 1",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "742756265",
      "name": "Get it done",
      "due_date": "2019-01-01",
      "status": "partially_complete",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "748715293",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "completed",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "785584324",
      "name": "Task name",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "896534432",
      "name": "Annotations task",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "937465541",
      "name": "Task name 2",
      "due_date": "2019-01-01",
      "status": "pending",
      "created_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "pagination": {
    "total_records": 9,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List to-dos assigned to a user

**GET** `/api/v1/users/:user_id/tasks`

### Parameters
- `user_id` () - **Required** - Numeric ID or key of the user

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/users/1049303076/tasks" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "tasks": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## Get a specific to-do

**GET** `/api/v1/tasks/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/tasks/1041191038" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "1041191038",
    "name": "Task name",
    "body": "Task body",
    "due_date": "2019-01-01",
    "status": "partially_complete",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "1061194521",
        "status": "completed",
        "user": {
          "id": "601067208",
          "name": "Jeremy Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      },
      {
        "id": "642374309",
        "status": "pending",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/1041191038",
    "resource": "http://company.aha.io/api/v1/tasks/1041191038",
    "comments_count": 0
  }
}
```

---

## Update a to-do

**PUT** `/api/v1/tasks/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks/1041191038" -d '{"task":{"body":"\u003cp\u003eCan you please review this press release\u003c/p\u003e"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "1041191038",
    "name": "Task name",
    "body": "<p>Can you please review this press release</p>",
    "due_date": "2019-01-01",
    "status": "partially_complete",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "1061194521",
        "status": "completed",
        "user": {
          "id": "601067208",
          "name": "Jeremy Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      },
      {
        "id": "642374309",
        "status": "pending",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/1041191038",
    "resource": "http://company.aha.io/api/v1/tasks/1041191038",
    "comments_count": 0
  }
}
```

---

## Update a to-do's status

**PUT** `/api/v1/tasks/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks/1041191038" -d '{"task":{"status":"complete"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "1041191038",
    "name": "Task name",
    "body": "Task body",
    "due_date": "2019-01-01",
    "status": "completed",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "",
    "assigned_to_users": [
      {
        "id": "1061194521",
        "status": "completed",
        "user": {
          "id": "601067208",
          "name": "Jeremy Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      },
      {
        "id": "642374309",
        "status": "completed",
        "completed_date": "2019-01-01T00:00:00.000Z",
        "user": {
          "id": "689956296",
          "name": "Henry Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/1041191038",
    "resource": "http://company.aha.io/api/v1/tasks/1041191038",
    "comments_count": 0
  }
}
```

---

## Delete a to-do

**DELETE** `/api/v1/tasks/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks/1041191038" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Update an approval's status

**PUT** `/api/v1/tasks/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks/568474467" -d '{"task":{"status":"approved","type":"Approval"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "task": {
    "id": "568474467",
    "name": "Task name",
    "body": "Task body",
    "due_date": "2019-01-01",
    "status": "completed",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "702241743",
    "assigned_to_users": [
      {
        "id": "938180846",
        "status": "completed",
        "completed_date": "2019-01-01T00:00:00.000Z",
        "user": {
          "id": "1020675218",
          "name": "Mary Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/tasks/568474467",
    "resource": "http://company.aha.io/api/v1/tasks/568474467",
    "comments_count": 0,
    "taskable": {
      "type": "Feature",
      "id": "959120953",
      "reference_num": "PRJ3-2",
      "name": "A third Feature",
      "url": "http://company.aha.io/features/PRJ3-2",
      "resource": "http://company.aha.io/api/v1/features/PRJ3-2"
    }
  }
}
```

---
