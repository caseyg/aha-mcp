# Schedulable changes

## Create a schedulable change

**POST** `/api/v1/schedulable_changes`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/schedulable_changes" -d '{"schedulable_change":{"effective_start_date":"2019-01-01","schedule_id":54870801,"team_member_count":4,"hourly_rate":155.0},"team_id":949295028}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "schedulable_change": {
    "id": "6776757454430597442",
    "effective_start_date": "2019-01-01",
    "team_members_count": 5,
    "hourly_rate": "155.0",
    "color": 6710886,
    "schedule": {
      "id": "54870801",
      "name": "Another schedule",
      "hours_per_day": "10.0",
      "story_points_per_day": "5.0",
      "velocity": "10.0"
    },
    "team_memberships": [
      {
        "id": "202266373",
        "name": "John Johnson",
        "new_user": false,
        "deleted": null,
        "schedule": {
          "id": "441193141",
          "name": "Default schedule",
          "hours_per_day": "8.2",
          "story_points_per_day": "1.0",
          "velocity": "10.5",
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": false,
          "sunday": false
        }
      },
      {
        "id": "646482528",
        "name": "Mary Humpty",
        "new_user": false,
        "deleted": null,
        "schedule": {
          "id": "441193141",
          "name": "Default schedule",
          "hours_per_day": "8.2",
          "story_points_per_day": "1.0",
          "velocity": "10.5",
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": false,
          "sunday": false
        }
      }
    ]
  }
}
```

---

## List schedulable changes

**GET** `/api/v1/schedulable_changes`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/schedulable_changes" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "schedulable_changes": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## Update a schedulable change

**PUT** `/api/v1/schedulable_changes/:id`

### Parameters
- `team_id` () - **Required** - The team to make changes to
- `effective_start_date` () - **Required** - Date the change should be applied, must be in the future, YYYY-MM-DD format
- `schedule_id` () - Optional - The ID of a new schedule to change to
- `team_members_count` () - Optional - The number of team members. Passing null with use automatic calculation
- `hourly_rate` () - Optional - Hourly rate to change to
- `color` () - Optional - Color in the format of #ff0000

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/schedulable_changes/711001786" -d '{"team_id":949295028,"schedulable_change":{"effective_start_date":"2019-01-01","schedule_id":54870801,"team_members_count":4,"hourly_rate":155.0,"color":"#ff0000"}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "schedulable_change": {
    "id": "711001786",
    "effective_start_date": "2019-01-01",
    "team_members_count": 4,
    "hourly_rate": "155.0",
    "color": 16711680,
    "schedule": {
      "id": "54870801",
      "name": "Another schedule",
      "hours_per_day": "10.0",
      "story_points_per_day": "5.0",
      "velocity": "10.0"
    },
    "team_memberships": [
      {
        "id": "202266373",
        "name": "John Johnson",
        "new_user": false,
        "deleted": null,
        "schedule": {
          "id": "441193141",
          "name": "Default schedule",
          "hours_per_day": "8.2",
          "story_points_per_day": "1.0",
          "velocity": "10.5",
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": false,
          "sunday": false
        }
      },
      {
        "id": "646482528",
        "name": "Mary Humpty",
        "new_user": false,
        "deleted": null,
        "schedule": {
          "id": "441193141",
          "name": "Default schedule",
          "hours_per_day": "8.2",
          "story_points_per_day": "1.0",
          "velocity": "10.5",
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": false,
          "sunday": false
        }
      }
    ]
  }
}
```

---

## Update a scheduled change's team memberships

**PUT** `/api/v1/schedulable_changes/:schedulable_change_id/update_team_memberships`

### Description
Adds, updates, or removes users via a scheduled change using the Team Membership relation. The schedulable change must be in the future

### Parameters
- `schedulable_change_id` () - **Required** - ID of the schedulable change to update
- `team_membership_id` () - **Required** - ID of the team membership to schedule a change for
- `deleted` () - Optional - If true will schedule to remove the team membership from the team
- `hours_per_day` () - Optional - Hours per day team member is scheduled
- `story_points_per_day` () - Optional - Story points per day for the team member
- `monday` () - Optional - If user is to be scheduled for monday
- `tuesday` () - Optional - If user is to be scheduled for tuesday
- `wednesday` () - Optional - If user is to be scheduled for wednesday
- `thursday` () - Optional - If user is to be scheduled for thursday
- `friday` () - Optional - If user is to be scheduled for friday
- `staurday` () - Optional - If user is to be scheduled for staurday
- `sunday` () - Optional - If user is to be scheduled for sunday

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/schedulable_changes/711001786/update_team_memberships" -d '{"team_membership_id":202266373,"team_membership":{"schedule":{"hours_per_day":5.0,"story_points_per_day":4.0,"monday":false,"tuesday":true,"wednesday":true,"thursday":true,"friday":false,"saturday":false,"sunday":false}}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "schedulable_change": {
    "id": "711001786",
    "effective_start_date": "2019-01-01",
    "team_members_count": 5,
    "hourly_rate": "100.0",
    "color": 6710886,
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "team_memberships": [
      {
        "id": "202266373",
        "name": "John Johnson",
        "new_user": false,
        "deleted": null,
        "schedule": {
          "id": "441193141",
          "name": "Default schedule",
          "hours_per_day": "8.2",
          "story_points_per_day": "1.0",
          "velocity": "10.5",
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": false,
          "sunday": false
        }
      },
      {
        "id": "646482528",
        "name": "Mary Humpty",
        "new_user": false,
        "deleted": null,
        "schedule": {
          "id": "441193141",
          "name": "Default schedule",
          "hours_per_day": "8.2",
          "story_points_per_day": "1.0",
          "velocity": "10.5",
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": false,
          "sunday": false
        }
      }
    ]
  }
}
```

---

## Delete a schedulable change

**DELETE** `/api/v1/schedulable_changes/:id`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/schedulable_changes/711001786" -d '{}' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
