# Custom fields

## List all custom fields

**GET** `/api/v1/custom_field_definitions`

### Description
Custom fields are defined by record type, and are shared
across all workspaces across the account. Fields must be
added to a layout before they will appear on a record.

For custom fields that include options, (e.g. tags, choice
lists), you can also load the list of all available options.


### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/custom_field_definitions" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "custom_field_definitions": [
    {
      "name": "Priority",
      "id": "581360680",
      "key": "priority",
      "type": "CustomFieldDefinitions::SelectConstant",
      "custom_fieldable_type": "Feature",
      "internal_name": null
    }
  ]
}
```

---

## List options for a custom field

**GET** `/api/v1/custom_field_definitions/:custom_field_definition_id/options`

### Description
Custom fields are defined by record type, and are shared
across all workspaces across the account. Fields must be
added to a layout before they will appear on a record.

For custom fields that include options, (e.g. tags, choice
lists), you can also load the list of all available options.


### Parameters
- `custom_field_definition_id` () - **Required** - Numeric ID of the custom field

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/custom_field_definitions/581360680/options" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "options": [
    {
      "text": "P1",
      "value": "486420793",
      "meta": {
        "color": "#666666"
      }
    },
    {
      "text": "P2",
      "value": "100098181",
      "meta": {
        "color": "#666666"
      }
    },
    {
      "text": "P3",
      "value": "854609942",
      "meta": {
        "color": "#666666"
      }
    },
    {
      "text": "P4",
      "value": "747947447",
      "meta": {
        "color": "#666666"
      }
    },
    {
      "text": "P5",
      "value": "462681378",
      "meta": {
        "color": "#666666"
      }
    }
  ]
}
```

---
