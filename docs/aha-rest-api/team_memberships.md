# Team memberships

## Add user to a team

**POST** `/api/v1/teams/:team_id/team_memberships`

### Description
Team memberships for capacity planning teams. Users can be either Aha! users or virtual users

### Parameters
- `team_id` () - **Required** - Team ID
- `user_id` () - Optional - ID of the Aha! user to add to the team. Only one of these or virtual_user_id can be present
- `virtual_user_id` () - Optional - ID of the virtual capacity planning user to add to the team. Only one of these or user_id can be present
- `product_id` () - Optional - When adding virtual users, pass in the product ID the virtual user belongs to. If missing, it's assumed the virtual user is at the account level

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams/949295028/team_memberships" -d '{"team_membership":{"user_id":689956296}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## List team memberships for a team

**GET** `/api/v1/teams/:team_id/team_memberships`

### Description
Team memberships for capacity planning teams. Users can be either Aha! users or virtual users

### Parameters
- `team_id` () - **Required** - Team ID

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/teams/949295028/team_memberships?fields=team_member%2Cteam%2Ccreated_at" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team_memberships": [
    {
      "id": "202266373",
      "team_member": {
        "id": "540018633",
        "name": "John Johnson",
        "email": "john.johnson@corporation.com",
        "user_id": null,
        "virtual": true
      },
      "team": {
        "id": "949295028",
        "name": "Default team"
      },
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "646482528",
      "team_member": {
        "id": "960059005",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "user_id": "1020675218",
        "virtual": false
      },
      "team": {
        "id": "949295028",
        "name": "Default team"
      },
      "created_at": "2019-01-01T00:00:00.000Z"
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

## Remove a user from a team

**DELETE** `/api/v1/teams/:team_id/team_memberships/:id`

### Description
Team memberships for capacity planning teams. Users can be either Aha! users or virtual users

### Parameters
- `team_id` () - **Required** - Team ID
- `id` () - **Required** - Team membership ID

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams/949295028/team_memberships/202266373" -d '{}' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
