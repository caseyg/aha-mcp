# Idea users

## Create a idea user

**POST** `/api/v1/idea_users`

### Parameters
- `email` () - **Required** - Email address of the contact. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the contact
- `last_name` () - Optional - Last name of the contact

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_users" -d '{"idea_user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_user": {
    "id": "6776757454431834101",
    "name": "sam doe",
    "email": "sam.doe@example.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "idea_organizations": [],
    "custom_fields": []
  }
}
```

---

## List idea users for an account

**GET** `/api/v1/idea_users`

### Parameters
- `email` () - Optional - If provided, returns idea users with an email address matching the given value
- `idea_portal_id` () - Optional - If provided, returns idea users that are associated with the given idea portal

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_users" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_users": [
    {
      "id": "55650758",
      "name": "Sir Mixalot",
      "email": "spins@example.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [
        {
          "id": "138732915",
          "name": "Acme",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/ideas/idea_organizations/138732915",
          "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
        }
      ],
      "custom_fields": []
    },
    {
      "id": "244576613",
      "name": "Sammy Smith",
      "email": "sammy@smith.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
    },
    {
      "id": "284648642",
      "name": "Joe Shmo",
      "email": "joe@shmo.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
    },
    {
      "id": "446386906",
      "name": "Timmy Smith",
      "email": "timmy@smith.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
    },
    {
      "id": "670061655",
      "name": "Tim Smith",
      "email": "tim@smith.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
    },
    {
      "id": "761219305",
      "name": "Mr Scrooge",
      "email": "lot@example.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [
        {
          "id": "138732915",
          "name": "Acme",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/ideas/idea_organizations/138732915",
          "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
        }
      ],
      "custom_fields": []
    },
    {
      "id": "870840916",
      "name": "Bill Billings",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
    },
    {
      "id": "966050294",
      "name": "John Long",
      "email": "johnvery@long.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
    },
    {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "idea_organizations": [],
      "custom_fields": []
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

## Get a specific idea user

**GET** `/api/v1/idea_users/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the contact

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_users/1056507375" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_user": {
    "id": "1056507375",
    "name": "John Long",
    "email": "john@long.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "idea_organizations": [],
    "custom_fields": [
      {
        "id": "6776757454432472273",
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "the value for the field",
        "type": "string"
      }
    ]
  }
}
```

---

## Update an idea user

**PUT** `/api/v1/idea_users/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the contact
- `idea_organization_ids` () - Optional - Numeric IDs of the idea organizations to associate with the idea user
- `email` () - Optional - Email address of the contact. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the contact
- `last_name` () - Optional - Last name of the contact

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_users/1056507375" -d '{"idea_user":{"first_name":"Sarah"}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_user": {
    "id": "1056507375",
    "name": "Sarah Long",
    "email": "john@long.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "idea_organizations": [],
    "custom_fields": []
  }
}
```

---

## Update an idea user's idea_organizations

**PUT** `/api/v1/idea_users/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the contact
- `idea_organization_ids` () - Optional - Numeric IDs of the idea organizations to associate with the idea user
- `email` () - Optional - Email address of the contact. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the contact
- `last_name` () - Optional - Last name of the contact

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_users/1056507375" -d '{"idea_user":{"idea_organization_ids":[138732915,290305227]}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_user": {
    "id": "1056507375",
    "name": "John Long",
    "email": "john@long.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "idea_organizations": [
      {
        "id": "138732915",
        "name": "Acme",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/138732915",
        "resource": "http://company.aha.io/api/v1/idea_organizations/138732915"
      },
      {
        "id": "290305227",
        "name": "FaceTube",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/ideas/idea_organizations/290305227",
        "resource": "http://company.aha.io/api/v1/idea_organizations/290305227"
      }
    ],
    "custom_fields": []
  }
}
```

---

## Remove an idea user's idea_organizations

**PUT** `/api/v1/idea_users/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the contact
- `idea_organization_ids` () - Optional - Numeric IDs of the idea organizations to associate with the idea user
- `email` () - Optional - Email address of the contact. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the contact
- `last_name` () - Optional - Last name of the contact

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_users/1056507375" -d '{"idea_user":{"idea_organization_ids":[]}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_user": {
    "id": "1056507375",
    "name": "John Long",
    "email": "john@long.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "idea_organizations": [],
    "custom_fields": []
  }
}
```

---

## Delete an idea user

**DELETE** `/api/v1/idea_users/:id`

### Parameters
- `id` () - **Required** - Numeric ID idea user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_users/1056507375" -d '' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
