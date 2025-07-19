# Ideas portal users

## Create a portal user

**POST** `/api/v1/idea_portals/:idea_portal_id/portal_users`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `email` () - **Required** - Email address of the portal user. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the portal user
- `last_name` () - Optional - Last name of the portal user
- `permission` () - Optional - Whether the portal user is an employee/partner. Must be 'true' or 'false'
- `enabled` () - Optional - Whether the portal user is active. Must be 'true' or 'false'
- `max_endorsement_override` () - Optional - The vote allocation for this specific user
- `unsubscribed` () - Optional - Whether the portal user has been unsubscribed from all communications from this portal
- `unsubscribed_from_weekly_emails` () - Optional - Whether the portal user has been unsubscribed from weekly portal summary email

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users" -d '{"portal_user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user": {
    "id": "6776757454436147236",
    "email": "sam.doe@example.com",
    "first_name": "sam",
    "last_name": "doe",
    "enabled": true,
    "verified": false,
    "employee": false,
    "max_endorsements_override": null,
    "idea_user_id": "6776757454428792445",
    "created_at": "2019-01-01T00:00:00.000Z",
    "unsubscribed": false,
    "unsubscribed_from_weekly_emails": null
  }
}
```

---

## Create a portal user with employee permissions

**POST** `/api/v1/idea_portals/:idea_portal_id/portal_users`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `email` () - **Required** - Email address of the portal user. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the portal user
- `last_name` () - Optional - Last name of the portal user
- `permission` () - Optional - Whether the portal user is an employee/partner. Must be 'true' or 'false'
- `enabled` () - Optional - Whether the portal user is active. Must be 'true' or 'false'
- `max_endorsement_override` () - Optional - The vote allocation for this specific user
- `unsubscribed` () - Optional - Whether the portal user has been unsubscribed from all communications from this portal
- `unsubscribed_from_weekly_emails` () - Optional - Whether the portal user has been unsubscribed from weekly portal summary email

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users" -d '{"portal_user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe","permission":"employee"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user": {
    "id": "6776757454438935274",
    "email": "sam.doe@example.com",
    "first_name": "sam",
    "last_name": "doe",
    "enabled": true,
    "verified": false,
    "employee": true,
    "max_endorsements_override": null,
    "idea_user_id": "6776757454433676414",
    "created_at": "2019-01-01T00:00:00.000Z",
    "unsubscribed": false,
    "unsubscribed_from_weekly_emails": null
  }
}
```

---

## List portal users for an ideas portal

**GET** `/api/v1/idea_portals/:idea_portal_id/portal_users`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `email` () - Optional - If provided, returns portal users with an email address matching the given value

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_users": [
    {
      "id": "144817500",
      "email": "timmy@smith.com",
      "first_name": "Timmy",
      "last_name": "Smith",
      "enabled": true,
      "verified": true,
      "employee": true,
      "max_endorsements_override": null,
      "idea_user_id": "446386906",
      "created_at": "2019-01-01T00:00:00.000Z",
      "unsubscribed": false,
      "unsubscribed_from_weekly_emails": null
    },
    {
      "id": "477635308",
      "email": "no-reply@aha.io",
      "first_name": "Bill",
      "last_name": "Billings",
      "enabled": true,
      "verified": false,
      "employee": false,
      "max_endorsements_override": null,
      "idea_user_id": "870840916",
      "created_at": "2019-01-01T00:00:00.000Z",
      "unsubscribed": false,
      "unsubscribed_from_weekly_emails": null
    },
    {
      "id": "646391926",
      "email": "john@long.com",
      "first_name": "John",
      "last_name": "Long",
      "enabled": true,
      "verified": false,
      "employee": false,
      "max_endorsements_override": null,
      "idea_user_id": "1056507375",
      "created_at": "2019-01-01T00:00:00.000Z",
      "unsubscribed": false,
      "unsubscribed_from_weekly_emails": null
    },
    {
      "id": "1066301902",
      "email": "tim@smith.com",
      "first_name": "Tim",
      "last_name": "Smith",
      "enabled": true,
      "verified": false,
      "employee": false,
      "max_endorsements_override": null,
      "idea_user_id": "670061655",
      "created_at": "2019-01-01T00:00:00.000Z",
      "unsubscribed": false,
      "unsubscribed_from_weekly_emails": null
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

## Get a specific portal user

**GET** `/api/v1/idea_portals/:idea_portal_id/portal_users/:id`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID of the idea portal
- `id` () - **Required** - Numeric ID of the portal user

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user": {
    "id": "646391926",
    "email": "john@long.com",
    "first_name": "John",
    "last_name": "Long",
    "enabled": true,
    "verified": false,
    "employee": false,
    "max_endorsements_override": null,
    "idea_user_id": "1056507375",
    "created_at": "2019-01-01T00:00:00.000Z",
    "unsubscribed": false,
    "unsubscribed_from_weekly_emails": null
  }
}
```

---

## Update a portal user

**PUT** `/api/v1/idea_portals/:idea_portal_id/portal_users/:id`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID of the idea portal
- `id` () - **Required** - Numeric ID of the portal user
- `email` () - Optional - Email address of the portal user. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the portal user
- `last_name` () - Optional - Last name of the portal user
- `permission` () - Optional - Whether the portal user is an employee/partner. Must be 'true' or 'false'
- `enabled` () - Optional - Whether the portal user is active. Must be 'true' or 'false'
- `max_endorsement_override` () - Optional - The vote allocation for this specific user
- `unsubscribed` () - Optional - Whether the portal user has been unsubscribed from all communications from this portal
- `unsubscribed_from_weekly_emails` () - Optional - Whether the portal user has been unsubscribed from weekly portal summary email

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926" -d '{"portal_user":{"first_name":"Sarah"}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user": {
    "id": "646391926",
    "email": "john@long.com",
    "first_name": "Sarah",
    "last_name": "Long",
    "enabled": true,
    "verified": false,
    "employee": false,
    "max_endorsements_override": null,
    "idea_user_id": "1056507375",
    "created_at": "2019-01-01T00:00:00.000Z",
    "unsubscribed": false,
    "unsubscribed_from_weekly_emails": null
  }
}
```

---

## Unsubscribe portal user from all communications

**PUT** `/api/v1/idea_portals/:idea_portal_id/portal_users/:id`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID of the idea portal
- `id` () - **Required** - Numeric ID of the portal user
- `email` () - Optional - Email address of the portal user. The email address does not need to be of a user of Aha!
- `first_name` () - Optional - First name of the portal user
- `last_name` () - Optional - Last name of the portal user
- `permission` () - Optional - Whether the portal user is an employee/partner. Must be 'true' or 'false'
- `enabled` () - Optional - Whether the portal user is active. Must be 'true' or 'false'
- `max_endorsement_override` () - Optional - The vote allocation for this specific user
- `unsubscribed` () - Optional - Whether the portal user has been unsubscribed from all communications from this portal
- `unsubscribed_from_weekly_emails` () - Optional - Whether the portal user has been unsubscribed from weekly portal summary email

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926" -d '{"portal_user":{"unsubscribed":true,"unsubscribed_from_weekly_emails":true}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user": {
    "id": "646391926",
    "email": "john@long.com",
    "first_name": "John",
    "last_name": "Long",
    "enabled": true,
    "verified": false,
    "employee": false,
    "max_endorsements_override": null,
    "idea_user_id": "1056507375",
    "created_at": "2019-01-01T00:00:00.000Z",
    "unsubscribed": true,
    "unsubscribed_from_weekly_emails": true
  }
}
```

---

## Delete a portal user

**DELETE** `/api/v1/idea_portals/:idea_portal_id/portal_users/:id`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID of the idea portal
- `id` () - **Required** - Numeric ID or key of the portal user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926" -d '' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
