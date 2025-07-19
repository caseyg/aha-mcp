# Custom field options

## List all custom fields

**GET** `/api/v1/custom_field_definitions/:custom_field_definition_id/custom_field_options`

### Parameters
- `custom_field_definition_id` () - **Required** - Numeric ID of the custom field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/custom_field_definitions/581360680/custom_field_options" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "custom_field_options": [
    {
      "id": "100098181",
      "value": "P2",
      "color": 6710886,
      "hidden": false
    },
    {
      "id": "462681378",
      "value": "P5",
      "color": 6710886,
      "hidden": false
    },
    {
      "id": "486420793",
      "value": "P1",
      "color": 6710886,
      "hidden": false
    },
    {
      "id": "747947447",
      "value": "P4",
      "color": 6710886,
      "hidden": false
    },
    {
      "id": "854609942",
      "value": "P3",
      "color": 6710886,
      "hidden": false
    }
  ]
}
```

---

## Create a custom field option

**POST** `/api/v1/custom_field_definitions/:custom_field_definition_id/custom_field_options`

### Parameters
- `custom_field_definition_id` () - **Required** - Numeric ID of the custom field
- `value` () - **Required** - The value of the custom field option
- `color` () - Optional - Base 10 representation of a hex rgb color. E.g. #666666 is 6710886

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_field_definitions/581360680/custom_field_options" -d '{"custom_field_option":{"value":"New option"}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "id": "6776757454427054555",
  "value": "New option",
  "color": 6710886,
  "hidden": false
}
```

---

## Update a custom field option

**PUT** `/api/v1/custom_field_definitions/:custom_field_definition_id/custom_field_options/:id`

### Parameters
- `custom_field_definition_id` () - **Required** - Numeric ID of the custom field
- `value` () - Optional - The value of the custom field option
- `color` () - Optional - Base 10 representation of a hex rgb color. E.g. #666666 is 6710886
- `hidden` () - Optional - Boolean flag indicating if the option should be hidden

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_field_definitions/581360680/custom_field_options/486420793" -d '{"custom_field_option":{"value":"New option2"}}' -X PUT \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "id": "486420793",
  "value": "New option2",
  "color": 6710886,
  "hidden": false
}
```

---

## Delete a custom field option

**DELETE** `/api/v1/custom_field_definitions/:custom_field_definition_id/custom_field_options/:id`

### Parameters
- `custom_field_definition_id` () - **Required** - Numeric ID of the custom field

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_field_definitions/581360680/custom_field_options/486420793" -d '{}' -X DELETE \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "id": "486420793",
  "value": "P1",
  "color": 6710886,
  "hidden": false
}
```

---
