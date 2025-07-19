# Deletions

## List contents of recycle bin

**GET** `/api/v1/deletions`

### Description
The recycle bin contains recently deleted workspaces, teams, and records. It is possible to restore items up to 7 days after they have been deleted.


### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/deletions" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "deletions": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## restore a specific record

**POST** `/api/v1/deletions/:id/restore`

### Description
The recycle bin contains recently deleted workspaces, teams, and records. It is possible to restore items up to 7 days after they have been deleted.


### Parameters
- `id` () - **Required** - Numeric ID of the deletion record

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/deletions/7465370015620243547/restore" -d '' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "deletion": {
    "status": "restore_in_progress",
    "record": {
      "name": "Feature 1",
      "type": "Feature"
    },
    "deleted_by": {
      "id": 1049303076,
      "name": "George Gently",
      "email": "no-reply@aha.io"
    },
    "id": "6776757454439573883",
    "deleted_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---
