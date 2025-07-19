# Idea categories

## List idea categories in a product

**GET** `/api/v1/products/:product_id/idea_categories`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/idea_categories" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea_categories": [
    {
      "id": "251347229",
      "name": "Usability",
      "parent_id": null,
      "project_id": 131414752,
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "552935478",
      "name": "Storage",
      "parent_id": null,
      "project_id": 131414752,
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    {
      "id": "972845454",
      "name": "Hard disk drive",
      "parent_id": 552935478,
      "project_id": 131414752,
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
