# Time tracking events

## Create a time tracking event for a feature with remaining estimate

**POST** `/api/v1/features/:feature_id/time_tracking_events`

### Parameters
- `occurred_on` () - Optional - The timestamp of when the time tracking event occurred on
- `work_done_text` () - Optional - The text representation of how much work was done (e.g. 1d 2h)
- `remaining_estimate_text` () - Optional - The text representation of how much work is left (e.g. 3d 1h)
- `remaining_automatic` () - Optional - Whether or not to automatically calculate the remaining estimate

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/1007868956/time_tracking_events" -d '{"time_tracking_event":{"user_id":689956296,"work_done_text":"1h 30min","remaining_estimate_text":"2h"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "time_tracking_event": {
    "id": "6776757454426247159",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "occurred_on": "2019-01-01",
    "work_done": 90,
    "work_units": 10
  }
}
```

---

## Log work done for a feature that uses story points

**POST** `/api/v1/features/:feature_id/time_tracking_events`

### Parameters
- `occurred_on` () - Optional - The timestamp of when the time tracking event occurred on
- `work_done_text` () - Optional - The text representation of how much work was done (e.g. 1d 2h)
- `remaining_estimate_text` () - Optional - The text representation of how much work is left (e.g. 3d 1h)
- `remaining_automatic` () - Optional - Whether or not to automatically calculate the remaining estimate

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/1007868956/time_tracking_events" -d '{"time_tracking_event":{"user_id":689956296,"work_done_text":"5p","remaining_estimate_text":"20p"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "time_tracking_event": {
    "id": "6776757454429736995",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "occurred_on": "2019-01-01",
    "work_done": 5,
    "work_units": 20
  }
}
```

---

## Create a time tracking event for a requirement

**POST** `/api/v1/requirements/:requirement_id/time_tracking_events`

### Parameters
- `occurred_on` () - Optional - The timestamp of when the time tracking event occurred on
- `work_done_text` () - Optional - The text representation of how much work was done (e.g. 1d 2h)
- `remaining_estimate_text` () - Optional - The text representation of how much work is left (e.g. 3d 1h)
- `remaining_automatic` () - Optional - Whether or not to automatically calculate the remaining estimate

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/483368544/time_tracking_events" -d '{"time_tracking_event":{"user_id":689956296,"work_done_text":"2h"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "time_tracking_event": {
    "id": "6776757454441446857",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "occurred_on": "2019-01-01",
    "work_done": 120,
    "work_units": 10
  }
}
```

---

## Create a time tracking event for an initiative

**POST** `/api/v1/initiatives/:initiative_id/time_tracking_events`

### Parameters
- `occurred_on` () - Optional - The timestamp of when the time tracking event occurred on
- `work_done_text` () - Optional - The text representation of how much work was done (e.g. 1d 2h)
- `remaining_estimate_text` () - Optional - The text representation of how much work is left (e.g. 3d 1h)
- `remaining_automatic` () - Optional - Whether or not to automatically calculate the remaining estimate

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/initiatives/423077122/time_tracking_events" -d '{"time_tracking_event":{"user_id":689956296,"work_done_text":"2h"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "time_tracking_event": {
    "id": "6776757454426238723",
    "user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "occurred_on": "2019-01-01",
    "work_done": 120,
    "work_units": 10
  }
}
```

---

## Delete a time tracking event

**DELETE** `/api/v1/time_tracking_events/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the time tracking event

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/time_tracking_events/447203384" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
