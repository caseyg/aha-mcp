# Release phases

## List release phases for a release

**GET** `/api/v1/releases/:id/release_phases`

### Parameters
- `id` () - **Required** - Numeric ID or key of the release
- `type` () - Optional - Limit to either release milestones or release phases. Options are `milestone` or `phase`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/releases/278327321/release_phases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phases": [
    {
      "id": "20526005",
      "name": "Alpha",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "phase",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "243384959",
        "body": "Description of release phase 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "405824017",
      "name": "Beta",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "milestone",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "965145324",
        "body": "Description of release phase 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "792154778",
      "name": "Beta [2]",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "milestone",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "6776757454432882880",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "827574075",
      "name": "Gamma",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "milestone",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "6776757454435380800",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
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

## Get a specific release phase

**GET** `/api/v1/release_phases/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the release phase

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/release_phases/20526005" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phase": {
    "id": "20526005",
    "name": "Alpha",
    "start_on": "2019-01-01",
    "end_on": "2019-01-01",
    "type": "phase",
    "release_id": 278327321,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "description": {
      "id": "243384959",
      "body": "Description of release phase 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    }
  }
}
```

---

## List release phases in the account

**GET** `/api/v1/release_phases`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/release_phases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phases": [
    {
      "id": "20526005",
      "name": "Alpha",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "phase",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "243384959",
        "body": "Description of release phase 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "405824017",
      "name": "Beta",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "milestone",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "965145324",
        "body": "Description of release phase 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "792154778",
      "name": "Beta [2]",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "milestone",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "6776757454437087046",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    {
      "id": "827574075",
      "name": "Gamma",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "milestone",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "6776757454431607832",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
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

## Create a release phase

**POST** `/api/v1/release_phases`

### Parameters
- `name` () - **Required** - Name of the release phase
- `release_id` () - **Required** - ID of the release to which the new release phase belongs
- `phase_type` () - **Required** - Type of phase, either 'phase' or 'milestone'
- `start_on` () - Optional - Start date of the release phase in format YYYY-MM-DD
- `end_on` () - Optional - End date of the release phase in format YYYY-MM-DD
- `description` () - Optional - Description of the release phase — may include HTML formatting.
- `progress_source` () - Optional - Source for calculating progress on the release phase. Options are: progress_manual, progress_from_features, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the release phase. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end on dates. Options are: duration_manual, duration_from_features.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases" -d '{"release_phase":{"name":"New release phase","phase_type":"phase","release_id":278327321,"start_on":"2019-01-01","end_on":"2019-01-01","description":"\u003cp\u003eThis is the description\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phase": {
    "id": "6776757454428716355",
    "name": "New release phase",
    "start_on": "2019-01-01",
    "end_on": "2019-01-01",
    "type": "phase",
    "release_id": 278327321,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": 0,
    "progress_source": "progress_from_todos",
    "duration_source": "duration_manual",
    "description": {
      "id": "6776757454426617099",
      "body": "<p>This is the description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    }
  }
}
```

---

## Create a release milestone

**POST** `/api/v1/release_phases`

### Parameters
- `name` () - **Required** - Name of the release phase
- `release_id` () - **Required** - ID of the release to which the new release phase belongs
- `phase_type` () - **Required** - Type of phase, either 'phase' or 'milestone'
- `start_on` () - Optional - Start date of the release phase in format YYYY-MM-DD
- `end_on` () - Optional - End date of the release phase in format YYYY-MM-DD
- `description` () - Optional - Description of the release phase — may include HTML formatting.
- `progress_source` () - Optional - Source for calculating progress on the release phase. Options are: progress_manual, progress_from_features, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the release phase. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end on dates. Options are: duration_manual, duration_from_features.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases" -d '{"release_phase":{"name":"New release milestone","phase_type":"milestone","release_id":278327321,"start_on":"2019-01-01","description":"\u003cp\u003eThis is the description\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phase": {
    "id": "6776757454435355688",
    "name": "New release milestone",
    "start_on": "2019-01-01",
    "end_on": "2019-01-01",
    "type": "milestone",
    "release_id": 278327321,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": 0,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "description": {
      "id": "6776757454431800568",
      "body": "<p>This is the description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    }
  }
}
```

---

## Update a release phase

**PUT** `/api/v1/release_phases/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the release phase
- `name` () - Optional - Name of the release phase
- `phase_type` () - **Required** - Type of phase, either 'phase' or 'milestone'
- `start_on` () - Optional - Start date of the release phase in format YYYY-MM-DD
- `end_on` () - Optional - End date of the release phase in format YYYY-MM-DD
- `description` () - Optional - Description of the release phase — may include HTML formatting.
- `progress_source` () - Optional - Source for calculating progress on the release phase. Options are: progress_manual, progress_from_features, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the release phase. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end on dates. Options are: duration_manual, duration_from_features.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases/20526005" -d '{"release_phase":{"name":"Another name","description":"\u003cp\u003enew description\u003c/p\u003e","phase_type":"milestone"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phase": {
    "id": "20526005",
    "name": "Another name",
    "start_on": "2019-01-01",
    "end_on": "2019-01-01",
    "type": "milestone",
    "release_id": 278327321,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "description": {
      "id": "243384959",
      "body": "<p>new description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    }
  }
}
```

---

## Update a release phase's progress source

**PUT** `/api/v1/release_phases/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the release phase
- `name` () - Optional - Name of the release phase
- `phase_type` () - **Required** - Type of phase, either 'phase' or 'milestone'
- `start_on` () - Optional - Start date of the release phase in format YYYY-MM-DD
- `end_on` () - Optional - End date of the release phase in format YYYY-MM-DD
- `description` () - Optional - Description of the release phase — may include HTML formatting.
- `progress_source` () - Optional - Source for calculating progress on the release phase. Options are: progress_manual, progress_from_features, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the release phase. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end on dates. Options are: duration_manual, duration_from_features.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases/20526005" -d '{"release_phase":{"progress_source":"progress_from_features"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phase": {
    "id": "20526005",
    "name": "Alpha",
    "start_on": "2019-01-01",
    "end_on": "2019-01-01",
    "type": "phase",
    "release_id": 278327321,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": 0,
    "progress_source": "progress_from_features",
    "duration_source": "duration_manual",
    "description": {
      "id": "243384959",
      "body": "Description of release phase 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    }
  }
}
```

---

## Update a release phase's progress

**PUT** `/api/v1/release_phases/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the release phase
- `name` () - Optional - Name of the release phase
- `phase_type` () - **Required** - Type of phase, either 'phase' or 'milestone'
- `start_on` () - Optional - Start date of the release phase in format YYYY-MM-DD
- `end_on` () - Optional - End date of the release phase in format YYYY-MM-DD
- `description` () - Optional - Description of the release phase — may include HTML formatting.
- `progress_source` () - Optional - Source for calculating progress on the release phase. Options are: progress_manual, progress_from_features, progress_from_todos, progress_from_features_completed.
- `progress` () - Optional - Progress completed on the release phase. May only be set when the progress_source is manual.
- `duration_source` () - Optional - Source for automatically calculating start and end on dates. Options are: duration_manual, duration_from_features.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases/20526005" -d '{"release_phase":{"progress":25}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release_phase": {
    "id": "20526005",
    "name": "Alpha",
    "start_on": "2019-01-01",
    "end_on": "2019-01-01",
    "type": "phase",
    "release_id": 278327321,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "progress": 25,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "description": {
      "id": "243384959",
      "body": "Description of release phase 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    }
  }
}
```

---

## Delete a release phase

**DELETE** `/api/v1/release_phases/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the release phase

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/release_phases/20526005" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
