# Products

## Create a product

**POST** `/api/v1/products`

### Parameters
- `name` () - **Required** - Name of the product
- `reference_prefix` () - **Required** - Give the product an abbreviation. It will be used as a prefix on all features for this product.
- `description` () - Optional - Description of the product — may include HTML formatting.
- `parent_id` () - Optional - Numeric ID or prefix of product line to be parent of the new product. The product line must already exist.
- `workspace_type` () - Optional - Type of workspace. (e.g. "product_workspace", "it_workspace")
- `product_line` () - Optional - true
- `product_line_type` () - Optional - Required if creating a product line
- `configuration_epics_enabled` () - Optional - Whether epics are enabled for this product. Must be `true`, `false`, an empty string ""
- `configuration_okrs_enabled` () - Optional - Whether objectives and key results are enabled for this product. Must be `true`, `false`, an empty string ""
- `configuration_default_progress_calculations_inherit` () - Optional - Whether the product should inherit the default progress calculations from the parent product. Must be `true`, or `false`
- `configuration_default_progress_calculations_strategic_imperatives` () - Optional - What the default progress calculations should be set to for goals. Must be `progress_manual`, `progress_from_features`, `progress_from_releases`, `progress_from_initiatives`, `progress_from_descendants`, `progress_from_features_completed`, `progress_from_epics`, or `progress_from_key_results`
- `configuration_default_progress_calculations_key_results` () - Optional - What the default progress calculations should be set to for key results. Must be `progress_manual`, `progress_from_initiatives`, `progress_from_releases`, `progress_from_epics`, `progress_from_features`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_initiatives` () - Optional - What the default progress calculations should be set to for initiatives. Must be `progress_manual`, `progress_from_features`, `progress_from_releases`, `progress_from_children`, `progress_from_features_completed`, or `progress_from_epics`
- `configuration_default_progress_calculations_releases` () - Optional - What the default progress calculations should be set to for releases. Must be `progress_manual`, `progress_from_features`, `progress_from_release_phases`, `progress_from_todos`, `progress_from_remaining_estimate`, `progress_from_features_completed`, or `progress_from_epics`
- `configuration_default_progress_calculations_release_phases` () - Optional - What the default progress calculations should be set to for release phases. Must be `progress_manual`, `progress_from_features`, `progress_from_todos`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_epics` () - Optional - What the default progress calculations should be set to for epics. Must be `progress_manual`, `progress_from_features`, `progress_from_remaining_estimate`, `progress_from_todos`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_features` () - Optional - What the default progress calculations should be set to for features. Must be `progress_manual`, `progress_from_requirements`, `progress_from_remaining_estimate`, or `progress_from_todos`
- `configuration_default_parent_dates_inherit` () - Optional - Whether the product should inherit the default parent dates from the parent product. Must be `true`, or `false`
- `configuration_default_parent_dates_initiatives` () - Optional - What the default parent dates should be set to for initiatives. Must be `duration_manual`, `duration_from_children`, `duration_from_releases`, or `duration_from_features_epics`
- `configuration_default_parent_dates_releases` () - Optional - What the default parent dates should be set to for releases. Must be `duration_manual`, `duration_from_release_phases_features`, or `duration_from_sub_releases`
- `configuration_default_parent_dates_master_releases` () - Optional - What the default parent dates should be set to for roll-up releases. Must be `duration_manual`, `duration_from_release_phases_features`, or `duration_from_sub_releases`
- `configuration_default_parent_dates_release_phases` () - Optional - What the default parent dates should be set to for release phases. Must be `duration_manual` and `duration_from_features`
- `configuration_default_parent_dates_epics` () - Optional - What the default parent dates should be set to for epics. Must be `duration_manual` and `duration_from_features`
- `configuration_default_parent_dates_features` () - Optional - What the default parent dates should be set to for features. Must be `duration_manual`, `duration_from_iterations`, or `duration_from_releases`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products" -d '{"product":{"name":"New Product","description":"An amazing new product","prefix":"NEWPRODUCT"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "product": {
    "id": "6776881149496673510",
    "reference_prefix": "NEWPRODUCT",
    "name": "New Product",
    "product_line": false,
    "product_line_type": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "description": {
      "id": "6776881149491007680",
      "body": "An amazing new product",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/projects/NEWPRODUCT",
    "resource": "http://company.aha.io/projects/NEWPRODUCT",
    "children": [],
    "custom_fields": [],
    "screen_definition_ids": {},
    "screen_definitions": [],
    "has_ideas": true,
    "has_master_features": true,
    "has_epics": true,
    "release_workflow": {
      "id": 717623509,
      "name": "Account product release workflow",
      "statusable_type": "Release",
      "workflow_type": "release"
    },
    "requirement_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "requirement"
    },
    "feature_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "feature"
    },
    "initiative_workflow": {
      "id": 61191651,
      "name": "Account initiative workflow",
      "statusable_type": "Initiative",
      "workflow_type": "initiative"
    },
    "epic_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "epic"
    },
    "idea_workflow": {
      "id": 80245244,
      "name": "Account product idea workflow",
      "statusable_type": "Idea",
      "workflow_type": "idea"
    },
    "strategic_imperative_workflow": {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "workflow_type": "strategic_imperative"
    },
    "key_result_workflow": {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "workflow_type": "key_result"
    },
    "capacity_planning_enabled": false,
    "default_capacity_units": 10,
    "enhanced_capacity_planning_enabled": false,
    "workspace_type": "product_workspace"
  }
}
```

---

## List products in the account

**GET** `/api/v1/products`

### Parameters
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only products updated after the timestamp will be returned.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "products": [
    {
      "id": "12123897",
      "reference_prefix": "PRJ5",
      "name": "Project 5",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ5"
    },
    {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    {
      "id": "174813163",
      "reference_prefix": "PL3",
      "name": "Product Line 3",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL3"
    },
    {
      "id": "186424834",
      "reference_prefix": "MW1",
      "name": "Marketing workspace 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "marketing_workspace",
      "url": "http://company.aha.io/projects/MW1"
    },
    {
      "id": "303419322",
      "reference_prefix": "MW2",
      "name": "Marketing workspace 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "marketing_workspace",
      "url": "http://company.aha.io/projects/MW2"
    },
    {
      "id": "336591436",
      "reference_prefix": "PL4",
      "name": "Product Line 4",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL4"
    },
    {
      "id": "431075141",
      "reference_prefix": "PRJ6",
      "name": "Project 6",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ6"
    },
    {
      "id": "517761884",
      "reference_prefix": "PRJ2",
      "name": "Project 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ2"
    },
    {
      "id": "610602692",
      "reference_prefix": "PL1",
      "name": "Product Line 1",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL1"
    },
    {
      "id": "702241743",
      "reference_prefix": "PRJ3",
      "name": "Project 3",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ3"
    },
    {
      "id": "783720408",
      "reference_prefix": "PRJ7",
      "name": "Project 7",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ7"
    },
    {
      "id": "935317104",
      "reference_prefix": "PRJ4",
      "name": "Project 4",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ4"
    },
    {
      "id": "1030512512",
      "reference_prefix": "PL2",
      "name": "Product Line 2",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL2"
    }
  ],
  "pagination": {
    "total_records": 13,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List products (including Aha! teams in the account)

**GET** `/api/v1/products`

### Parameters
- `include_teams` () - Optional - Set to true to include Aha! teams in the response

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products?include_teams=true" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "products": [
    {
      "id": "12123897",
      "reference_prefix": "PRJ5",
      "name": "Project 5",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ5"
    },
    {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    {
      "id": "174813163",
      "reference_prefix": "PL3",
      "name": "Product Line 3",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL3"
    },
    {
      "id": "186424834",
      "reference_prefix": "MW1",
      "name": "Marketing workspace 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "marketing_workspace",
      "url": "http://company.aha.io/projects/MW1"
    },
    {
      "id": "303419322",
      "reference_prefix": "MW2",
      "name": "Marketing workspace 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "marketing_workspace",
      "url": "http://company.aha.io/projects/MW2"
    },
    {
      "id": "336591436",
      "reference_prefix": "PL4",
      "name": "Product Line 4",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL4"
    },
    {
      "id": "431075141",
      "reference_prefix": "PRJ6",
      "name": "Project 6",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ6"
    },
    {
      "id": "517761884",
      "reference_prefix": "PRJ2",
      "name": "Project 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ2"
    },
    {
      "id": "610602692",
      "reference_prefix": "PL1",
      "name": "Product Line 1",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL1"
    },
    {
      "id": "702241743",
      "reference_prefix": "PRJ3",
      "name": "Project 3",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ3"
    },
    {
      "id": "783720408",
      "reference_prefix": "PRJ7",
      "name": "Project 7",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ7"
    },
    {
      "id": "787060436",
      "reference_prefix": "TEAM",
      "name": "Development Team",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "team",
      "url": "http://company.aha.io/projects/TEAM"
    },
    {
      "id": "935317104",
      "reference_prefix": "PRJ4",
      "name": "Project 4",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ4"
    },
    {
      "id": "1030512512",
      "reference_prefix": "PL2",
      "name": "Product Line 2",
      "product_line": true,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PL2"
    }
  ],
  "pagination": {
    "total_records": 14,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List products with idea portals in the account

**GET** `/api/v1/products`

### Parameters
- `with_idea_portals` () - Optional - Set to true to list only products with idea portals

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products?with_idea_portals=true" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "products": [
    {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    {
      "id": "517761884",
      "reference_prefix": "PRJ2",
      "name": "Project 2",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ2"
    },
    {
      "id": "702241743",
      "reference_prefix": "PRJ3",
      "name": "Project 3",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ3"
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

## Get a specific product

**GET** `/api/v1/products/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the product or product line

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "product": {
    "id": "131414752",
    "reference_prefix": "PRJ1",
    "name": "Project 1",
    "product_line": false,
    "product_line_type": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "description": {
      "id": "21164619",
      "body": "",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/projects/PRJ1",
    "resource": "http://company.aha.io/projects/PRJ1",
    "children": [],
    "custom_fields": [
      {
        "id": 33687638,
        "key": "release_count",
        "name": "Release count",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "6809377296730243716": {
              "value": 6,
              "name": "Release count",
              "display_value": "6.0"
            }
          }
        },
        "type": "equation_sheet"
      }
    ],
    "screen_definition_ids": {
      "Competitor": 826556567,
      "Epic": 908690576,
      "Feature": 19837977,
      "Ideas::Idea": 405267877,
      "Ideas::IdeaPortal": 790680888,
      "Initiative": 838774462,
      "Page": 26499634,
      "Project": 524951996,
      "Release": 647403809,
      "Requirement": 687341318,
      "StrategicImperative": 117022249
    },
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
        "id": 117022249,
        "screenable_type": "StrategicImperative",
        "name": "Screen Definition 13",
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
      }
    ],
    "has_ideas": true,
    "has_master_features": false,
    "has_epics": false,
    "release_workflow": {
      "id": 717623509,
      "name": "Account product release workflow",
      "statusable_type": "Release",
      "workflow_type": "release"
    },
    "requirement_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "requirement"
    },
    "feature_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "feature"
    },
    "initiative_workflow": {
      "id": 61191651,
      "name": "Account initiative workflow",
      "statusable_type": "Initiative",
      "workflow_type": "initiative"
    },
    "epic_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "epic"
    },
    "idea_workflow": {
      "id": 80245244,
      "name": "Account product idea workflow",
      "statusable_type": "Idea",
      "workflow_type": "idea"
    },
    "strategic_imperative_workflow": {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "workflow_type": "strategic_imperative"
    },
    "key_result_workflow": {
      "id": 1024772447,
      "name": "Account product key result workflow",
      "statusable_type": "KeyResult",
      "workflow_type": "key_result"
    },
    "capacity_planning_enabled": false,
    "default_capacity_units": 10,
    "enhanced_capacity_planning_enabled": false,
    "workspace_type": "product_workspace"
  }
}
```

---

## Create a product line

**POST** `/api/v1/products`

### Parameters
- `name` () - Optional - Name of the product
- `reference_prefix` () - Optional - Give the product an abbreviation. It will be used as a prefix on all features for this product.
- `description` () - Optional - Description of the product — may include HTML formatting.
- `parent_id` () - Optional - Numeric ID or prefix of product line to be parent of the new product. The product line must already exist.
- `workspace_type` () - Optional - Type of workspace. (e.g. "product_workspace", "it_workspace")
- `product_line` () - Optional - true
- `product_line_type` () - Optional - Required if creating a product line
- `configuration_epics_enabled` () - Optional - Whether epics are enabled for this product. Must be `true`, `false`, an empty string ""
- `configuration_okrs_enabled` () - Optional - Whether objectives and key results are enabled for this product. Must be `true`, `false`, an empty string ""
- `configuration_default_progress_calculations_inherit` () - Optional - Whether the product should inherit the default progress calculations from the parent product. Must be `true`, or `false`
- `configuration_default_progress_calculations_strategic_imperatives` () - Optional - What the default progress calculations should be set to for goals. Must be `progress_manual`, `progress_from_features`, `progress_from_releases`, `progress_from_initiatives`, `progress_from_descendants`, `progress_from_features_completed`, `progress_from_epics`, or `progress_from_key_results`
- `configuration_default_progress_calculations_key_results` () - Optional - What the default progress calculations should be set to for key results. Must be `progress_manual`, `progress_from_initiatives`, `progress_from_releases`, `progress_from_epics`, `progress_from_features`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_initiatives` () - Optional - What the default progress calculations should be set to for initiatives. Must be `progress_manual`, `progress_from_features`, `progress_from_releases`, `progress_from_children`, `progress_from_features_completed`, or `progress_from_epics`
- `configuration_default_progress_calculations_releases` () - Optional - What the default progress calculations should be set to for releases. Must be `progress_manual`, `progress_from_features`, `progress_from_release_phases`, `progress_from_todos`, `progress_from_remaining_estimate`, `progress_from_features_completed`, or `progress_from_epics`
- `configuration_default_progress_calculations_release_phases` () - Optional - What the default progress calculations should be set to for release phases. Must be `progress_manual`, `progress_from_features`, `progress_from_todos`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_epics` () - Optional - What the default progress calculations should be set to for epics. Must be `progress_manual`, `progress_from_features`, `progress_from_remaining_estimate`, `progress_from_todos`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_features` () - Optional - What the default progress calculations should be set to for features. Must be `progress_manual`, `progress_from_requirements`, `progress_from_remaining_estimate`, or `progress_from_todos`
- `configuration_default_parent_dates_inherit` () - Optional - Whether the product should inherit the default parent dates from the parent product. Must be `true`, or `false`
- `configuration_default_parent_dates_initiatives` () - Optional - What the default parent dates should be set to for initiatives. Must be `duration_manual`, `duration_from_children`, `duration_from_releases`, or `duration_from_features_epics`
- `configuration_default_parent_dates_releases` () - Optional - What the default parent dates should be set to for releases. Must be `duration_manual`, `duration_from_release_phases_features`, or `duration_from_sub_releases`
- `configuration_default_parent_dates_master_releases` () - Optional - What the default parent dates should be set to for roll-up releases. Must be `duration_manual`, `duration_from_release_phases_features`, or `duration_from_sub_releases`
- `configuration_default_parent_dates_release_phases` () - Optional - What the default parent dates should be set to for release phases. Must be `duration_manual` and `duration_from_features`
- `configuration_default_parent_dates_epics` () - Optional - What the default parent dates should be set to for epics. Must be `duration_manual` and `duration_from_features`
- `configuration_default_parent_dates_features` () - Optional - What the default parent dates should be set to for features. Must be `duration_manual`, `duration_from_iterations`, or `duration_from_releases`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products" -d '{"product":{"name":"New Product Line","description":"An amazing new product line","prefix":"NEWPRODUCT","product_line":true,"product_line_type":"a new product line type"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "product": {
    "id": "6776881149497073946",
    "reference_prefix": "NEWPRODUCT",
    "name": "New Product Line",
    "product_line": true,
    "product_line_type": "a new product line type",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "description": {
      "id": "6776881149487303525",
      "body": "An amazing new product line",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/projects/NEWPRODUCT",
    "resource": "http://company.aha.io/projects/NEWPRODUCT",
    "children": [],
    "custom_fields": [],
    "screen_definition_ids": {},
    "screen_definitions": [],
    "has_ideas": false,
    "has_master_features": true,
    "has_epics": true,
    "release_workflow": {
      "id": 717623509,
      "name": "Account product release workflow",
      "statusable_type": "Release",
      "workflow_type": "release"
    },
    "requirement_workflow": {
      "id": 845522269,
      "name": "Example product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "requirement"
    },
    "feature_workflow": {
      "id": 845522269,
      "name": "Example product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "feature"
    },
    "initiative_workflow": {
      "id": 61191651,
      "name": "Account initiative workflow",
      "statusable_type": "Initiative",
      "workflow_type": "initiative"
    },
    "epic_workflow": {
      "id": 845522269,
      "name": "Example product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "epic"
    },
    "idea_workflow": {
      "id": 80245244,
      "name": "Account product idea workflow",
      "statusable_type": "Idea",
      "workflow_type": "idea"
    },
    "strategic_imperative_workflow": {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "workflow_type": "strategic_imperative"
    },
    "key_result_workflow": {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "workflow_type": "key_result"
    },
    "capacity_planning_enabled": false,
    "default_capacity_units": 10,
    "enhanced_capacity_planning_enabled": false,
    "workspace_type": "product_workspace"
  }
}
```

---

## Update a product

**PUT** `/api/v1/products/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the product
- `name` () - Optional - Name of the product
- `reference_prefix` () - Optional - Give the product an abbreviation. It will be used as a prefix on all features for this product.
- `description` () - Optional - Description of the product — may include HTML formatting.
- `parent_id` () - Optional - Numeric ID or prefix of product line to be parent of the new product. The product line must already exist.
- `workspace_type` () - Optional - Type of workspace. (e.g. "product_workspace", "it_workspace")
- `product_line` () - Optional - true
- `product_line_type` () - Optional - Required if creating a product line
- `configuration_epics_enabled` () - Optional - Whether epics are enabled for this product. Must be `true`, `false`, an empty string ""
- `configuration_okrs_enabled` () - Optional - Whether objectives and key results are enabled for this product. Must be `true`, `false`, an empty string ""
- `configuration_default_progress_calculations_inherit` () - Optional - Whether the product should inherit the default progress calculations from the parent product. Must be `true`, or `false`
- `configuration_default_progress_calculations_strategic_imperatives` () - Optional - What the default progress calculations should be set to for goals. Must be `progress_manual`, `progress_from_features`, `progress_from_releases`, `progress_from_initiatives`, `progress_from_descendants`, `progress_from_features_completed`, `progress_from_epics`, or `progress_from_key_results`
- `configuration_default_progress_calculations_key_results` () - Optional - What the default progress calculations should be set to for key results. Must be `progress_manual`, `progress_from_initiatives`, `progress_from_releases`, `progress_from_epics`, `progress_from_features`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_initiatives` () - Optional - What the default progress calculations should be set to for initiatives. Must be `progress_manual`, `progress_from_features`, `progress_from_releases`, `progress_from_children`, `progress_from_features_completed`, or `progress_from_epics`
- `configuration_default_progress_calculations_releases` () - Optional - What the default progress calculations should be set to for releases. Must be `progress_manual`, `progress_from_features`, `progress_from_release_phases`, `progress_from_todos`, `progress_from_remaining_estimate`, `progress_from_features_completed`, or `progress_from_epics`
- `configuration_default_progress_calculations_release_phases` () - Optional - What the default progress calculations should be set to for release phases. Must be `progress_manual`, `progress_from_features`, `progress_from_todos`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_epics` () - Optional - What the default progress calculations should be set to for epics. Must be `progress_manual`, `progress_from_features`, `progress_from_remaining_estimate`, `progress_from_todos`, or `progress_from_features_completed`
- `configuration_default_progress_calculations_features` () - Optional - What the default progress calculations should be set to for features. Must be `progress_manual`, `progress_from_requirements`, `progress_from_remaining_estimate`, or `progress_from_todos`
- `configuration_default_parent_dates_inherit` () - Optional - Whether the product should inherit the default parent dates from the parent product. Must be `true`, or `false`
- `configuration_default_parent_dates_initiatives` () - Optional - What the default parent dates should be set to for initiatives. Must be `duration_manual`, `duration_from_children`, `duration_from_releases`, or `duration_from_features_epics`
- `configuration_default_parent_dates_releases` () - Optional - What the default parent dates should be set to for releases. Must be `duration_manual`, `duration_from_release_phases_features`, or `duration_from_sub_releases`
- `configuration_default_parent_dates_master_releases` () - Optional - What the default parent dates should be set to for roll-up releases. Must be `duration_manual`, `duration_from_release_phases_features`, or `duration_from_sub_releases`
- `configuration_default_parent_dates_release_phases` () - Optional - What the default parent dates should be set to for release phases. Must be `duration_manual` and `duration_from_features`
- `configuration_default_parent_dates_epics` () - Optional - What the default parent dates should be set to for epics. Must be `duration_manual` and `duration_from_features`
- `configuration_default_parent_dates_features` () - Optional - What the default parent dates should be set to for features. Must be `duration_manual`, `duration_from_iterations`, or `duration_from_releases`

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/131414752" -d '{"product":{"name":"Two Products"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "product": {
    "id": "131414752",
    "reference_prefix": "PRJ1",
    "name": "Two Products",
    "product_line": false,
    "product_line_type": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "description": {
      "id": "21164619",
      "body": "",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/projects/PRJ1",
    "resource": "http://company.aha.io/projects/PRJ1",
    "children": [],
    "custom_fields": [
      {
        "id": 33687638,
        "key": "release_count",
        "name": "Release count",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "6809377296730243716": {
              "value": 6,
              "name": "Release count",
              "display_value": "6.0"
            }
          }
        },
        "type": "equation_sheet"
      }
    ],
    "screen_definition_ids": {
      "Competitor": 826556567,
      "Epic": 908690576,
      "Feature": 19837977,
      "Ideas::Idea": 405267877,
      "Ideas::IdeaPortal": 790680888,
      "Initiative": 838774462,
      "Page": 26499634,
      "Project": 524951996,
      "Release": 647403809,
      "Requirement": 687341318,
      "StrategicImperative": 117022249
    },
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
        "id": 117022249,
        "screenable_type": "StrategicImperative",
        "name": "Screen Definition 13",
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
      }
    ],
    "has_ideas": true,
    "has_master_features": false,
    "has_epics": false,
    "release_workflow": {
      "id": 717623509,
      "name": "Account product release workflow",
      "statusable_type": "Release",
      "workflow_type": "release"
    },
    "requirement_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "requirement"
    },
    "feature_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "feature"
    },
    "initiative_workflow": {
      "id": 61191651,
      "name": "Account initiative workflow",
      "statusable_type": "Initiative",
      "workflow_type": "initiative"
    },
    "epic_workflow": {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "workflow_type": "epic"
    },
    "idea_workflow": {
      "id": 80245244,
      "name": "Account product idea workflow",
      "statusable_type": "Idea",
      "workflow_type": "idea"
    },
    "strategic_imperative_workflow": {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "workflow_type": "strategic_imperative"
    },
    "key_result_workflow": {
      "id": 1024772447,
      "name": "Account product key result workflow",
      "statusable_type": "KeyResult",
      "workflow_type": "key_result"
    },
    "capacity_planning_enabled": false,
    "default_capacity_units": 10,
    "enhanced_capacity_planning_enabled": false,
    "workspace_type": "product_workspace"
  }
}
```

---
