# Idea comments

## Create an idea comment for an idea

**POST** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `body` () - **Required** - Body of the idea comment - may include html formatting.
- `spam` () - Optional - Whether the idea comment is considered spam. Must be 'true' or 'false'
- `visibility` () - Optional - Visibility of the idea comment (public or employee_or_creator; public is the default). Not for replies, who get their visibility from their parent idea comment instead.
- `parent_idea_comment_id` () - Optional - Numeric ID of the parent idea_comment to reply to.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/idea_comments" -d '{"idea_comment":{"idea_id":"PRJ1-I-1","body":"\u003cp\u003eThis is the comment body.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "6776757454438266938",
    "idea_id": "58056975",
    "body": "<p>This is the comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to all ideas portal users",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Create an idea comment with restricted visibility

**POST** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `body` () - **Required** - Body of the idea comment - may include html formatting.
- `spam` () - Optional - Whether the idea comment is considered spam. Must be 'true' or 'false'
- `visibility` () - Optional - Visibility of the idea comment (public or employee_or_creator; public is the default). Not for replies, who get their visibility from their parent idea comment instead.
- `parent_idea_comment_id` () - Optional - Numeric ID of the parent idea_comment to reply to.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/idea_comments" -d '{"idea_comment":{"idea_id":"PRJ1-I-1","body":"\u003cp\u003eThis is the comment body.\u003c/p\u003e","visibility":"employee_or_creator"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "6776757454428183566",
    "idea_id": "58056975",
    "body": "<p>This is the comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to creator and employees",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Create an idea comment visible to idea creator

**POST** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `body` () - **Required** - Body of the idea comment - may include html formatting.
- `spam` () - Optional - Whether the idea comment is considered spam. Must be 'true' or 'false'
- `visibility` () - Optional - Visibility of the idea comment (public or employee_or_creator; public is the default). Not for replies, who get their visibility from their parent idea comment instead.
- `parent_idea_comment_id` () - Optional - Numeric ID of the parent idea_comment to reply to.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/idea_comments" -d '{"idea_comment":{"idea_id":"PRJ1-I-1","body":"\u003cp\u003eThis is the comment body.\u003c/p\u003e","visibility":"employee_or_idea_creator"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "6776757454428123697",
    "idea_id": "58056975",
    "body": "<p>This is the comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to idea creator and our employees",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Create an idea comment reply to a parent idea_comment

**POST** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `body` () - **Required** - Body of the idea comment - may include html formatting.
- `spam` () - Optional - Whether the idea comment is considered spam. Must be 'true' or 'false'
- `visibility` () - Optional - Visibility of the idea comment (public or employee_or_creator; public is the default). Not for replies, who get their visibility from their parent idea comment instead.
- `parent_idea_comment_id` () - Optional - Numeric ID of the parent idea_comment to reply to.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/idea_comments" -d '{"idea_comment":{"idea_id":"PRJ1-I-1","body":"\u003cp\u003eThis is the comment body.\u003c/p\u003e","parent_idea_comment_id":622085811}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "6776757454434762031",
    "idea_id": "58056975",
    "body": "<p>This is the comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to all ideas portal users",
    "parent_idea_comment_id": 622085811,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Create an idea comment created by an ideas portal user (specified by id)

**POST** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `body` () - **Required** - Body of the idea comment - may include html formatting.
- `portal_user` () - Optional - Portal user who created the idea comment
- `spam` () - Optional - Whether the idea comment is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/idea_comments" -d '{"idea_comment":{"idea_id":"PRJ1-I-1","portal_user":{"id":646391926},"body":"\u003cp\u003eThis is the comment body.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "6776757454425479504",
    "idea_id": "58056975",
    "body": "<p>This is the comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to all ideas portal users",
    "parent_idea_comment_id": null,
    "idea_commenter_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_commenter_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Create an idea comment created by an Aha! user (specified by id)

**POST** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `body` () - **Required** - Body of the idea comment - may include html formatting.
- `user` () - Optional - The Aha! user who created the idea comment.
- `spam` () - Optional - Whether the idea comment is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/idea_comments" -d '{"idea_comment":{"idea_id":"PRJ1-I-1","user":{"id":689956296},"body":"\u003cp\u003eThis is the comment body.\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "6776757454438967249",
    "idea_id": "58056975",
    "body": "<p>This is the comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to all ideas portal users",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## List idea comments for an idea

**GET** `/api/v1/ideas/:idea_id/idea_comments`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `spam` () - Optional - When true, shows idea comments that have been marked as spam. By default, no spam ideas will be shown.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/58056975/idea_comments" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comments": [
    {
      "id": "622085811",
      "idea_id": "58056975",
      "body": "This is a great idea! We'll get started right away.",
      "created_at": "2019-01-01T00:00:00.000Z",
      "visibility": "Visible to all ideas portal users",
      "parent_idea_comment_id": null,
      "idea_commenter_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
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
      },
      "attachments": []
    },
    {
      "id": "6776757454428931551",
      "idea_id": "58056975",
      "body": "A reply to a comment",
      "created_at": "2019-01-01T00:00:00.000Z",
      "visibility": "Visible to all ideas portal users",
      "parent_idea_comment_id": 622085811,
      "idea_commenter_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
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
      },
      "attachments": []
    },
    {
      "id": "6776757454433176488",
      "idea_id": "58056975",
      "body": "Just us employees",
      "created_at": "2019-01-01T00:00:00.000Z",
      "visibility": "Visible to creator and employees",
      "parent_idea_comment_id": null,
      "idea_commenter_user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
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
      },
      "attachments": []
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

## Mark an idea comment as spam

**PUT** `/api/v1/idea_comments/:id`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `id` () - **Required** - Numeric ID of the idea comment
- `spam` () - Optional - Whether the comment is considered spam. Must be 'true' or 'false'
- `visibility` () - Optional - Visibility of the idea comment (public, employee_or_creator or employee_or_idea_creator; public is the default). Not for replies, who get their visibility from their parent idea comment instead.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_comments/622085811" -d '{"idea_comment":{"spam":"true"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "622085811",
    "idea_id": "58056975",
    "body": "This is a great idea! We'll get started right away.",
    "spam": true,
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to all ideas portal users",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Update an idea comment's visibility

**PUT** `/api/v1/idea_comments/:id`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `id` () - **Required** - Numeric ID of the idea comment
- `spam` () - Optional - Whether the comment is considered spam. Must be 'true' or 'false'
- `visibility` () - Optional - Visibility of the idea comment (public, employee_or_creator or employee_or_idea_creator; public is the default). Not for replies, who get their visibility from their parent idea comment instead.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_comments/622085811" -d '{"idea_comment":{"visibility":"employee_or_idea_creator"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "622085811",
    "idea_id": "58056975",
    "body": "This is a great idea! We'll get started right away.",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to idea creator and our employees",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Update a comment

**PUT** `/api/v1/idea_comments/:id`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `id` () - **Required** - Numeric ID of the idea comment
- `body` () - Optional - Body of the idea comment - may include html formatting.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_comments/622085811" -d '{"idea_comment":{"body":"\u003cp\u003eUpdated comment body.\u003c/p\u003e"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_comment": {
    "id": "622085811",
    "idea_id": "58056975",
    "body": "<p>Updated comment body.</p>",
    "created_at": "2019-01-01T00:00:00.000Z",
    "visibility": "Visible to all ideas portal users",
    "parent_idea_comment_id": null,
    "idea_commenter_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
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
    },
    "attachments": []
  }
}
```

---

## Delete an idea comment

**DELETE** `/api/v1/ideas/:idea_id/idea_comments/:id`

### Description
Idea comments can appear in ideas portals.
To reply to an idea_comment, specify the parent_idea_comment_id. Its visibility
will come from its parent idea comment and cannot be overridden.



### Parameters
- `id` () - **Required** - Numeric ID of the idea comment

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/%3Aidea_id/idea_comments/622085811" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
