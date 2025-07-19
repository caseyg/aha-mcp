# Creative briefs

## Create a creative brief

**POST** `/api/v1/products/:product_id/creative_briefs`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `name` () - **Required** - Name of the creative brief
- `color` () - Optional - Hex color of the creative brief in the Aha! UI

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/MW1/creative_briefs" -d '{"creative_brief":{"name":"April launch"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "creative_brief": {
    "id": "6776757454432422291",
    "name": "April launch",
    "color": 13421772,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/creative_briefs/6776757454432422291",
    "resource": "http://company.aha.io/creative_briefs/6776757454432422291",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## List creative briefs in a product

**GET** `/api/v1/products/:product_id/creative_briefs`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against creative brief name

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/MW1/creative_briefs" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "creative_briefs": [
    {
      "id": "91171755",
      "name": "May launch",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "476477971",
      "name": "April launch",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "982259096",
      "name": "June launch",
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

## Get a specific creative_brief

**GET** `/api/v1/creative_briefs/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the creative brief

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/creative_briefs/476477971" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "creative_brief": {
    "id": "476477971",
    "name": "April launch",
    "color": 13421772,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/creative_briefs/476477971",
    "resource": "http://company.aha.io/creative_briefs/476477971",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## Update a creative brief

**PUT** `/api/v1/products/:product_id/creative_briefs/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the creative brief
- `name` () - Optional - Name of the creative brief
- `color` () - Optional - Hex color of the creative brief in the Aha! UI

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/MW1/creative_briefs/476477971" -d '{"creative_brief":{"name":"December launch"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "creative_brief": {
    "id": "476477971",
    "name": "December launch",
    "color": 13421772,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "url": "http://company.aha.io/creative_briefs/476477971",
    "resource": "http://company.aha.io/creative_briefs/476477971",
    "custom_fields": [],
    "comments_count": 0
  }
}
```

---

## Delete a creative brief

**DELETE** `/api/v1/products/:product_id/creative_briefs/:id`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `id` () - **Required** - Numeric ID or key of the creative brief

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/MW1/creative_briefs/476477971" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
