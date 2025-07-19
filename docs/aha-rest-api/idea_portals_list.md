# Idea Portals

## List idea portals in a product

**GET** `/api/v1/products/:product_id/idea_portals`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/idea_portals" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_portals": [
    {
      "id": "297813804",
      "title": "Ideas 3",
      "portal_enabled": true,
      "access_type": "public",
      "external_url": "https://testideaportal2.ideas.aha.io:8338/",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "650606523",
      "title": "Ideas 2",
      "portal_enabled": true,
      "access_type": "public",
      "external_url": "https://testideaportal1.ideas.aha.io:8338/",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "1070474755",
      "title": "Ideas 1",
      "portal_enabled": true,
      "access_type": "submit-only",
      "external_url": "https://testideaportal.ideas.aha.io:8338/ideas/new",
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

## List all idea portals in an account

**GET** `/api/v1/idea_portals`

### Parameters
- `page` () - Optional - Page number
- `per_page` () - Optional - Number of records per page

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/idea_portals?page=1&per_page=10" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_portals": [
    {
      "id": "297813804",
      "title": "Ideas 3",
      "portal_enabled": true,
      "access_type": "public",
      "external_url": "https://testideaportal2.ideas.aha.io:8338/",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "650606523",
      "title": "Ideas 2",
      "portal_enabled": true,
      "access_type": "public",
      "external_url": "https://testideaportal1.ideas.aha.io:8338/",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "675900055",
      "title": "portal with 1 endorsement per idea",
      "portal_enabled": true,
      "access_type": "submit-only",
      "external_url": "https://testideaportal3.ideas.aha.io:8338/ideas/new",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "747493361",
      "title": "portal with 2 endorsements per idea",
      "portal_enabled": true,
      "access_type": "submit-only",
      "external_url": "https://testideaportal4.ideas.aha.io:8338/ideas/new",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "1070474755",
      "title": "Ideas 1",
      "portal_enabled": true,
      "access_type": "submit-only",
      "external_url": "https://testideaportal.ideas.aha.io:8338/ideas/new",
      "created_at": "2019-01-01T00:00:00.000Z"
    }
  ],
  "pagination": {
    "total_records": 5,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---
