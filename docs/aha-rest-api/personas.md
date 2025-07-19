# Personas

## Create a persona

**POST** `/api/v1/products/:product_id/personas`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the persona
- `color` () - Optional - Hex color of the persona in the Aha! UI

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/personas" -d '{"persona":{"name":"John"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "persona": {
    "id": "6776757454425989729",
    "name": "John",
    "color": 13421772,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/personas/6776757454425989729",
    "resource": "http://company.aha.io/personas/6776757454425989729",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## List personas in a product

**GET** `/api/v1/products/:product_id/personas`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against the persona name

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/personas" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "personas": [
    {
      "id": "227222789",
      "name": "Jim the cyclist",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "344093881",
      "name": "Jane the athlete",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "982259096",
      "name": "Tim the repairer",
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

## Get a specific persona

**GET** `/api/v1/personas/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the persona

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/personas/344093881" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "persona": {
    "id": "344093881",
    "name": "Jane the athlete",
    "color": 13421772,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/personas/344093881",
    "resource": "http://company.aha.io/personas/344093881",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## Update a persona

**PUT** `/api/v1/products/:product_id/personas/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the persona
- `name` () - Optional - Name of the persona
- `color` () - Optional - Hex color of the persona in the Aha! UI

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/personas/344093881" -d '{"persona":{"name":"Julie"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "persona": {
    "id": "344093881",
    "name": "Julie",
    "color": 13421772,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/personas/344093881",
    "resource": "http://company.aha.io/personas/344093881",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## Delete a persona

**DELETE** `/api/v1/products/:product_id/personas/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID of the persona

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/personas/344093881" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
