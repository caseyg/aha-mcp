# Competitors

## List competitors in a product

**GET** `/api/v1/products/:product_id/competitors`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against competitor name

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/competitors" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "competitors": [
    {
      "id": "457085224",
      "name": "TrackFast",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "741974453",
      "name": "Road Racer",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "892399625",
      "name": "360 Tracker",
      "created_at": "2019-01-01T00:00:00.000Z"
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

## Get a specific competitor

**GET** `/api/v1/competitors/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the competitor

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/competitors/892399625" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "competitor": {
    "id": "892399625",
    "name": "360 Tracker",
    "color": 29647,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/competitors/892399625",
    "resource": "http://company.aha.io/competitors/892399625",
    "custom_fields": [
      {
        "id": 415795050,
        "key": "revenue",
        "name": "Revenue",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "300.0",
        "type": "number"
      }
    ],
    "comments_count": 1
  }
}
```

---

## Create a competitor

**POST** `/api/v1/products/:product_id/competitors`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the competitor
- `color` () - **Required** - Hex color of the competitor in the Aha! UI

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/competitors" -d '{"competitor":{"name":"Plan-a-lot","color":29647}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "competitor": {
    "id": "6776757454432513299",
    "name": "Plan-a-lot",
    "color": 29647,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/competitors/6776757454432513299",
    "resource": "http://company.aha.io/competitors/6776757454432513299",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## Update a competitor

**PUT** `/api/v1/products/:product_id/competitors/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the competitor
- `name` () - Optional - Name of the competitor
- `color` () - Optional - Hex color of the competitor in the Aha! UI

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/competitors/892399625" -d '{"competitor":{"name":"Plan-a-lot"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "competitor": {
    "id": "892399625",
    "name": "Plan-a-lot",
    "color": 29647,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/competitors/892399625",
    "resource": "http://company.aha.io/competitors/892399625",
    "custom_fields": [
      {
        "id": 415795050,
        "key": "revenue",
        "name": "Revenue",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "300.0",
        "type": "number"
      }
    ],
    "comments_count": 1
  }
}
```

---

## Delete a competitor

**DELETE** `/api/v1/products/:product_id/competitors/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the competitor

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/competitors/892399625" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
