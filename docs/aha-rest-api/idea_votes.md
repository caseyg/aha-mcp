# Idea votes

## Create an idea vote

**POST** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -d '{"idea_endorsement":{"email":"no-reply@aha.io"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454428816669",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": null,
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "6776757454432463935",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "6776757454426866044",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "description": {
      "id": "",
      "body": "",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
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

## Create a proxy vote with idea users (contacts)

**POST** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.
- `idea_organization_id` () - Optional - Numeric ID of the organization. For proxy votes only.
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.
- `link` () - Optional - URL associated with the proxy vote. For proxy votes only.
- `description` () - Optional - Description of the proxy vote. HTML formatting is supported. For proxy votes only.
- `idea_users` () - Optional - Email addresses of idea users (contacts) to associate with the proxy vote. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -d '{"idea_endorsement":{"idea_id":"PRJ1-I-1","idea_users":["user1@example.com","user2@example.com"],"email":"no-reply@aha.io","idea_organization_id":138732915,"value":2,"link":"https://example.com","description":"This is a description"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454441799961",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": "2.0",
    "link": "https://example.com",
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "6776757454425506076",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "6776757454431130988",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "idea_users": [
      {
        "id": "6776757454430677939",
        "first_name": null,
        "last_name": null,
        "email": "user1@example.com"
      },
      {
        "id": "6776757454440632150",
        "first_name": null,
        "last_name": null,
        "email": "user2@example.com"
      }
    ],
    "description": {
      "id": "6776757454428588461",
      "body": "This is a description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
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

## Create a proxy vote

**POST** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.
- `idea_organization_id` () - Optional - Numeric ID of the organization. For proxy votes only.
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.
- `link` () - Optional - URL associated with the proxy vote. For proxy votes only.
- `description` () - Optional - Description of the proxy vote. HTML formatting is supported. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -d '{"idea_endorsement":{"idea_id":"PRJ1-I-1","email":"no-reply@aha.io","idea_organization_id":138732915,"value":2,"link":"https://example.com","description":"This is a description"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454439787737",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": "2.0",
    "link": "https://example.com",
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "6776757454436715758",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "6776757454436266217",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "6776757454435929624",
      "body": "This is a description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
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

## Create a proxy vote with custom fields

**POST** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.
- `idea_organization_id` () - Optional - Numeric ID of the organization. For proxy votes only.
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.
- `link` () - Optional - URL associated with the proxy vote. For proxy votes only.
- `description` () - Optional - Description of the proxy vote. HTML formatting is supported. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -d '{"idea_endorsement":{"idea_id":"PRJ1-I-1","email":"no-reply@aha.io","idea_organization_id":138732915,"value":2,"link":"https://example.com","description":"This is a description","custom_fields":{"vote_priority":"P3"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454431266756",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": "2.0",
    "link": "https://example.com",
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "6776757454437044116",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "6776757454434609981",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "6776757454426583481",
      "body": "This is a description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [
      {
        "id": "6776757454429891194",
        "key": "vote_priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ],
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

## Create a proxy vote created by an Aha! user

**POST** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.
- `idea_organization_id` () - Optional - Numeric ID of the organization. For proxy votes only.
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.
- `link` () - Optional - URL associated with the proxy vote. For proxy votes only.
- `description` () - Optional - Description of the proxy vote. HTML formatting is supported. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -d '{"idea_endorsement":{"idea_id":"PRJ1-I-1","created_by_user":"no-reply@aha.io","idea_organization_id":138732915,"value":2,"link":"https://example.com","description":"This is a description"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454429499423",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": "2.0",
    "link": "https://example.com",
    "weight": 1,
    "endorsed_by_user": {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "6776757454435773750",
      "body": "This is a description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
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

## Create a proxy vote created by the authenticated user

**POST** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.
- `idea_organization_id` () - Optional - Numeric ID of the organization. For proxy votes only.
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.
- `link` () - Optional - URL associated with the proxy vote. For proxy votes only.
- `description` () - Optional - Description of the proxy vote. HTML formatting is supported. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -d '{"idea_endorsement":{"idea_id":"PRJ1-I-1","idea_organization_id":138732915,"value":2,"link":"https://example.com","description":"This is a description"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454427178277",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": "2.0",
    "link": "https://example.com",
    "weight": 1,
    "endorsed_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "6776757454437418910",
      "body": "This is a description",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
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

## Create additional idea votes

**POST** `/api/v1/ideas/:idea_id/endorsements?multiple_endorsements=true`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Additional Information
Create an additional vote for a user who has already voted on the idea. Only permitted for an ideas portal where users are allowed multiple votes on the same idea.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-8/endorsements?multiple_endorsements=true" -d '{"idea_endorsement":{"email":"no-reply@aha.io"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454432152985",
    "idea_id": "140490859",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": null,
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "6776757454439601916",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "6776757454439190938",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "description": {
      "id": "",
      "body": "",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
    "idea": {
      "id": "140490859",
      "reference_num": "PRJ1-I-8",
      "name": "Some idea name 3",
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
        "id": "6776757454436881488",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-8",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-8"
    }
  }
}
```

---

## Create an idea vote for a user, using the vote limits of an idea portal

**POST** `/api/v1/ideas/:idea_id/endorsements?idea_portal_id=:idea_portal_id`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `created_by_user` () - Optional - Email address of Aha! user who created the vote. For create only.
- `email` () - Optional - Email address of portal user who created the vote. For create only.
- `idea_portal_id` () - Optional - Numeric ID of the idea portal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-8/endorsements?idea_portal_id=747493361" -d '{"idea_endorsement":{"email":"no-reply@aha.io","idea_portal_id":747493361}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "6776757454438207884",
    "idea_id": "140490859",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": null,
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "6776757454430575522",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "6776757454432203478",
      "name": "no-reply@aha.io",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "description": {
      "id": "",
      "body": "",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "integration_fields": [],
    "custom_fields": [],
    "idea": {
      "id": "140490859",
      "reference_num": "PRJ1-I-8",
      "name": "Some idea name 3",
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
        "id": "6776757454429760866",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-8",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-8"
    }
  }
}
```

---

## List votes for an account

**GET** `/api/v1/ideas/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `created_before` () - Optional - UTC timestamp (in ISO8601 format). If provided, only votes created before the timestamp will be returned.
- `created_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only votes created after the timestamp will be returned.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only votes updated or created after the timestamp will be returned.
- `proxy` () - Optional - If set to 'true', only returns proxy votes (votes with an associated organization).

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/endorsements" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsements": [
    {
      "id": "53377392",
      "idea_id": "58056975",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "646391926",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "1056507375",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "idea_organization": {
        "id": "138732915",
        "name": "Acme",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/138732915",
        "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
      }
    },
    {
      "id": "260764892",
      "idea_id": "397084149",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "143214937",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "284648642",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "377726308",
      "idea_id": "245519441",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "143214937",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "284648642",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "449162139",
      "idea_id": "849214356",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "646391926",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "1056507375",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "idea_organization": {
        "id": "138732915",
        "name": "Acme",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/138732915",
        "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
      }
    },
    {
      "id": "562337269",
      "idea_id": "140490859",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "143214937",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "284648642",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "1062165688",
      "idea_id": "444379319",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "646391926",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "1056507375",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "id": "1071644760",
      "idea_id": "290908627",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "143214937",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "284648642",
        "name": "Joe Shmo",
        "email": "joe@shmo.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
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

## List votes for an idea

**GET** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `proxy` () - Optional - If set to 'true', only returns proxy votes (votes with an associated organization).

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsements": [
    {
      "id": "53377392",
      "idea_id": "58056975",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "646391926",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "1056507375",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "idea_organization": {
        "id": "138732915",
        "name": "Acme",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/138732915",
        "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
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

## Get all related idea organizations for votes associated with an idea

**GET** `/api/v1/ideas/:idea_id/endorsements`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Additional Information
Use the field "associated_idea_organizations" to get a list of all related idea organizations associated with each vote. This field can also be used when retrieving a single idea endorement.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `fields` () - **Required** - *,associated_idea_organizations

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements?fields=*%2Cassociated_idea_organizations" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsements": [
    {
      "id": "53377392",
      "idea_id": "58056975",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_idea_user": {
        "id": "6776757454431654341",
        "name": "user@example.com",
        "email": "user@example.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "associated_idea_organizations": [
        {
          "id": "138732915",
          "name": "Acme",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/ideas/idea_organizations/138732915",
          "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
        },
        {
          "id": "6776757454437321466",
          "name": "Widgets",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/ideas/idea_organizations/6776757454437321466",
          "resource": "http://company.aha.io/api/v1/idea_organizations/6776757454437321466"
        }
      ],
      "description": {
        "id": "6776757454426309041",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "integration_fields": [
        {
          "id": "975466318",
          "name": "key",
          "value": "JRA-123",
          "integration_id": 204584239,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "custom_fields": [],
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
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific vote for an idea

**GET** `/api/v1/ideas/:idea_id/endorsements/:id`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the idea vote

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements/53377392" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "53377392",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": null,
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "idea_users": [
      {
        "id": "670061655",
        "first_name": "Tim",
        "last_name": "Smith",
        "email": "tim@smith.com"
      },
      {
        "id": "1056507375",
        "first_name": "John",
        "last_name": "Long",
        "email": "john@long.com"
      }
    ],
    "description": {
      "id": "6776757454432751759",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "integration_fields": [
      {
        "id": "975466318",
        "name": "key",
        "value": "JRA-123",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [],
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

## Update an idea vote

**PUT** `/api/v1/ideas/:idea_id/endorsements/:id`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the idea vote
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements/53377392" -d '{"idea_endorsement":{"value":123.45}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "53377392",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": "123.45",
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "",
      "body": "",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "integration_fields": [
      {
        "id": "975466318",
        "name": "key",
        "value": "JRA-123",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [],
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

## Update an idea vote's custom fields

**PUT** `/api/v1/ideas/:idea_id/endorsements/:id`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the idea vote
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements/53377392" -d '{"idea_endorsement":{"custom_fields":{"vote_priority":"P3"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "53377392",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": null,
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "",
      "body": "",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "integration_fields": [
      {
        "id": "975466318",
        "name": "key",
        "value": "JRA-123",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [
      {
        "id": "6776757454434607824",
        "key": "vote_priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ],
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

## Update an idea vote's custom fields with an array value

**PUT** `/api/v1/ideas/:idea_id/endorsements/:id`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the idea vote
- `value` () - Optional - Dollar value of the idea vote, numeric. For proxy votes only.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements/53377392" -d '{"idea_endorsement":{"custom_fields":[{"key":"vote_priority","value":"P3"}]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsement": {
    "id": "53377392",
    "idea_id": "58056975",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "value": null,
    "link": null,
    "weight": 1,
    "endorsed_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "endorsed_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "idea_organization": {
      "id": "138732915",
      "name": "Acme",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/ideas/idea_organizations/138732915",
      "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
    },
    "description": {
      "id": "",
      "body": "",
      "created_at": null,
      "updated_at": null,
      "attachments": []
    },
    "integration_fields": [
      {
        "id": "975466318",
        "name": "key",
        "value": "JRA-123",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [
      {
        "id": "6776757454431731153",
        "key": "vote_priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ],
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

## Delete an idea vote

**DELETE** `/api/v1/ideas/:idea_id/endorsements/:id`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `id` () - **Required** - Numeric ID of the vote

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements/53377392" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## List only proxy votes for an idea

**GET** `/api/v1/ideas/:idea_id/endorsements?proxy=true`

### Description
"Idea votes" in the web interface are referenced as "idea endorsements" from API endpoints.


### Additional Information
Only returns votes that have an associated organization (proxy votes).

### Parameters
- `idea_id` () - **Required** - Numeric ID or key of the idea
- `proxy` () - Optional - If set to 'true', only returns proxy votes (votes with an associated organization).

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1/endorsements?proxy=true" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_endorsements": [
    {
      "id": "53377392",
      "idea_id": "58056975",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_portal_user": {
        "id": "646391926",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "endorsed_by_idea_user": {
        "id": "1056507375",
        "name": "John Long",
        "email": "john@long.com",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      "idea_organization": {
        "id": "138732915",
        "name": "Acme",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/138732915",
        "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
      }
    },
    {
      "id": "6776881149485092993",
      "idea_id": "58056975",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "value": null,
      "link": null,
      "weight": 1,
      "endorsed_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "idea_organization": {
        "id": "138732915",
        "name": "Acme",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/138732915",
        "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
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
