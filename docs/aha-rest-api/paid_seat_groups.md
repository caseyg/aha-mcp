# Paid Seat Groups

## List the administered paid seat groups

**GET** `/api/v1/paid_seat_groups`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/paid_seat_groups" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "paid_seat_groups": [
    {
      "id": "572805993",
      "name": "Group 2",
      "administrators": [
        {
          "id": "82352673",
          "name": "Bob Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "capacity": 20,
      "allocated_seats": 2,
      "description": {
        "id": "6776757454430306696",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "992805589",
      "name": "Group 1",
      "administrators": [
        {
          "id": "373433676",
          "name": "Jim Jingles",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "capacity": 21,
      "allocated_seats": 1,
      "description": {
        "id": "6776757454432192622",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    }
  ]
}
```

---

## Updates the paid seat group

**PUT** `/api/v1/paid_seat_groups/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the paid seat group
- `name` () - Optional - Name of the paid seat group
- `capacity` () - Optional - Size of the paid seat group

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/paid_seat_groups/572805993" -d '{"name":"Group 2","capacity":3}' -X PUT \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "id": "572805993",
  "name": "Group 2",
  "administrators": [
    {
      "id": "82352673",
      "name": "Bob Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "capacity": 3,
  "allocated_seats": 2,
  "description": {
    "id": "6776757454434017458",
    "body": "",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "attachments": []
  }
}
```

---

## Adds the user to the paid seat group

**POST** `/api/v1/paid_seat_groups/:id/modify_user`

### Parameters
- `id` () - **Required** - Numeric ID of the paid seat group
- `user_id` () - **Required** - Numeric ID of the user
- `remove` () - Optional - Boolean flag to remove the user from the group

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/paid_seat_groups/572805993/modify_user" -d '{"user_id":82352673,"remove":null}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 27291e2e898a9d85792f8c817adc491018d7176b5cc7d6865571e808055dd73b"
```

**Response:**
```json
{
  "id": "572805993",
  "name": "Group 2",
  "administrators": [
    {
      "id": "82352673",
      "name": "Bob Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "capacity": 20,
  "allocated_seats": 2,
  "description": {
    "id": "6776757454429375519",
    "body": "",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "attachments": []
  }
}
```

---
