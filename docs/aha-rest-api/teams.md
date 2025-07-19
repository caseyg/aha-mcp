# Teams

## Create a team

**POST** `/api/v1/teams`

### Parameters
- `name` () - **Required** - Name of the team
- `product_id` () - Optional - Numeric ID or key of the product to assign the team to, or null for an account-level team
- `schedule_id` () - Optional - Schedule to use for this team
- `team_members_count` () - Optional - Number of members on a team
- `capacity` () - Optional - The team's weekly capacity in hours
- `start_date` () - Optional - The start date for the team in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the team in format YYYY-MM-DD
- `hourly_rate` () - Optional - The hourly rate per team member
- `automatically_calculate_team_members_count` () - Optional - Calculate `team_members_count` using existing team members. Set to `false` and supply `team_members_count` to manually update to supplied member count value.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams" -d '{"team":{"name":"Account team"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team": {
    "id": "6776757454430155795",
    "name": "Account team",
    "team_members_count": 0,
    "automatically_calculate_team_members_count": true,
    "capacity": 0,
    "hourly_rate": null,
    "color": "#666666",
    "start_date": null,
    "end_date": null,
    "project": null,
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "custom_fields": []
  }
}
```

---

## Create a team associated with a product

**POST** `/api/v1/products/:product_id/teams`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product to create a team for
- `name` () - **Required** - Name of the team
- `product_id` () - Optional - Numeric ID or key of the product to assign the team to, or null for an account-level team
- `schedule_id` () - Optional - Schedule to use for this team
- `team_members_count` () - Optional - Number of members on a team
- `capacity` () - Optional - The team's weekly capacity in hours
- `start_date` () - Optional - The start date for the team in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the team in format YYYY-MM-DD
- `hourly_rate` () - Optional - The hourly rate per team member
- `automatically_calculate_team_members_count` () - Optional - Calculate `team_members_count` using existing team members. Set to `false` and supply `team_members_count` to manually update to supplied member count value.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/teams" -d '{"team":{"product_id":"PRJ1","name":"Product team"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team": {
    "id": "6776757454431863092",
    "name": "Product team",
    "team_members_count": 0,
    "automatically_calculate_team_members_count": true,
    "capacity": 0,
    "hourly_rate": null,
    "color": "#666666",
    "start_date": null,
    "end_date": null,
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "custom_fields": []
  }
}
```

---

## List teams

**GET** `/api/v1/teams`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/teams?fields=name%2Cteam_members_count%2Cautomatically_calculate_team_members_count%2Ccapacity%2Chourly_rate%2Ccolor%2Cstart_date%2Cend_date%2Cproject%2Cschedule%2Ccustom_fields%2Cteam_members" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "teams": [
    {
      "id": "134558347",
      "name": "Project team",
      "team_members_count": 0,
      "automatically_calculate_team_members_count": false,
      "capacity": "0.0",
      "hourly_rate": "250.0",
      "color": "#666666",
      "start_date": "2019-01-01",
      "end_date": "2019-01-01",
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "workspace_type": "product_workspace"
      },
      "schedule": {
        "id": "441193141",
        "name": "Default schedule",
        "hours_per_day": "8.2",
        "story_points_per_day": "1.0",
        "velocity": "10.5"
      },
      "custom_fields": [],
      "team_members": {
        "id": "730311797",
        "name": "Peter Parker",
        "email": null,
        "user_id": null,
        "virtual": true
      }
    },
    {
      "id": "563889676",
      "name": "Another team",
      "team_members_count": 0,
      "automatically_calculate_team_members_count": false,
      "capacity": "0.0",
      "hourly_rate": "150.0",
      "color": "#666666",
      "start_date": "2019-01-01",
      "end_date": "2019-01-01",
      "project": null,
      "schedule": {
        "id": "441193141",
        "name": "Default schedule",
        "hours_per_day": "8.2",
        "story_points_per_day": "1.0",
        "velocity": "10.5"
      },
      "custom_fields": [],
      "team_members": {
        "id": "960059005",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "user_id": "1020675218",
        "virtual": false
      }
    },
    {
      "id": "949295028",
      "name": "Default team",
      "team_members_count": 5,
      "automatically_calculate_team_members_count": false,
      "capacity": "205.0",
      "hourly_rate": "100.0",
      "color": "#666666",
      "start_date": "2019-01-01",
      "end_date": "2019-01-01",
      "project": null,
      "schedule": {
        "id": "441193141",
        "name": "Default schedule",
        "hours_per_day": "8.2",
        "story_points_per_day": "1.0",
        "velocity": "10.5"
      },
      "custom_fields": [],
      "team_members": {
        "id": "960059005",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "user_id": "1020675218",
        "virtual": false
      }
    }
  ],
  "pagination": {
    "total_records": 3,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List teams in a product

**GET** `/api/v1/products/:product_id/teams`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ3/teams" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "teams": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## Get a specific team

**GET** `/api/v1/teams/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the team

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/teams/949295028" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team": {
    "id": "949295028",
    "name": "Default team",
    "team_members_count": 5,
    "automatically_calculate_team_members_count": false,
    "capacity": "205.0",
    "hourly_rate": "100.0",
    "color": "#666666",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "project": null,
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "custom_fields": [],
    "team_members": {
      "id": "960059005",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "user_id": "1020675218",
      "virtual": false
    }
  }
}
```

---

## Update a team's product

**PUT** `/api/v1/teams/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the team
- `name` () - Optional - Name of the team
- `product_id` () - Optional - Numeric ID or key of the product to assign the team to, or null for an account-level team
- `schedule_id` () - Optional - Schedule to use for this team
- `team_members_count` () - Optional - Number of members on a team
- `capacity` () - Optional - The team's weekly capacity in hours
- `start_date` () - Optional - The start date for the team in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the team in format YYYY-MM-DD
- `hourly_rate` () - Optional - The hourly rate per team member
- `automatically_calculate_team_members_count` () - Optional - Calculate `team_members_count` using existing team members. Set to `false` and supply `team_members_count` to manually update to supplied member count value.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams/134558347" -d '{"team":{"name":"Product 2 team","product_id":"PRJ2"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team": {
    "id": "134558347",
    "name": "Product 2 team",
    "team_members_count": 0,
    "automatically_calculate_team_members_count": false,
    "capacity": "0.0",
    "hourly_rate": "250.0",
    "color": "#666666",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "custom_fields": [],
    "team_members": {
      "id": "730311797",
      "name": "Peter Parker",
      "email": null,
      "user_id": null,
      "virtual": true
    }
  }
}
```

---

## Manually update a team's member count

**PUT** `/api/v1/teams/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the team
- `name` () - Optional - Name of the team
- `product_id` () - Optional - Numeric ID or key of the product to assign the team to, or null for an account-level team
- `schedule_id` () - Optional - Schedule to use for this team
- `team_members_count` () - Optional - Number of members on a team
- `capacity` () - Optional - The team's weekly capacity in hours
- `start_date` () - Optional - The start date for the team in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the team in format YYYY-MM-DD
- `hourly_rate` () - Optional - The hourly rate per team member
- `automatically_calculate_team_members_count` () - Optional - Calculate `team_members_count` using existing team members. Set to `false` and supply `team_members_count` to manually update to supplied member count value.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams/134558347" -d '{"team":{"automatically_calculate_team_members_count":false,"team_members_count":6}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team": {
    "id": "134558347",
    "name": "Project team",
    "team_members_count": 6,
    "automatically_calculate_team_members_count": false,
    "capacity": "246.0",
    "hourly_rate": "250.0",
    "color": "#666666",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "custom_fields": [],
    "team_members": {
      "id": "730311797",
      "name": "Peter Parker",
      "email": null,
      "user_id": null,
      "virtual": true
    }
  }
}
```

---

## Automatically calculate team's member count

**PUT** `/api/v1/teams/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the team
- `name` () - Optional - Name of the team
- `product_id` () - Optional - Numeric ID or key of the product to assign the team to, or null for an account-level team
- `schedule_id` () - Optional - Schedule to use for this team
- `team_members_count` () - Optional - Number of members on a team
- `capacity` () - Optional - The team's weekly capacity in hours
- `start_date` () - Optional - The start date for the team in format YYYY-MM-DD
- `end_date` () - Optional - The end date for the team in format YYYY-MM-DD
- `hourly_rate` () - Optional - The hourly rate per team member
- `automatically_calculate_team_members_count` () - Optional - Calculate `team_members_count` using existing team members. Set to `false` and supply `team_members_count` to manually update to supplied member count value.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams/134558347" -d '{"team":{"automatically_calculate_team_members_count":true}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "team": {
    "id": "134558347",
    "name": "Project team",
    "team_members_count": 1,
    "automatically_calculate_team_members_count": true,
    "capacity": "41.0",
    "hourly_rate": "250.0",
    "color": "#666666",
    "start_date": "2019-01-01",
    "end_date": "2019-01-01",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "schedule": {
      "id": "441193141",
      "name": "Default schedule",
      "hours_per_day": "8.2",
      "story_points_per_day": "1.0",
      "velocity": "10.5"
    },
    "custom_fields": [],
    "team_members": {
      "id": "730311797",
      "name": "Peter Parker",
      "email": null,
      "user_id": null,
      "virtual": true
    }
  }
}
```

---

## Delete a team

**DELETE** `/api/v1/teams/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the team

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/teams/134558347" -d '{}' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
