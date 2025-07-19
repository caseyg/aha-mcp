# Idea subscriptions

## Create an idea subscription

**POST** `/api/v1/ideas/:idea_id/subscriptions`

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `email` () - **Required** - Email address of portal user
- `idea_portal_id` () - Optional - Numeric ID of the ideas portal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/subscriptions" -d '{"idea_subscription":{"email":"username@example.com"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_subscription": {
    "id": "6776757454426628301",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "portal_user": {
      "id": "6776757454433537771",
      "name": "username@example.com",
      "email": "username@example.com",
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
    }
  }
}
```

---

## Create an idea subscription in a specific portal

**POST** `/api/v1/ideas/:idea_id/subscriptions`

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `email` () - **Required** - Email address of portal user
- `idea_portal_id` () - Optional - Numeric ID of the ideas portal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/subscriptions" -d '{"idea_subscription":{"email":"username@example.com","idea_portal_id":"6776757454426957806"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_subscription": {
    "id": "6776757454441657911",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "portal_user": {
      "id": "6776757454432116223",
      "name": "username@example.com",
      "email": "username@example.com",
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
    }
  }
}
```

---

## List subscriptions for an idea

**GET** `/api/v1/ideas/:idea_id/subscriptions`

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/subscriptions" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_subscriptions": [
    {
      "id": "783147498",
      "idea_id": "58056975",
      "created_at": "2019-01-01T00:00:00.000Z",
      "portal_user": {
        "id": "646391926",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
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

## Get a specific subscription for an idea

**GET** `/api/v1/ideas/:idea_id/subscriptions/:id`

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the idea subscription

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/subscriptions/783147498" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_subscription": {
    "id": "783147498",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "portal_user": {
      "id": "646391926",
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
    }
  }
}
```

---

## Delete an idea subscription

**DELETE** `/api/v1/ideas/:idea_id/subscriptions/:id`

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the subscription

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/subscriptions/783147498" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
