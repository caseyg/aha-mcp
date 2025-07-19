# Custom table record links

## Create a custom table record link associated with a product

**PUT** `/api/v1/products/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1" -d '{"product":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
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

## Create a custom table record link associated with a release

**PUT** `/api/v1/releases/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Additional Information
*[Custom Tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.*


### Parameters
- `id` () - **Required** - Numeric ID or key of the release

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/releases/PRJ1-R-1" -d '{"release":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "release": {
    "id": "278327321",
    "product_id": "131414752",
    "reference_num": "PRJ1-R-1",
    "name": "Release 1",
    "start_date": "2019-01-01",
    "end_date": null,
    "development_started_on": "2019-01-01",
    "release_date": "2019-01-01",
    "external_release_date": "2019-01-01",
    "external_release_date_description": "Feb 5, 2025",
    "external_date_resolution": "exact",
    "released": false,
    "parking_lot": false,
    "master_release": false,
    "released_on": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "position": null,
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "status_changed_on": null,
    "theme": {
      "id": "522610666",
      "body": "Theme of the release",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "url": "http://company.aha.io/releases/PRJ1-R-1",
    "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
    "integration_fields": [
      {
        "id": "68217473",
        "name": "id",
        "value": "777",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [
      {
        "id": "432637490",
        "key": "note",
        "name": "Note",
        "updatedAt": "2019-01-01T00:00:00Z",
        "body": "<p>sample text</p>",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": [],
        "value": "<p>sample text</p>",
        "type": "note"
      },
      {
        "id": 424324947,
        "key": "text_field",
        "name": "TextField",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      }
    ],
    "custom_object_links": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      }
    ],
    "comments_count": 1,
    "workflow_status": {
      "id": "738862546",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "owner": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "goals": [
      {
        "id": "602095703",
        "name": "Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
        "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "166463080",
          "body": "Description of goal 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      }
    ],
    "initiatives": [
      {
        "id": "423077122",
        "reference_num": "PRJ1-S-1",
        "name": "Initiative 1",
        "url": "http://company.aha.io/initiatives/PRJ1-S-1",
        "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "673273729",
          "body": "Description of initiative 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "integration_fields": [
          {
            "id": "546711007",
            "name": "id",
            "value": "9913333",
            "integration_id": 186281709,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "966751335",
            "name": "key",
            "value": "JRA-987222",
            "integration_id": 186281709,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ]
      }
    ],
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Create a custom table record link associated with a feature

**PUT** `/api/v1/features/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID or key of the feature

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/features/PRJ1-1" -d '{"feature":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "feature": {
    "id": "1007868956",
    "name": "Feature 1",
    "reference_num": "PRJ1-1",
    "initiative_reference_num": "PRJ1-S-1",
    "release_reference_num": "PRJ1-R-1",
    "epic_reference_num": "PRJ1-E-1",
    "position": 1,
    "score": 3,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "start_date": "2019-01-01",
    "due_date": "2019-01-01",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "status_changed_on": null,
    "created_by_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_kind": {
      "id": "98484309",
      "name": "New"
    },
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "description": {
      "id": "793547626",
      "body": "Body of note 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": [
        {
          "id": "724655692",
          "download_url": "https://company.aha.io/attachments/724655692/token/aaabbbccc7.download?size=original",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "original_file_size": 123,
          "content_type": "text/plain",
          "file_name": "uploaded_file_name.txt",
          "file_size": 123
        }
      ]
    },
    "attachments": [],
    "integration_fields": [
      {
        "id": "92040219",
        "name": "url",
        "value": "https://bigaha.atlassian.net/issues/JRA-123",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "728894778",
        "name": "key",
        "value": "JRA-123",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "846945422",
        "name": "id",
        "value": "435",
        "integration_id": 204584239,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "url": "http://company.aha.io/features/PRJ1-1",
    "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
    "release": {
      "id": "278327321",
      "reference_num": "PRJ1-R-1",
      "name": "Release 1",
      "start_date": "2019-01-01",
      "release_date": "2019-01-01",
      "parking_lot": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "product_id": "131414752",
      "integration_fields": [
        {
          "id": "68217473",
          "name": "id",
          "value": "777",
          "integration_id": 204584239,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ],
      "url": "http://company.aha.io/releases/PRJ1-R-1",
      "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
      "owner": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "project": {
        "id": "131414752",
        "reference_prefix": "PRJ1",
        "name": "Project 1",
        "product_line": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "workspace_type": "product_workspace",
        "url": "http://company.aha.io/projects/PRJ1"
      }
    },
    "master_feature": {
      "id": "999605892",
      "reference_num": "PRJ1-E-1",
      "name": "Epic 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
    },
    "belongs_to_release_phase": {
      "id": "20526005",
      "name": "Alpha",
      "start_on": "2019-01-01",
      "end_on": "2019-01-01",
      "type": "phase",
      "release_id": 278327321,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "progress": null,
      "progress_source": "progress_manual",
      "duration_source": "duration_manual",
      "description": {
        "id": "243384959",
        "body": "Description of release phase 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      }
    },
    "epic": {
      "id": "999605892",
      "reference_num": "PRJ1-E-1",
      "name": "Epic 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/epics/PRJ1-E-1",
      "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "requirements": [
      {
        "id": "96915428",
        "name": "Body of requirement 2",
        "reference_num": "PRJ1-1-2",
        "position": 2,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "release_id": 278327321,
        "created_by_user": {
          "id": "1020675218",
          "name": "Mary Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        },
        "workflow_status": {
          "id": "1025247908",
          "name": "Shipped",
          "position": 5,
          "complete": true,
          "color": "#ecdd8f"
        },
        "url": "http://company.aha.io/requirements/PRJ1-1-2",
        "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-2",
        "description": {
          "id": "6776757454432882880",
          "body": "",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "feature": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "Feature 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-1",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
          "product_id": "131414752"
        },
        "assigned_to_user": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "default_assignee": false
        },
        "attachments": [],
        "tags": [],
        "full_tags": [],
        "custom_fields": [],
        "integration_fields": [],
        "comments_count": 0
      },
      {
        "id": "483368544",
        "name": "Body of requirement 1",
        "reference_num": "PRJ1-1-1",
        "position": 1,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "release_id": 278327321,
        "created_by_user": {
          "id": "1020675218",
          "name": "Mary Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        },
        "workflow_status": {
          "id": "934242751",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        "url": "http://company.aha.io/requirements/PRJ1-1-1",
        "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1",
        "description": {
          "id": "910541534",
          "body": "Body of requirement 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "feature": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "Feature 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-1",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
          "product_id": "131414752"
        },
        "assigned_to_user": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "default_assignee": false
        },
        "attachments": [],
        "tags": [],
        "full_tags": [],
        "custom_fields": [
          {
            "id": 848810602,
            "key": "expected_completion_date",
            "name": "Expected completion date",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": "2019-01-01",
            "type": "date"
          },
          {
            "id": 731808726,
            "key": "requested_by",
            "name": "Requested By",
            "updatedAt": "2019-01-01T00:00:00Z",
            "value": "TK",
            "type": "string"
          }
        ],
        "integration_fields": [
          {
            "id": "32487847",
            "name": "key",
            "value": "JRA-987",
            "integration_id": 342659513,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "417785887",
            "name": "id",
            "value": "991",
            "integration_id": 342659513,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "803330186",
            "name": "aha::remote_entity",
            "value": "issue_10100",
            "integration_id": 342659513,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "comments_count": 1
      },
      {
        "id": "851574643",
        "name": "Body of requirement 3",
        "reference_num": "PRJ1-1-3",
        "position": 3,
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "release_id": 278327321,
        "created_by_user": {
          "id": "1020675218",
          "name": "Mary Humpty",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        },
        "workflow_status": {
          "id": "922838743",
          "name": "Not started",
          "position": 8,
          "complete": false,
          "color": "#dce790"
        },
        "url": "http://company.aha.io/requirements/PRJ1-1-3",
        "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-3",
        "description": {
          "id": "6776757454435380800",
          "body": "",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "feature": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "Feature 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-1",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
          "product_id": "131414752"
        },
        "assigned_to_user": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "default_assignee": false
        },
        "attachments": [],
        "tags": [],
        "full_tags": [],
        "custom_fields": [],
        "integration_fields": [],
        "comments_count": 0
      }
    ],
    "initiative": {
      "id": "423077122",
      "reference_num": "PRJ1-S-1",
      "name": "Initiative 1",
      "url": "http://company.aha.io/initiatives/PRJ1-S-1",
      "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "description": {
        "id": "673273729",
        "body": "Description of initiative 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "integration_fields": [
        {
          "id": "546711007",
          "name": "id",
          "value": "9913333",
          "integration_id": 186281709,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        },
        {
          "id": "966751335",
          "name": "key",
          "value": "JRA-987222",
          "integration_id": 186281709,
          "service_name": "jira",
          "created_at": "2019-01-01T00:00:00.000Z"
        }
      ]
    },
    "goals": [
      {
        "id": "602095703",
        "name": "Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
        "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "166463080",
          "body": "Description of goal 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      }
    ],
    "comments_count": 1,
    "score_facts": [
      {
        "id": "728895917",
        "value": 1,
        "name": "Effort"
      },
      {
        "id": "846938137",
        "value": 2,
        "name": "Benefit"
      }
    ],
    "tags": [
      "Engineering",
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 3412727,
        "name": "Engineering",
        "color": "#e09052"
      },
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "custom_fields": [
      {
        "id": 1051489895,
        "key": "equation_specs_field",
        "name": "Equation specs field",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": {
          "values": {
            "123": {
              "value": 10,
              "name": "a",
              "display_value": "10.0"
            },
            "456": {
              "value": "Foobar",
              "name": "b",
              "display_value": "Foobar"
            },
            "789": {
              "value": null,
              "name": "789",
              "display_value": null
            }
          }
        },
        "type": "equation_sheet"
      },
      {
        "id": 621325984,
        "key": "expected_completion_date",
        "name": "Expected completion date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 694694494,
        "key": "negative_scorecard",
        "name": "Negative custom scorecard",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": 31,
        "type": "scorecard",
        "score_facts": [
          {
            "id": "462102328",
            "value": 6,
            "name": "Negative default value"
          }
        ]
      },
      {
        "id": 736691743,
        "key": "upload",
        "name": "Upload",
        "updatedAt": "2019-01-01T00:00:00Z",
        "attachments": [
          {
            "id": "471688235",
            "download_url": "https://company.aha.io/attachments/471688235/token/aaabbbccc7.download?size=original",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z",
            "original_file_size": 123,
            "content_type": "text/plain",
            "file_name": "uploaded_file_name.txt",
            "file_size": 123
          }
        ],
        "type": "attachment"
      }
    ],
    "custom_object_links": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      }
    ],
    "feature_links": [
      {
        "link_type": "Depends on",
        "link_type_id": 20,
        "created_at": "2019-01-01T00:00:00.000Z",
        "parent_record": {
          "id": "1007868956",
          "reference_num": "PRJ1-1",
          "name": "Feature 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-1",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
          "product_id": "131414752"
        },
        "child_record": {
          "id": "622562724",
          "reference_num": "PRJ1-2",
          "name": "Another Feature",
          "created_at": "2019-01-01T00:00:00.000Z",
          "url": "http://company.aha.io/features/PRJ1-2",
          "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
          "product_id": "131414752"
        }
      }
    ],
    "feature_only_original_estimate": null,
    "feature_only_remaining_estimate": null,
    "feature_only_work_done": null
  }
}
```

---

## Create a custom table record link associated with a requirement

**PUT** `/api/v1/requirements/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID or key of the requirement

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/requirements/PRJ1-1-1" -d '{"requirement":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "requirement": {
    "id": "483368544",
    "name": "Body of requirement 1",
    "reference_num": "PRJ1-1-1",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "release_id": 278327321,
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "workflow_status": {
      "id": "934242751",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "url": "http://company.aha.io/requirements/PRJ1-1-1",
    "resource": "http://company.aha.io/api/v1/requirements/PRJ1-1-1",
    "description": {
      "id": "910541534",
      "body": "Body of requirement 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "attachments": [],
    "tags": [],
    "full_tags": [],
    "custom_fields": [
      {
        "id": 848810602,
        "key": "expected_completion_date",
        "name": "Expected completion date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 731808726,
        "key": "requested_by",
        "name": "Requested By",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "TK",
        "type": "string"
      }
    ],
    "custom_object_links": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      }
    ],
    "integration_fields": [
      {
        "id": "32487847",
        "name": "key",
        "value": "JRA-987",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "417785887",
        "name": "id",
        "value": "991",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "803330186",
        "name": "aha::remote_entity",
        "value": "issue_10100",
        "integration_id": 342659513,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "comments_count": 1
  }
}
```

---

## Create a custom table record link associated with an idea

**PUT** `/api/v1/ideas/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "58056975",
    "name": "Idea 1",
    "reference_num": "PRJ1-I-1",
    "score": 15,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 1,
    "initial_votes": 0,
    "status_changed_at": null,
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "103757394",
      "body": "Description of idea 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-1",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-1",
    "product": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    },
    "assigned_to_user": null,
    "endorsements_count": 1,
    "comments_count": 0,
    "score_facts": [
      {
        "id": "244026645",
        "value": 10,
        "name": "Effort"
      },
      {
        "id": "394452137",
        "value": 5,
        "name": "Benefit"
      }
    ],
    "tags": [
      "Infrastructure"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      }
    ],
    "categories": [
      {
        "id": "972845454",
        "name": "Hard disk drive",
        "parent_id": 552935478,
        "project_id": 131414752,
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [
      {
        "id": 585340588,
        "key": "component",
        "name": "Component",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": [
          "web"
        ],
        "type": "array"
      },
      {
        "id": 267687015,
        "key": "custom_scorecard_definition",
        "name": "Some custom scorecard definition",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": 11,
        "type": "scorecard",
        "score_facts": [
          {
            "id": "84642379",
            "value": 10,
            "name": "Effort"
          }
        ]
      },
      {
        "id": 193641455,
        "key": "text_field1",
        "name": "TextField1",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Cairo",
        "type": "string"
      },
      {
        "id": 310635095,
        "key": "text_field2",
        "name": "TextField2",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Rennes",
        "type": "string"
      },
      {
        "id": 800380718,
        "key": "upload",
        "name": "Upload",
        "updatedAt": "2019-01-01T00:00:00Z",
        "attachments": [],
        "type": "attachment"
      }
    ],
    "custom_object_links": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      },
      {
        "key": "revenue",
        "name": "Revenue",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      },
      {
        "key": "submitters",
        "name": "Submitters",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      }
    ],
    "submitted_idea_portal_record_url": "https://ideas.example.com:8338/ideas/PRJ1-I-1",
    "integration_fields": []
  }
}
```

---

## Create a custom table record link associated with an initiative

**PUT** `/api/v1/initiatives/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID or key of the initiative

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/initiatives/423077122" -d '{"initiative":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "initiative": {
    "id": "423077122",
    "name": "Initiative 1",
    "reference_num": "PRJ1-S-1",
    "status": "not_started",
    "effort": 30,
    "value": 50,
    "presented": true,
    "color": "#bada55",
    "start_date": null,
    "end_date": null,
    "position": 1,
    "score": 4,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "duration_source": "duration_manual",
    "url": "http://company.aha.io/initiatives/PRJ1-S-1",
    "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "workflow_status": {
      "id": "53968949",
      "name": "Not Started",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "673273729",
      "body": "Description of initiative 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "attachments": [],
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
    },
    "comments_count": 1,
    "goals": [
      {
        "id": "602095703",
        "name": "Goal 1",
        "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
        "resource": "http://company.aha.io/api/v1/goals/DEMOENT-G-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "166463080",
          "body": "Description of goal 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        }
      }
    ],
    "score_facts": [],
    "features": [
      {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      }
    ],
    "master_features": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "epic": [
      {
        "id": "269219656",
        "reference_num": "PRJ3-E-3",
        "name": "A different project epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ3-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ3-E-3"
      },
      {
        "id": "362457003",
        "reference_num": "PRJ1-E-3",
        "name": "And a third",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-3",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-3"
      },
      {
        "id": "580753216",
        "reference_num": "PRJ1-E-2",
        "name": "Here's another epic",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-2",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-2"
      },
      {
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      }
    ],
    "releases": [
      {
        "id": "161456549",
        "reference_num": "PRJ1-R-2",
        "name": "Release 2",
        "start_date": "2019-01-01",
        "release_date": "2019-01-01",
        "parking_lot": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "product_id": "131414752",
        "integration_fields": [],
        "url": "http://company.aha.io/releases/PRJ1-R-2",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-2",
        "owner": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        },
        "project": {
          "id": "131414752",
          "reference_prefix": "PRJ1",
          "name": "Project 1",
          "product_line": false,
          "created_at": "2019-01-01T00:00:00.000Z",
          "workspace_type": "product_workspace",
          "url": "http://company.aha.io/projects/PRJ1"
        }
      },
      {
        "id": "278327321",
        "reference_num": "PRJ1-R-1",
        "name": "Release 1",
        "start_date": "2019-01-01",
        "release_date": "2019-01-01",
        "parking_lot": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "product_id": "131414752",
        "integration_fields": [
          {
            "id": "68217473",
            "name": "id",
            "value": "777",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "url": "http://company.aha.io/releases/PRJ1-R-1",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
        "owner": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        },
        "project": {
          "id": "131414752",
          "reference_prefix": "PRJ1",
          "name": "Project 1",
          "product_line": false,
          "created_at": "2019-01-01T00:00:00.000Z",
          "workspace_type": "product_workspace",
          "url": "http://company.aha.io/projects/PRJ1"
        }
      }
    ],
    "integration_fields": [
      {
        "id": "546711007",
        "name": "id",
        "value": "9913333",
        "integration_id": 186281709,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "966751335",
        "name": "key",
        "value": "JRA-987222",
        "integration_id": 186281709,
        "service_name": "jira",
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [
      {
        "id": 973371762,
        "key": "initiative_custom_date",
        "name": "Initiative custom date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      },
      {
        "id": 1073063442,
        "key": "initiative_priority",
        "name": "Initiative priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P2",
        "type": "string"
      }
    ],
    "custom_object_links": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---

## Create a custom table record link associated with a goal

**PUT** `/api/v1/goals/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID or key of the goal

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/goals/602095703" -d '{"goal":{"custom_object_links":{"customers":["640362830"]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "goal": {
    "id": "602095703",
    "name": "Goal 1",
    "reference_num": "DEMOENT-G-1",
    "effort": 10,
    "value": 70,
    "color": "#bada55",
    "position": 1,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "progress": null,
    "progress_source": "progress_manual",
    "url": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "resource": "http://company.aha.io/strategic_imperatives/DEMOENT-G-1",
    "description": {
      "id": "166463080",
      "body": "Description of goal 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "success_metric": {
      "name": "Metric 1",
      "description": {
        "id": "546284368",
        "body": "Description of goal 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "workflow_status": {
        "id": "396368932",
        "name": "On Track",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
    },
    "project": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "initiatives": [
      {
        "id": "423077122",
        "reference_num": "PRJ1-S-1",
        "name": "Initiative 1",
        "url": "http://company.aha.io/initiatives/PRJ1-S-1",
        "resource": "http://company.aha.io/api/v1/initiatives/PRJ1-S-1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "description": {
          "id": "673273729",
          "body": "Description of initiative 1",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "integration_fields": [
          {
            "id": "546711007",
            "name": "id",
            "value": "9913333",
            "integration_id": 186281709,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          },
          {
            "id": "966751335",
            "name": "key",
            "value": "JRA-987222",
            "integration_id": 186281709,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ]
      }
    ],
    "comments_count": 1,
    "features": [
      {
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      }
    ],
    "releases": [
      {
        "id": "278327321",
        "reference_num": "PRJ1-R-1",
        "name": "Release 1",
        "start_date": "2019-01-01",
        "release_date": "2019-01-01",
        "parking_lot": false,
        "created_at": "2019-01-01T00:00:00.000Z",
        "product_id": "131414752",
        "integration_fields": [
          {
            "id": "68217473",
            "name": "id",
            "value": "777",
            "integration_id": 204584239,
            "service_name": "jira",
            "created_at": "2019-01-01T00:00:00.000Z"
          }
        ],
        "url": "http://company.aha.io/releases/PRJ1-R-1",
        "resource": "http://company.aha.io/api/v1/releases/PRJ1-R-1",
        "owner": {
          "id": "16338845",
          "name": "John Smith",
          "email": "no-reply@aha.io",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z"
        },
        "project": {
          "id": "131414752",
          "reference_prefix": "PRJ1",
          "name": "Project 1",
          "product_line": false,
          "created_at": "2019-01-01T00:00:00.000Z",
          "workspace_type": "product_workspace",
          "url": "http://company.aha.io/projects/PRJ1"
        }
      }
    ],
    "custom_fields": [],
    "custom_object_links": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          640362830
        ]
      }
    ]
  }
}
```

---

## Link custom table records to another custom table record

**PUT** `/api/v1/custom_object_records/:id`

### Description
Resources that can be linked to records from a custom table (called custom objects in the API) can be manipulated in a bulk ID-list format.
To use custom table record links you must first add a many-to-many custom field definition to the resource.
When you pass the IDs of custom table records to link to the feature, the existing list of links will be replaced.

Examples of linking custom objects to resources with a many-to-many `customer` field:

- [Products](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_product)
- [Releases](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_release)
- [Features](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_feature)
- [Ideas](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_idea)
- [Initiatives](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_an_initiative)
- [Goals](/api/resources/custom_table_record_links/create_a_custom_table_record_link_associated_with_a_goal)

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID of the custom table record

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_object_records/640362830" -d '{"custom_object_record":{"custom_object_links":{"custom_table_name_submitters":[136661093]}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "custom_object_record": {
    "id": "640362830",
    "product_id": "131414752",
    "key": "customers",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "custom_fields": [
      {
        "id": 262515157,
        "key": "name",
        "name": "Name",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Acme Corp",
        "type": "string"
      },
      {
        "id": 883926222,
        "key": "website",
        "name": "Website",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "www.acme.com",
        "type": "url"
      }
    ],
    "custom_object_links": [
      {
        "key": "custom_table_name_link_many",
        "name": "Custom Table Linked Records",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          1059223798
        ]
      },
      {
        "key": "custom_table_name_link_many_to_one",
        "name": "Custom Table Many to One Field",
        "record_type": "CustomObjectRecord",
        "record_ids": []
      },
      {
        "key": "custom_table_name_submitters",
        "name": "Custom Table Linked Submitters",
        "record_type": "CustomObjectRecord",
        "record_ids": [
          136661093
        ]
      }
    ],
    "linked_records": [
      {
        "key": "customers",
        "name": "Customers",
        "record_type": "Ideas::Idea",
        "record_id": 162120796
      },
      {
        "key": "revenue",
        "name": "Revenue",
        "record_type": "Ideas::Idea",
        "record_id": 58056975
      },
      {
        "key": "submitters",
        "name": "Submitters",
        "record_type": "Ideas::Idea",
        "record_id": 58056975
      }
    ],
    "created_by_user": {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z"
    }
  }
}
```

---
