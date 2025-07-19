# Comments

## Create a comment on a feature

**POST** `/api/v1/features/:feature_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `feature_id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/1007868956/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a feature.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454430500729",
    "body": "<p>This is the comment body for a feature.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454430500729",
    "resource": "http://company.aha.io/api/v1/comments/6776757454430500729",
    "commentable": {
      "type": "Feature",
      "id": "1007868956",
      "product_id": "131414752",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## Create a comment on an epic

**POST** `/api/v1/epics/:epic_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `epic_id` () - **Required** - Numeric ID or key of the epic

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/epics/999605892/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for an epic.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454432331659",
    "body": "<p>This is the comment body for an epic.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454432331659",
    "resource": "http://company.aha.io/api/v1/comments/6776757454432331659",
    "commentable": {
      "type": "Epic",
      "id": "999605892",
      "product_id": "131414752",
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
    }
  }
}
```

---

## Create a comment on a requirement

**POST** `/api/v1/requirements/:requirement_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `requirement_id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/483368544/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a requirement.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454429121230",
    "body": "<p>This is the comment body for a requirement.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454429121230",
    "resource": "http://company.aha.io/api/v1/comments/6776757454429121230",
    "commentable": {
      "type": "Requirement",
      "id": "483368544",
      "product_id": "131414752",
      "url": "http://company.aha.io/requirements/PRJ1-1-1",
      "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1"
    }
  }
}
```

---

## Create a comment on a note

**POST** `/api/v1/pages/:page_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `page_id` () - **Required** - Numeric ID or key of the note

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a note.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454436142835",
    "body": "<p>This is the comment body for a note.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454436142835",
    "resource": "http://company.aha.io/api/v1/comments/6776757454436142835",
    "commentable": {
      "type": "Page",
      "id": "1051981226",
      "product_id": "131414752",
      "url": "http://company.aha.io/pages/PRJ1-N-1",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1"
    }
  }
}
```

---

## Create an internal comment for an idea

**POST** `/api/v1/ideas/:idea_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/58056975/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for an idea.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454437312610",
    "body": "<p>This is the comment body for an idea.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454437312610",
    "resource": "http://company.aha.io/api/v1/comments/6776757454437312610",
    "commentable": {
      "type": "Ideas::Idea",
      "id": "58056975",
      "product_id": "131414752",
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-1",
      "resource": "http://company.aha.io/api/v1/ideas/ideas/PRJ1-I-1"
    }
  }
}
```

---

## Create a comment on an initiative

**POST** `/api/v1/initiatives/:initiative_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `initiative_id` () - **Required** - Numeric ID or key of the initiative

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/initiatives/423077122/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for an initiative.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454438943501",
    "body": "<p>This is the comment body for an initiative.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454438943501",
    "resource": "http://company.aha.io/api/v1/comments/6776757454438943501",
    "commentable": {
      "type": "Initiative",
      "id": "423077122",
      "product_id": "131414752",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1"
    }
  }
}
```

---

## Create a comment on a goal

**POST** `/api/v1/goals/:goal_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `goal_id` () - **Required** - Numeric ID or key of the goal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/goals/602095703/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a goal.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454428410340",
    "body": "<p>This is the comment body for a goal.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454428410340",
    "resource": "http://company.aha.io/api/v1/comments/6776757454428410340",
    "commentable": {
      "type": "StrategicImperative",
      "id": "602095703",
      "product_id": "131414752",
      "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
      "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1"
    }
  }
}
```

---

## Create a comment on a release

**POST** `/api/v1/releases/:release_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/278327321/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a release.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454429477559",
    "body": "<p>This is the comment body for a release.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454429477559",
    "resource": "http://company.aha.io/api/v1/comments/6776757454429477559",
    "commentable": {
      "type": "Release",
      "id": "278327321",
      "product_id": "131414752",
      "url": "http://company.aha.io/releases/PRJ1-R-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1"
    }
  }
}
```

---

## Create a comment on a release phase

**POST** `/api/v1/release_phases/:release_phase_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `release_phase_id` () - **Required** - Numeric ID or key of the release phase

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases/20526005/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a release phase.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454431502913",
    "body": "<p>This is the comment body for a release phase.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454431502913",
    "resource": "http://company.aha.io/api/v1/comments/6776757454431502913",
    "commentable": {
      "type": "ReleasePhase",
      "id": "20526005",
      "url": "http://company.aha.io/release_phases/20526005",
      "resource": "http://company.aha.io/api/v1/release_phases/20526005"
    }
  }
}
```

---

## Create a comment on a to-do

**POST** `/api/v1/tasks/:task_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `task_id` () - **Required** - Numeric ID or key of the to-do

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks/748715293/comments" -d '{"comment":{"body":"\u003cp\u003eThis is the comment body for a to-do.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "6776757454429663874",
    "body": "<p>This is the comment body for a to-do.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [],
    "url": "http://company.aha.io/comments/6776757454429663874",
    "resource": "http://company.aha.io/api/v1/comments/6776757454429663874",
    "commentable": {
      "type": "Task",
      "id": "748715293",
      "product_id": "131414752",
      "url": "http://company.aha.io/tasks/748715293",
      "resource": "http://company.aha.io/api/v1/tasks/748715293"
    }
  }
}
```

---

## Get a specific comment

**GET** `/api/v1/comments/:id`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `id` () - **Required** - Numberic ID of the comment

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/comments/781701978" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "781701978",
    "body": "Comment on feature",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [
      {
        "id": "180276963",
        "download_url": "https://company.aha.io/attachments/180276963/token/aaabbbccc9.download?size=original",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "original_file_size": 123,
        "content_type": "text/plain",
        "file_name": "uploaded_file_name.txt",
        "file_size": 123
      },
      {
        "id": "822785180",
        "download_url": "https://company.aha.io/attachments/822785180/token/aaabbbccc8.download?size=original",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "original_file_size": 123,
        "content_type": "text/plain",
        "file_name": "uploaded_file_name.txt",
        "file_size": 123
      }
    ],
    "url": "http://company.aha.io/comments/781701978",
    "resource": "http://company.aha.io/api/v1/comments/781701978",
    "commentable": {
      "type": "Feature",
      "id": "1007868956",
      "product_id": "131414752",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## List comments in a product

**GET** `/api/v1/products/:project_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `project_id` () - **Required** - Numeric ID of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/131414752/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "428925905",
      "body": "Comment on release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/428925905",
      "resource": "http://company.aha.io/api/v1/comments/428925905",
      "commentable": {
        "type": "Release",
        "id": "278327321",
        "product_id": "131414752",
        "url": "http://company.aha.io/releases/PRJ1-R-1",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1"
      }
    },
    {
      "id": "133461614",
      "body": "Comment on initiative",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/133461614",
      "resource": "http://company.aha.io/api/v1/comments/133461614",
      "commentable": {
        "type": "Initiative",
        "id": "423077122",
        "product_id": "131414752",
        "url": "http://company.aha.io/initiatives/PRJ1-S-1",
        "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1"
      }
    },
    {
      "id": "821249787",
      "body": "Comment on goal",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/821249787",
      "resource": "http://company.aha.io/api/v1/comments/821249787",
      "commentable": {
        "type": "StrategicImperative",
        "id": "602095703",
        "product_id": "131414752",
        "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
        "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1"
      }
    },
    {
      "id": "102125331",
      "body": "Comment 5",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/102125331",
      "resource": "http://company.aha.io/api/v1/comments/102125331",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "522133163",
      "body": "Comment 6",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/522133163",
      "resource": "http://company.aha.io/api/v1/comments/522133163",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "672673340",
      "body": "Comment 7",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/672673340",
      "resource": "http://company.aha.io/api/v1/comments/672673340",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "950481839",
      "body": "Comment 8",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/950481839",
      "resource": "http://company.aha.io/api/v1/comments/950481839",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "262144830",
      "body": "Comment 9",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/262144830",
      "resource": "http://company.aha.io/api/v1/comments/262144830",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "231087120",
      "body": "Comment 10",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/231087120",
      "resource": "http://company.aha.io/api/v1/comments/231087120",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "985738395",
      "body": "Comment 11",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/985738395",
      "resource": "http://company.aha.io/api/v1/comments/985738395",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "600341795",
      "body": "Comment 12",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/600341795",
      "resource": "http://company.aha.io/api/v1/comments/600341795",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "349130164",
      "body": "Comment 13",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/349130164",
      "resource": "http://company.aha.io/api/v1/comments/349130164",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "179034137",
      "body": "Comment 14",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/179034137",
      "resource": "http://company.aha.io/api/v1/comments/179034137",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "1034741892",
      "body": "Comment 15",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/1034741892",
      "resource": "http://company.aha.io/api/v1/comments/1034741892",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "614840636",
      "body": "Comment 16",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/614840636",
      "resource": "http://company.aha.io/api/v1/comments/614840636",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "329419181",
      "body": "Comment 17",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/329419181",
      "resource": "http://company.aha.io/api/v1/comments/329419181",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "52270142",
      "body": "Comment 18",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/52270142",
      "resource": "http://company.aha.io/api/v1/comments/52270142",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "823230344",
      "body": "Comment 4",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/823230344",
      "resource": "http://company.aha.io/api/v1/comments/823230344",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "796256805",
      "body": "Comment 3",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/796256805",
      "resource": "http://company.aha.io/api/v1/comments/796256805",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "410180276",
      "body": "Comment 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/410180276",
      "resource": "http://company.aha.io/api/v1/comments/410180276",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "24873740",
      "body": "Comment 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/24873740",
      "resource": "http://company.aha.io/api/v1/comments/24873740",
      "commentable": {
        "type": "Feature",
        "id": "622562724",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2"
      }
    },
    {
      "id": "213086058",
      "body": "An annotation comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/213086058",
      "resource": "http://company.aha.io/api/v1/comments/213086058",
      "commentable": {
        "type": "Annotation",
        "id": "541632378",
        "url": "http://company.aha.io/annotations/541632378"
      }
    },
    {
      "id": "971503243",
      "body": "This is a requirement comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/971503243",
      "resource": "http://company.aha.io/api/v1/comments/971503243",
      "commentable": {
        "type": "Requirement",
        "id": "483368544",
        "product_id": "131414752",
        "url": "http://company.aha.io/requirements/PRJ1-1-1",
        "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1"
      }
    },
    {
      "id": "340318108",
      "body": "This feature is integrated",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/340318108",
      "resource": "http://company.aha.io/api/v1/comments/340318108",
      "commentable": {
        "type": "Feature",
        "id": "303873333",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-3",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-3"
      }
    },
    {
      "id": "110125740",
      "body": "Comment on competitor 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/110125740",
      "resource": "http://company.aha.io/api/v1/comments/110125740",
      "commentable": {
        "type": "Competitor",
        "id": "892399625",
        "product_id": "131414752",
        "url": "http://company.aha.io/competitors/892399625",
        "resource": "http://company.aha.io/api/v1/competitors/892399625"
      }
    },
    {
      "id": "781701978",
      "body": "Comment on feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [
        {
          "id": "180276963",
          "download_url": "https://company.aha.io/attachments/180276963/token/aaabbbccc9.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "text/plain",
          "file_name": "uploaded_file_name.txt",
          "file_size": 123
        },
        {
          "id": "822785180",
          "download_url": "https://company.aha.io/attachments/822785180/token/aaabbbccc8.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "text/plain",
          "file_name": "uploaded_file_name.txt",
          "file_size": 123
        }
      ],
      "url": "http://company.aha.io/comments/781701978",
      "resource": "http://company.aha.io/api/v1/comments/781701978",
      "commentable": {
        "type": "Feature",
        "id": "1007868956",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
      }
    },
    {
      "id": "933135074",
      "body": "Comment on project",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [
        {
          "id": "109125418",
          "download_url": "https://company.aha.io/attachments/109125418/token/aaabbbccc6.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 67794,
          "content_type": "application/pdf",
          "file_name": "google_doc.pdf",
          "file_size": 67794
        },
        {
          "id": "221084308",
          "download_url": "https://company.aha.io/attachments/221084308/token/aaabbbccc14.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "image/png",
          "file_name": "Mockup.png",
          "file_size": 123
        },
        {
          "id": "229957526",
          "download_url": "https://company.aha.io/attachments/229957526/token/aaabbbccc15.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "image/png",
          "file_name": "not-a-mockup.png",
          "file_size": 123
        },
        {
          "id": "744925247",
          "download_url": "https://company.aha.io/attachments/744925247/token/aaabbbccc1.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "text/plain",
          "file_name": "uploaded_file_name.txt",
          "file_size": 123
        }
      ],
      "url": "http://company.aha.io/comments/933135074",
      "resource": "http://company.aha.io/api/v1/comments/933135074",
      "commentable": {
        "type": "Project",
        "id": "131414752",
        "url": "http://company.aha.io/projects/PRJ1",
        "resource": "http://company.aha.io/api/v1/products/PRJ1"
      }
    },
    {
      "id": "55160124",
      "body": "Comment on project",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/55160124",
      "resource": "http://company.aha.io/api/v1/comments/55160124",
      "commentable": {
        "type": "Task",
        "id": "748715293",
        "product_id": "131414752",
        "url": "http://company.aha.io/tasks/748715293",
        "resource": "http://company.aha.io/api/v1/tasks/748715293"
      }
    },
    {
      "id": "779056158",
      "body": "An annotation comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/779056158",
      "resource": "http://company.aha.io/api/v1/comments/779056158",
      "commentable": {
        "type": "Annotation",
        "id": "594874923",
        "url": "http://company.aha.io/annotations/594874923"
      }
    },
    {
      "id": "714777635",
      "body": "An annotation comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/714777635",
      "resource": "http://company.aha.io/api/v1/comments/714777635",
      "commentable": {
        "type": "Annotation",
        "id": "345680906",
        "url": "http://company.aha.io/annotations/345680906"
      }
    }
  ],
  "pagination": {
    "total_records": 69,
    "total_pages": 3,
    "current_page": 1
  }
}
```

---

## List comments on a feature

**GET** `/api/v1/features/:feature_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `feature_id` () - **Required** - Numeric ID of the feature

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/1007868956/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "781701978",
      "body": "Comment on feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [
        {
          "id": "180276963",
          "download_url": "https://company.aha.io/attachments/180276963/token/aaabbbccc9.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "text/plain",
          "file_name": "uploaded_file_name.txt",
          "file_size": 123
        },
        {
          "id": "822785180",
          "download_url": "https://company.aha.io/attachments/822785180/token/aaabbbccc8.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "text/plain",
          "file_name": "uploaded_file_name.txt",
          "file_size": 123
        }
      ],
      "url": "http://company.aha.io/comments/781701978",
      "resource": "http://company.aha.io/api/v1/comments/781701978",
      "commentable": {
        "type": "Feature",
        "id": "1007868956",
        "product_id": "131414752",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
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

## List comments on an epic

**GET** `/api/v1/epics/:epic_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `epic_id` () - **Required** - Numeric ID of the epic

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/epics/999605892/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "465979716",
      "body": "This is an epic comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/465979716",
      "resource": "http://company.aha.io/api/v1/comments/465979716",
      "commentable": {
        "type": "Epic",
        "id": "999605892",
        "product_id": "131414752",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
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

## List comments on a requirement

**GET** `/api/v1/requirements/:requirement_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `requirement_id` () - **Required** - Numeric ID of the requirement

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/requirements/483368544/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "971503243",
      "body": "This is a requirement comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/971503243",
      "resource": "http://company.aha.io/api/v1/comments/971503243",
      "commentable": {
        "type": "Requirement",
        "id": "483368544",
        "product_id": "131414752",
        "url": "http://company.aha.io/requirements/PRJ1-1-1",
        "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1"
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

## List comments on an idea

**GET** `/api/v1/ideas/:idea_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `idea_id` () - **Required** - Numeric ID of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/58056975/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List comments on an initiative

**GET** `/api/v1/initiatives/:initiative_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `initiative_id` () - **Required** - Numeric ID of the initiative

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/initiatives/423077122/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "133461614",
      "body": "Comment on initiative",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/133461614",
      "resource": "http://company.aha.io/api/v1/comments/133461614",
      "commentable": {
        "type": "Initiative",
        "id": "423077122",
        "product_id": "131414752",
        "url": "http://company.aha.io/initiatives/PRJ1-S-1",
        "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1"
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

## List comments on a goal

**GET** `/api/v1/goals/:goal_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `goal_id` () - **Required** - Numeric ID of the goal

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/goals/602095703/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "821249787",
      "body": "Comment on goal",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/821249787",
      "resource": "http://company.aha.io/api/v1/comments/821249787",
      "commentable": {
        "type": "StrategicImperative",
        "id": "602095703",
        "product_id": "131414752",
        "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
        "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1"
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

## List comments on a release

**GET** `/api/v1/releases/:release_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `release_id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/278327321/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "428925905",
      "body": "Comment on release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/428925905",
      "resource": "http://company.aha.io/api/v1/comments/428925905",
      "commentable": {
        "type": "Release",
        "id": "278327321",
        "product_id": "131414752",
        "url": "http://company.aha.io/releases/PRJ1-R-1",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1"
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

## List comments on a release phase

**GET** `/api/v1/release_phases/:release_phase_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `release_phase_id` () - **Required** - Numeric ID of the release phase

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/release_phases/20526005/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## List comments on a to-do

**GET** `/api/v1/tasks/:task_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `task_id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/tasks/748715293/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "55160124",
      "body": "Comment on project",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/55160124",
      "resource": "http://company.aha.io/api/v1/comments/55160124",
      "commentable": {
        "type": "Task",
        "id": "748715293",
        "product_id": "131414752",
        "url": "http://company.aha.io/tasks/748715293",
        "resource": "http://company.aha.io/api/v1/tasks/748715293"
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

## List comments on a to-do

**GET** `/api/v1/tasks/:task_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `task_id` () - **Required** - Numeric ID of the to-do

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/tasks/748715293/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [
    {
      "id": "55160124",
      "body": "Comment on project",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "attachments": [],
      "url": "http://company.aha.io/comments/55160124",
      "resource": "http://company.aha.io/api/v1/comments/55160124",
      "commentable": {
        "type": "Task",
        "id": "748715293",
        "product_id": "131414752",
        "url": "http://company.aha.io/tasks/748715293",
        "resource": "http://company.aha.io/api/v1/tasks/748715293"
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

## List comments on a note

**GET** `/api/v1/pages/:page_id/comments`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `page_id` () - **Required** - Numeric ID or key of the note

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/pages/1051981226/comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comments": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## Update a comment

**PUT** `/api/v1/comments/:id`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `id` () - **Required** - Numeric ID or key of the comment

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/comments/781701978" -d '{"comment":{"body":"\u003cp\u003eUpdated comment body.\u003c/p\u003e"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "comment": {
    "id": "781701978",
    "body": "<p>Updated comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "attachments": [
      {
        "id": "180276963",
        "download_url": "https://company.aha.io/attachments/180276963/token/aaabbbccc9.download?size=original",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "original_file_size": 123,
        "content_type": "text/plain",
        "file_name": "uploaded_file_name.txt",
        "file_size": 123
      },
      {
        "id": "822785180",
        "download_url": "https://company.aha.io/attachments/822785180/token/aaabbbccc8.download?size=original",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "original_file_size": 123,
        "content_type": "text/plain",
        "file_name": "uploaded_file_name.txt",
        "file_size": 123
      }
    ],
    "url": "http://company.aha.io/comments/781701978",
    "resource": "http://company.aha.io/api/v1/comments/781701978",
    "commentable": {
      "type": "Feature",
      "id": "1007868956",
      "product_id": "131414752",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1"
    }
  }
}
```

---

## Delete a comment

**DELETE** `/api/v1/comments/:id`

### Description
Comments can be added to and listed as a sub-resource on any resource that supports them.
These resources support comments:

- [Features](/api/resources/comments/list_comments_on_a_feature)
- [Epics](/api/resources/comments/list_comments_on_an_epic)
- [Requirements](/api/resources/comments/list_comments_on_a_requirement)
- [Ideas](/api/resources/comments/list_comments_on_an_idea)
- [Initiatives](/api/resources/comments/list_comments_on_an_initiative)
- [Goals](/api/resources/comments/list_comments_on_a_goal)
- [Releases](/api/resources/comments/list_comments_on_a_release)
- [Release phases](/api/resources/comments/list_comments_on_a_release_phase)
- [To-dos](/api/resources/comments/list_comments_on_a_to-do)

They can be listed [product-wide](/api/resources/comments/list_comments_in_a_product),
or retrieved from anywhere in the system using the root [comments resource](/api/resources/comments/get_a_specific_comment).


### Parameters
- `id` () - **Required** - Numeric ID of the comment

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/comments/55160124" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
