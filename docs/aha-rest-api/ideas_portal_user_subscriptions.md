# Ideas portal user subscriptions

## List a portal user's preferences for the portal summary email

**GET** `/api/v1/idea_portals/:idea_portal_id/portal_users/:portal_user_id/portal_user_subscriptions`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `portal_user_id` () - **Required** - Numeric ID of the portal user

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926/portal_user_subscriptions" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user_subscriptions": {
    "preferences": [
      {
        "type": "project",
        "id": 131414752
      },
      {
        "type": "category",
        "id": 251347229
      }
    ]
  }
}
```

---

## Set a portal user's preferences to specific project and category updates

**POST** `/api/v1/idea_portals/:idea_portal_id/portal_users/:portal_user_id/portal_user_subscriptions`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `portal_user_id` () - **Required** - Numeric ID of the portal user
- `preferences` () - **Required** - An array of preferences for the weekly summary email

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926/portal_user_subscriptions" -d '{"portal_user_subscriptions":{"preferences":[{"type":"project","id":131414752},{"type":"category","id":251347229}]}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user_subscriptions": {
    "preferences": [
      {
        "type": "project",
        "id": 131414752
      },
      {
        "type": "category",
        "id": 251347229
      }
    ]
  }
}
```

---

## Set a portal user's preferences to specific categories

**POST** `/api/v1/idea_portals/:idea_portal_id/portal_users/:portal_user_id/portal_user_subscriptions`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `portal_user_id` () - **Required** - Numeric ID of the portal user
- `preferences` () - **Required** - An array of preferences for the weekly summary email

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926/portal_user_subscriptions" -d '{"portal_user_subscriptions":{"preferences":[{"type":"category","id":251347229},{"type":"category","id":552935478}]}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "portal_user_subscriptions": {
    "preferences": [
      {
        "type": "category",
        "id": 251347229
      },
      {
        "type": "category",
        "id": 552935478
      }
    ]
  }
}
```

---

## Subscribe a portal user to updates from all projects and categories

**POST** `/api/v1/idea_portals/:idea_portal_id/portal_users/:portal_user_id/portal_user_subscriptions/subscribe_to_all`

### Parameters
- `idea_portal_id` () - **Required** - Numeric ID or key of the idea portal
- `portal_user_id` () - **Required** - Numeric ID of the portal user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_portals/1070474755/portal_users/646391926/portal_user_subscriptions/subscribe_to_all" -d '' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
