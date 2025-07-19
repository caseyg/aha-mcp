# Schedules

## List schedules

**GET** `/api/v1/schedules`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/schedules?fields=name%2Chours_per_day%2Cstory_points_per_day%2Cvelocity%2Cmonday%2Ctuesday%2Cwednesday%2Cthursday%2Cfriday%2Csaturday%2Csunday" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "schedules": [
    {
      "id": "54870801",
      "name": "Another schedule",
      "hours_per_day": "10.0",
      "story_points_per_day": "5.0",
      "velocity": "10.0"
    },
    {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
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
