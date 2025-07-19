# Team members

## Create a virtual user

**POST** `/api/v1/team_members`

### Description
Manage virtual users used in capacity planning

### Parameters
- `first_name` () - **Required** - User's first name
- `last_name` () - **Required** - User's last name
- `email` () - **Required** - User's email address
- `product_id` () - Optional - If present, will create virtual users at this product level, otherwise will create account level virtual users

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/team_members" -d '{"team_member":{"first_name":"Sam","last_name":"Doe","email":"sam.doe@example.com"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team_member": {
    "id": "6776757454436387436",
    "name": "Sam Doe",
    "email": "sam.doe@example.com",
    "user_id": null,
    "virtual": true
  }
}
```

---

## List virtual team members

**GET** `/api/v1/team_members`

### Description
Manage virtual users used in capacity planning

### Parameters
- `product_id` () - Optional - If present, will return virtual users at this product level, otherwise will return account level virtual users

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/team_members" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team_members": [
    {
      "id": "540018633",
      "name": "John Johnson",
      "email": "john.johnson@corporation.com",
      "user_id": null,
      "virtual": true
    },
    {
      "id": "960059005",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "user_id": "1020675218",
      "virtual": false
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

## Delete a virtual team member

**DELETE** `/api/v1/team_members/:id`

### Description
Manage virtual users used in capacity planning

### Parameters
- `id` () - **Required** - Numeric ID of the team member

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/team_members/540018633" -d '{}' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
