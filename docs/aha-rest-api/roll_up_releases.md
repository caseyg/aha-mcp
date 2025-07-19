# Roll up releases

## Get a specific roll up release

**GET** `/api/v1/roll_up_releases/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the roll up release

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/roll_up_releases/PRJ1-MR-1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "roll_up_release": {
    "id": "292454904",
    "reference_num": "PRJ1-MR-1",
    "name": "Roll-up Release 1",
    "start_date": "2019-01-01",
    "release_date": "2019-01-01",
    "created_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/master_releases/PRJ1-MR-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-1"
  }
}
```

---

## List roll up releases in a product

**GET** `/api/v1/products/:product_id/roll_up_releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/610602692/roll_up_releases" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "roll_up_releases": [
    {
      "id": "6776757454427719099",
      "reference_num": "PL1-R-3",
      "name": "My release 002",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/master_releases/PL1-R-3",
      "resource": "http://company.aha.io/api/v1/releases/PL1-R-3"
    },
    {
      "id": "6776757454431689333",
      "reference_num": "PL1-R-2",
      "name": "My release 001",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/master_releases/PL1-R-2",
      "resource": "http://company.aha.io/api/v1/releases/PL1-R-2"
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

## Creates a roll up release

**POST** `/api/v1/products/:product_id/roll_up_releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PL1/roll_up_releases" -d '{"roll_up_release":{"name":"Roll up release","theme":"A roll up release","release_date":"2019-01-01"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "roll_up_release": {
    "id": "6776757454432725447",
    "reference_num": "PL1-R-2",
    "name": "Roll up release",
    "start_date": "2019-01-01",
    "release_date": "2019-01-01",
    "created_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/master_releases/PL1-R-2",
    "resource": "http://company.aha.io/api/v1/releases/PL1-R-2"
  }
}
```

---

## Create a project with a roll up release

**POST** `/api/v1/products/:product_id/roll_up_releases`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PL1/roll_up_releases" -d '{"roll_up_release":{"name":"Roll up release","project_ids":["PRJ2"]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "roll_up_release": {
    "id": "6776757454432792134",
    "reference_num": "PL1-R-2",
    "name": "Roll up release",
    "start_date": "2019-01-01",
    "release_date": "2019-01-01",
    "created_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/master_releases/PL1-R-2",
    "resource": "http://company.aha.io/api/v1/releases/PL1-R-2"
  }
}
```

---

## Update a roll up release

**PUT** `/api/v1/roll_up_releases/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the roll up release

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/roll_up_releases/PRJ1-MR-1" -d '{"roll_up_release":{"name":"Different release"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "roll_up_release": {
    "id": "292454904",
    "reference_num": "PRJ1-MR-1",
    "name": "Different release",
    "start_date": "2019-01-01",
    "release_date": "2019-01-01",
    "created_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/master_releases/PRJ1-MR-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-1"
  }
}
```

---

## Add a project to a roll up release

**PUT** `/api/v1/roll_up_releases/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the roll up release

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/roll_up_releases/PRJ1-MR-1" -d '{"roll_up_release":{"project_ids":["PRJ2"]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "roll_up_release": {
    "id": "292454904",
    "reference_num": "PRJ1-MR-1",
    "name": "Roll-up Release 1",
    "start_date": "2019-01-01",
    "release_date": "2019-01-01",
    "created_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/master_releases/PRJ1-MR-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-MR-1"
  }
}
```

---
