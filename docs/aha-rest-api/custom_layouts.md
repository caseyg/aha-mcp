# Custom Layouts

## List all custom layouts

**GET** `/api/v1/screen_definitions`

### Description
Custom layouts in Aha! Roadmaps help you define the information that you want your teammates to see at two important times: when they create a record and when they view a record's details. You must be a configuration administrator to view custom layouts on your account through the API.

For more information about custom layouts, consult our support documentation: https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-layouts


### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/screen_definitions?page=1&per_page=50" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "screen_definitions": [
    {
      "id": 19837977,
      "screenable_type": "Feature",
      "name": "Screen Definition 6",
      "custom_field_definitions": [
        {
          "id": 839883647,
          "key": "custom_scorecard_definition",
          "position": 3,
          "name": "Some custom scorecard definition",
          "type": "CustomFieldDefinitions::ScorecardField",
          "api_type": "scorecard",
          "required": false
        },
        {
          "id": 182007396,
          "key": "custom_table",
          "position": 7,
          "name": "Custom Table",
          "type": "CustomFieldDefinitions::LinkMasterDetail",
          "api_type": "array",
          "required": false
        },
        {
          "id": 20549131,
          "key": "customer",
          "position": 2,
          "name": "Customer",
          "type": "CustomFieldDefinitions::SelectEditable",
          "api_type": "string",
          "configuration_display": null,
          "required": false,
          "options": [
            {
              "id": 106870231,
              "label": "cust1"
            },
            {
              "id": 525853807,
              "label": "cust2"
            },
            {
              "id": 676386040,
              "label": "cust3"
            }
          ]
        },
        {
          "id": 141558949,
          "key": "customers_table",
          "position": 1,
          "name": "Customers for custom table",
          "type": "CustomFieldDefinitions::LinkMany",
          "api_type": "array",
          "required": false
        },
        {
          "id": 384804762,
          "key": "product_managers",
          "position": 7,
          "name": "Product Managers",
          "type": "CustomFieldDefinitions::Records::UsersField",
          "api_type": "array",
          "required": false
        }
      ]
    },
    {
      "id": 26499634,
      "screenable_type": "Page",
      "name": "Screen Definition 7",
      "custom_field_definitions": [
        {
          "id": 529933329,
          "key": "review_date",
          "position": 1,
          "name": "Review date",
          "type": "CustomFieldDefinitions::DateField",
          "api_type": "date",
          "required": false
        }
      ]
    },
    {
      "id": 105082880,
      "screenable_type": "Project",
      "name": "Screen Definition 2",
      "custom_field_definitions": []
    },
    {
      "id": 117022249,
      "screenable_type": "StrategicImperative",
      "name": "Screen Definition 13",
      "custom_field_definitions": []
    },
    {
      "id": 202819082,
      "screenable_type": "Feature",
      "name": "Screen Definition Feature 2",
      "custom_field_definitions": []
    },
    {
      "id": 405267877,
      "screenable_type": "Ideas::Idea",
      "name": "Screen Definition 5",
      "custom_field_definitions": [
        {
          "id": 711072024,
          "key": "customers_table",
          "position": 1,
          "name": "Customers for custom table",
          "type": "CustomFieldDefinitions::LinkMany",
          "api_type": "array",
          "required": false
        }
      ]
    },
    {
      "id": 412945294,
      "screenable_type": null,
      "name": "Screen Definition 14 - Idea with attachment custom field",
      "custom_field_definitions": []
    },
    {
      "id": 524951996,
      "screenable_type": "Project",
      "name": "Screen Definition 1",
      "custom_field_definitions": [
        {
          "id": 807801664,
          "key": "name",
          "position": 1,
          "name": "Name",
          "type": "CustomFieldDefinitions::TextField",
          "api_type": "string",
          "required": false
        },
        {
          "id": 221120583,
          "key": "website",
          "position": 2,
          "name": "Website",
          "type": "CustomFieldDefinitions::UrlField",
          "api_type": "url",
          "required": false
        }
      ]
    },
    {
      "id": 647403809,
      "screenable_type": "Release",
      "name": "Screen Definition 8",
      "custom_field_definitions": [
        {
          "id": 3228193,
          "key": "release_custom_date",
          "position": 1,
          "name": "Release custom date",
          "type": "CustomFieldDefinitions::DateField",
          "api_type": "date",
          "required": false
        }
      ]
    },
    {
      "id": 687341318,
      "screenable_type": "Requirement",
      "name": "Screen Definition 11",
      "custom_field_definitions": [
        {
          "id": 85990596,
          "key": "priority",
          "position": 3,
          "name": "Priority",
          "type": "CustomFieldDefinitions::SelectConstant",
          "api_type": "string",
          "configuration_display": null,
          "required": false,
          "options": [
            {
              "id": 135354995,
              "label": "P4"
            },
            {
              "id": 376819668,
              "label": "P3"
            },
            {
              "id": 561184585,
              "label": "P2"
            },
            {
              "id": 947629821,
              "label": "P1"
            },
            {
              "id": 1058433764,
              "label": "P5"
            }
          ]
        },
        {
          "id": 867049992,
          "key": "requested_by",
          "position": 2,
          "name": "Requested By",
          "type": "CustomFieldDefinitions::TextField",
          "api_type": "string",
          "required": false
        }
      ]
    },
    {
      "id": 790680888,
      "screenable_type": "Ideas::IdeaPortal",
      "name": "Screen Definition 4",
      "custom_field_definitions": [
        {
          "id": 807801664,
          "key": "name",
          "position": 1,
          "name": "Name",
          "type": "CustomFieldDefinitions::TextField",
          "api_type": "string",
          "required": false
        }
      ]
    },
    {
      "id": 798636831,
      "screenable_type": "ReleasePhase",
      "name": "Screen Definition 15 - Release phase custom field",
      "custom_field_definitions": [
        {
          "id": 43847680,
          "key": "text_field",
          "position": 1,
          "name": "TextField1",
          "type": "CustomFieldDefinitions::TextField",
          "api_type": "string",
          "required": false
        }
      ]
    },
    {
      "id": 826556567,
      "screenable_type": "Competitor",
      "name": "Screen Definition 3",
      "custom_field_definitions": []
    },
    {
      "id": 838774462,
      "screenable_type": "Initiative",
      "name": "Screen Definition 12",
      "custom_field_definitions": [
        {
          "id": 250383571,
          "key": "customers",
          "position": 1,
          "name": "Customers",
          "type": "CustomFieldDefinitions::LinkMany",
          "api_type": "array",
          "required": false
        },
        {
          "id": 688549069,
          "key": "initiative_custom_date",
          "position": 3,
          "name": "Initiative custom date",
          "type": "CustomFieldDefinitions::DateField",
          "api_type": "date",
          "required": false
        }
      ]
    },
    {
      "id": 908690576,
      "screenable_type": "Epic",
      "name": "Screen Definition 7",
      "custom_field_definitions": [
        {
          "id": 919440521,
          "key": "epic_custom_date",
          "position": 1,
          "name": "Epic custom date",
          "type": "CustomFieldDefinitions::DateField",
          "api_type": "date",
          "required": false
        }
      ]
    },
    {
      "id": 915630759,
      "screenable_type": "KeyResult",
      "name": "Screen Definition 16 - Key result custom field",
      "custom_field_definitions": [
        {
          "id": 909163750,
          "key": "stretch_goal",
          "position": 1,
          "name": "Stretch goal",
          "type": "CustomFieldDefinitions::TextField",
          "api_type": "string",
          "required": false
        }
      ]
    }
  ]
}
```

---

## Get a custom layout by ID

**GET** `/api/v1/screen_definitions/:id`

### Description
Custom layouts in Aha! Roadmaps help you define the information that you want your teammates to see at two important times: when they create a record and when they view a record's details. You must be a configuration administrator to view custom layouts on your account through the API.

For more information about custom layouts, consult our support documentation: https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-layouts


### Parameters
- `id` () - **Required** - Numeric ID of the custom layout

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/screen_definitions/19837977" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "id": 19837977,
  "screenable_type": "Feature",
  "name": "Screen Definition 6",
  "custom_field_definitions": [
    {
      "id": 839883647,
      "key": "custom_scorecard_definition",
      "position": 3,
      "name": "Some custom scorecard definition",
      "type": "CustomFieldDefinitions::ScorecardField",
      "api_type": "scorecard",
      "required": false
    },
    {
      "id": 182007396,
      "key": "custom_table",
      "position": 7,
      "name": "Custom Table",
      "type": "CustomFieldDefinitions::LinkMasterDetail",
      "api_type": "array",
      "required": false
    },
    {
      "id": 20549131,
      "key": "customer",
      "position": 2,
      "name": "Customer",
      "type": "CustomFieldDefinitions::SelectEditable",
      "api_type": "string",
      "configuration_display": null,
      "required": false,
      "options": [
        {
          "id": 106870231,
          "label": "cust1"
        },
        {
          "id": 525853807,
          "label": "cust2"
        },
        {
          "id": 676386040,
          "label": "cust3"
        }
      ]
    },
    {
      "id": 141558949,
      "key": "customers_table",
      "position": 1,
      "name": "Customers for custom table",
      "type": "CustomFieldDefinitions::LinkMany",
      "api_type": "array",
      "required": false
    },
    {
      "id": 384804762,
      "key": "product_managers",
      "position": 7,
      "name": "Product Managers",
      "type": "CustomFieldDefinitions::Records::UsersField",
      "api_type": "array",
      "required": false
    }
  ]
}
```

---
