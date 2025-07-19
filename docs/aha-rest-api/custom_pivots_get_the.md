# Custom pivots

## Get the list view of a saved report

**GET** `/api/v1/bookmarks/custom_pivots/:report_id`

### Description
The custom pivots API allows you to take existing list and pivot reports
and represent them as JSON. This enables developers to pull related data
from multiple types of records in a single API query.

There are two types of reports that you can pull via this API: list or pivot.
See the documentation below for a full explanation of their formats.

The `:report_id` parameter is the ID of a saved view in Aha! To find the
ID of an existing report, choose the report from the Views -> Saved views
dropdown in Aha! Then take the large number at the end of the URL with the term
custom_pivots in it. For example, `/bookmarks/custom_pivots/6434552458299516367`
has a `:report_id` of `6434552458299516367`.


### Additional Information
The list view responds with a JSON object with three attributes: pagination, columns, and rows.

The columns attribute is an array of objects that give detailed information
about the columns of the list. The objects include the name of the table, the field, and
a human readable title attribute.

The rows attribute is an of array of arrays. Each object within the inner array contains the value
of that for a specific column. Each object contains attributes for various representations of the
data. The fields are:

  - `id`: The unique id of the object
  - `plain_value`: A string representation of the object
  - `html_value`: An HTML representation of the object. This is the same HTML that
  is used in Aha! to represent the value in our reports.
  - `rich_value`: If the object is a reference to another object (such as a tag),
  the, this will be the object representation. For instance, a tag would be
  representated as:
  ```
  {
    id: "6013053275679792248",
    name: "API"
  }
  ```

The third attribute is pagination. This works like everywhere else in the Aha! API and is documented [here](/api#pagination).


### Parameters
- `report_id` () - Optional - The ID of the saved report in Aha!
- `view` () - Optional - The type of API response you want: `list` (default) or `pivot`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/bookmarks/custom_pivots/801750833?view=list" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "pagination": [
    {
      "total_records": 9,
      "total_pages": 1,
      "current_page": 1
    }
  ],
  "columns": [
    {
      "table": "projects",
      "field": "name",
      "title": "Workspace name"
    },
    {
      "table": "releases",
      "field": "name",
      "title": "Release name"
    },
    {
      "table": "features",
      "field": "name",
      "title": "Feature name"
    },
    {
      "table": "features",
      "field": "reference_num",
      "title": "Feature reference #"
    },
    {
      "table": "features",
      "field": "status",
      "title": "Feature status"
    },
    {
      "table": "ideas",
      "field": "created_by_user_id",
      "title": "Idea created by"
    }
  ],
  "rows": [
    [
      {
        "id": 131414752,
        "plain_value": "Project 1",
        "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>"
      },
      {
        "id": 278327321,
        "plain_value": "Release 1",
        "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
        "rich_value": "Release 1"
      },
      {
        "id": 209201304,
        "plain_value": "Another Fourth Feature",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-4\" href=\"/features/PRJ1-4\">Another Fourth Feature</a>",
        "rich_value": "Another Fourth Feature"
      },
      {
        "id": 209201304,
        "plain_value": "PRJ1-4",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-4\" href=\"/features/PRJ1-4\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-4</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-4</aha-record-reference>"
      },
      {
        "id": 209201304,
        "plain_value": "Designed",
        "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
        "rich_value": {
          "id": 962984386,
          "name": "Designed",
          "color": "ecdd8f"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ],
    [
      {
        "id": 131414752,
        "plain_value": "Project 1",
        "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>"
      },
      {
        "id": 278327321,
        "plain_value": "Release 1",
        "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
        "rich_value": "Release 1"
      },
      {
        "id": 303873333,
        "plain_value": "Another Third Feature",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-3\" href=\"/features/PRJ1-3\">Another Third Feature</a>",
        "rich_value": "Another Third Feature"
      },
      {
        "id": 303873333,
        "plain_value": "PRJ1-3",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-3\" href=\"/features/PRJ1-3\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-3</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-3</aha-record-reference>"
      },
      {
        "id": 303873333,
        "plain_value": "Designed",
        "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
        "rich_value": {
          "id": 962984386,
          "name": "Designed",
          "color": "ecdd8f"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ],
    [
      {
        "id": 131414752,
        "plain_value": "Project 1",
        "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>"
      },
      {
        "id": 278327321,
        "plain_value": "Release 1",
        "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
        "rich_value": "Release 1"
      },
      {
        "id": 622562724,
        "plain_value": "Another Feature",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-2\" href=\"/features/PRJ1-2\">Another Feature</a>",
        "rich_value": "Another Feature"
      },
      {
        "id": 622562724,
        "plain_value": "PRJ1-2",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-2\" href=\"/features/PRJ1-2\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-2</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-2</aha-record-reference>"
      },
      {
        "id": 622562724,
        "plain_value": "Designed",
        "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
        "rich_value": {
          "id": 962984386,
          "name": "Designed",
          "color": "ecdd8f"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ],
    [
      {
        "id": 131414752,
        "plain_value": "Project 1",
        "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>"
      },
      {
        "id": 278327321,
        "plain_value": "Release 1",
        "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
        "rich_value": "Release 1"
      },
      {
        "id": 998184963,
        "plain_value": "Another Fifth Feature",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-5\" href=\"/features/PRJ1-5\">Another Fifth Feature</a>",
        "rich_value": "Another Fifth Feature"
      },
      {
        "id": 998184963,
        "plain_value": "PRJ1-5",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-5\" href=\"/features/PRJ1-5\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-5</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-5</aha-record-reference>"
      },
      {
        "id": 998184963,
        "plain_value": "Designed",
        "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
        "rich_value": {
          "id": 962984386,
          "name": "Designed",
          "color": "ecdd8f"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ],
    [
      {
        "id": 131414752,
        "plain_value": "Project 1",
        "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>"
      },
      {
        "id": 278327321,
        "plain_value": "Release 1",
        "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
        "rich_value": "Release 1"
      },
      {
        "id": 1007868956,
        "plain_value": "Feature 1",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\">Feature 1</a>",
        "rich_value": "Feature 1"
      },
      {
        "id": 1007868956,
        "plain_value": "PRJ1-1",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference>"
      },
      {
        "id": 1007868956,
        "plain_value": "New",
        "html_value": "<span class=\"status-pill\" title=\"New\" style=\"border: none; background-color: #F1F5E8\">New</span>",
        "rich_value": {
          "id": 934242751,
          "name": "New",
          "color": "dce7c6"
        }
      },
      {
        "id": 444379319,
        "plain_value": "John Long (john@long.com)",
        "html_value": "<a data-drawer-url=\"/ideas/idea_users/1056507375\" href=\"/ideas/idea_users/1056507375\">John Long (john@long.com)</a>",
        "rich_value": {
          "id": 1056507375,
          "name": "John Long (john@long.com)"
        }
      }
    ],
    [
      {
        "id": 131414752,
        "plain_value": "Project 1",
        "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>"
      },
      {
        "id": 278327321,
        "plain_value": "Release 1",
        "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
        "rich_value": "Release 1"
      },
      {
        "id": 1007868956,
        "plain_value": "Feature 1",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\">Feature 1</a>",
        "rich_value": "Feature 1"
      },
      {
        "id": 1007868956,
        "plain_value": "PRJ1-1",
        "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference>"
      },
      {
        "id": 1007868956,
        "plain_value": "New",
        "html_value": "<span class=\"status-pill\" title=\"New\" style=\"border: none; background-color: #F1F5E8\">New</span>",
        "rich_value": {
          "id": 934242751,
          "name": "New",
          "color": "dce7c6"
        }
      },
      {
        "id": 1055237874,
        "plain_value": "John Long (john@long.com)",
        "html_value": "<a data-drawer-url=\"/ideas/idea_users/1056507375\" href=\"/ideas/idea_users/1056507375\">John Long (john@long.com)</a>",
        "rich_value": {
          "id": 1056507375,
          "name": "John Long (john@long.com)"
        }
      }
    ],
    [
      {
        "id": 517761884,
        "plain_value": "Project 2",
        "html_value": "<a data-drawer-url=\"/projects/PRJ2\" href=\"/projects/PRJ2\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 2\"></i></span><span>Project 2</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 2\"></i></span><span>Project 2</span></span>"
      },
      {
        "id": 1000426269,
        "plain_value": "Release 2",
        "html_value": "<a data-drawer-url=\"/releases/PRJ2-R-1\" href=\"/releases/PRJ2-R-1\">Release 2</a>",
        "rich_value": "Release 2"
      },
      {
        "id": 101074039,
        "plain_value": "A feature in project 2",
        "html_value": "<a data-drawer-url=\"/features/PRJ2-1\" href=\"/features/PRJ2-1\">A feature in project 2</a>",
        "rich_value": "A feature in project 2"
      },
      {
        "id": 101074039,
        "plain_value": "PRJ2-1",
        "html_value": "<a data-drawer-url=\"/features/PRJ2-1\" href=\"/features/PRJ2-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ2-1</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ2-1</aha-record-reference>"
      },
      {
        "id": 101074039,
        "plain_value": "Designed",
        "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
        "rich_value": {
          "id": 962984386,
          "name": "Designed",
          "color": "ecdd8f"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ],
    [
      {
        "id": 702241743,
        "plain_value": "Project 3",
        "html_value": "<a data-drawer-url=\"/projects/PRJ3\" href=\"/projects/PRJ3\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 3\"></i></span><span>Project 3</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 3\"></i></span><span>Project 3</span></span>"
      },
      {
        "id": 342040612,
        "plain_value": "Release 3 Project 3",
        "html_value": "<a data-drawer-url=\"/releases/PRJ3-R-1\" href=\"/releases/PRJ3-R-1\">Release 3 Project 3</a>",
        "rich_value": "Release 3 Project 3"
      },
      {
        "id": 229579240,
        "plain_value": "Feature without Requirements",
        "html_value": "<a data-drawer-url=\"/features/PRJ3-1\" href=\"/features/PRJ3-1\">Feature without Requirements</a>",
        "rich_value": "Feature without Requirements"
      },
      {
        "id": 229579240,
        "plain_value": "PRJ3-1",
        "html_value": "<a data-drawer-url=\"/features/PRJ3-1\" href=\"/features/PRJ3-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-1</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-1</aha-record-reference>"
      },
      {
        "id": 229579240,
        "plain_value": "New",
        "html_value": "<span class=\"status-pill\" title=\"New\" style=\"border: none; background-color: #F1F5E8\">New</span>",
        "rich_value": {
          "id": 934242751,
          "name": "New",
          "color": "dce7c6"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ],
    [
      {
        "id": 702241743,
        "plain_value": "Project 3",
        "html_value": "<a data-drawer-url=\"/projects/PRJ3\" href=\"/projects/PRJ3\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 3\"></i></span><span>Project 3</span></span></a>",
        "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 3\"></i></span><span>Project 3</span></span>"
      },
      {
        "id": 342040612,
        "plain_value": "Release 3 Project 3",
        "html_value": "<a data-drawer-url=\"/releases/PRJ3-R-1\" href=\"/releases/PRJ3-R-1\">Release 3 Project 3</a>",
        "rich_value": "Release 3 Project 3"
      },
      {
        "id": 959120953,
        "plain_value": "A third Feature",
        "html_value": "<a data-drawer-url=\"/features/PRJ3-2\" href=\"/features/PRJ3-2\">A third Feature</a>",
        "rich_value": "A third Feature"
      },
      {
        "id": 959120953,
        "plain_value": "PRJ3-2",
        "html_value": "<a data-drawer-url=\"/features/PRJ3-2\" href=\"/features/PRJ3-2\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-2</aha-record-reference></a>",
        "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-2</aha-record-reference>"
      },
      {
        "id": 959120953,
        "plain_value": "Designed",
        "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
        "rich_value": {
          "id": 962984386,
          "name": "Designed",
          "color": "ecdd8f"
        }
      },
      {
        "id": null,
        "plain_value": null,
        "html_value": null,
        "rich_value": null
      }
    ]
  ]
}
```

---

## Get the pivot view of a saved report

**GET** `/api/v1/bookmarks/custom_pivots/:report_id`

### Description
The custom pivots API allows you to take existing list and pivot reports
and represent them as JSON. This enables developers to pull related data
from multiple types of records in a single API query.

There are two types of reports that you can pull via this API: list or pivot.
See the documentation below for a full explanation of their formats.

The `:report_id` parameter is the ID of a saved view in Aha! To find the
ID of an existing report, choose the report from the Views -> Saved views
dropdown in Aha! Then take the large number at the end of the URL with the term
custom_pivots in it. For example, `/bookmarks/custom_pivots/6434552458299516367`
has a `:report_id` of `6434552458299516367`.


### Additional Information
The pivot view is similar to the list view, but is more referential.
There are six attributes in the JSON response: top_level_columns, columns, top_level_rows, rows, cells, field_definitions.

The columns attribute is an object where the keys are the unique id of column within the report.
Rows and field_definitions have the same referential treatment. The attributes are the id in order to ease lookup.

Since pivot reports are referential in nature and can be nested, there are top_level_rows and top_level_columns.
This allows you to easily iterate throught the nested structure. Each column and row object contain a reference to their
parent object (parent_ref). They also contain a set of references to their direct children (child_refs). They also, along with cells,
contain a reference to their field definition (via field_definitions_refs).

The field definitions object is an object that acts as a map to look up the definitions of the fields used
within the report. Similarly to the list view, these contain table, field, and title attributes.

The cells attribute is a set of nested arrays. The lowest level array is a list of the fields for a specific value.
Each element in this set has a row_ref, column_ref, and field_definition_ref which can be used to lookup which column and row
this value is representing. Just like the list view, there are multiple formats of the value:

  - id: The unique id of the object
  - plain_value: A string representation of the object
  - html_value: An HTML representation of the object. This is the same HTML that
  is used in Aha! to represent the value in our reports.
  - rich_value: If the object is a reference to another object (such as a tag),
  the, this will be the object representation.

There is no pagination with pivot report.


### Parameters
- `report_id` () - Optional - The ID of the saved report in Aha!
- `view` () - Optional - The type of API response you want: `list` (default) or `pivot`

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/bookmarks/custom_pivots/801750833?view=pivot" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "top_level_columns": [
    1,
    2,
    3
  ],
  "columns": {
    "1": {
      "ref": 1,
      "parent_ref": null,
      "child_refs": [],
      "id": 131414752,
      "plain_value": "Project 1",
      "html_value": "<a data-drawer-url=\"/projects/PRJ1\" href=\"/projects/PRJ1\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span></a>",
      "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 1\"></i></span><span>Project 1</span></span>",
      "field_definition_ref": 7
    },
    "2": {
      "ref": 2,
      "parent_ref": null,
      "child_refs": [],
      "id": 517761884,
      "plain_value": "Project 2",
      "html_value": "<a data-drawer-url=\"/projects/PRJ2\" href=\"/projects/PRJ2\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 2\"></i></span><span>Project 2</span></span></a>",
      "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 2\"></i></span><span>Project 2</span></span>",
      "field_definition_ref": 7
    },
    "3": {
      "ref": 3,
      "parent_ref": null,
      "child_refs": [],
      "id": 702241743,
      "plain_value": "Project 3",
      "html_value": "<a data-drawer-url=\"/projects/PRJ3\" href=\"/projects/PRJ3\"><span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 3\"></i></span><span>Project 3</span></span></a>",
      "rich_value": "<span class=\"project-name\"><span><i class=\"fa-regular fa-browser\" style=\"display: table-cell; vertical-align: middle; padding-right: 5px; \" data-title=\"Project 3\"></i></span><span>Project 3</span></span>",
      "field_definition_ref": 7
    }
  },
  "top_level_rows": [
    4,
    5,
    6
  ],
  "rows": {
    "4": {
      "ref": 4,
      "parent_ref": null,
      "child_refs": [],
      "id": 278327321,
      "plain_value": "Release 1",
      "html_value": "<a data-drawer-url=\"/releases/PRJ1-R-1\" href=\"/releases/PRJ1-R-1\">Release 1</a>",
      "rich_value": "Release 1",
      "field_definition_ref": 8
    },
    "5": {
      "ref": 5,
      "parent_ref": null,
      "child_refs": [],
      "id": 1000426269,
      "plain_value": "Release 2",
      "html_value": "<a data-drawer-url=\"/releases/PRJ2-R-1\" href=\"/releases/PRJ2-R-1\">Release 2</a>",
      "rich_value": "Release 2",
      "field_definition_ref": 8
    },
    "6": {
      "ref": 6,
      "parent_ref": null,
      "child_refs": [],
      "id": 342040612,
      "plain_value": "Release 3 Project 3",
      "html_value": "<a data-drawer-url=\"/releases/PRJ3-R-1\" href=\"/releases/PRJ3-R-1\">Release 3 Project 3</a>",
      "rich_value": "Release 3 Project 3",
      "field_definition_ref": 8
    }
  },
  "cells": [
    [
      [
        [
          {
            "id": 1007868956,
            "plain_value": "PRJ1-1",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference>",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 9
          },
          {
            "id": 1007868956,
            "plain_value": "Feature 1",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\">Feature 1</a>",
            "rich_value": "Feature 1",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 10
          },
          {
            "id": 1007868956,
            "plain_value": "New",
            "html_value": "<span class=\"status-pill\" title=\"New\" style=\"border: none; background-color: #F1F5E8\">New</span>",
            "rich_value": {
              "id": 934242751,
              "name": "New",
              "color": "dce7c6"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 11
          },
          {
            "id": 444379319,
            "plain_value": "John Long (john@long.com)",
            "html_value": "<a data-drawer-url=\"/ideas/idea_users/1056507375\" href=\"/ideas/idea_users/1056507375\">John Long (john@long.com)</a>",
            "rich_value": {
              "id": 1056507375,
              "name": "John Long (john@long.com)"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 12
          }
        ],
        [
          {
            "id": 1007868956,
            "plain_value": "PRJ1-1",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-1</aha-record-reference>",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 9
          },
          {
            "id": 1007868956,
            "plain_value": "Feature 1",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-1\" href=\"/features/PRJ1-1\">Feature 1</a>",
            "rich_value": "Feature 1",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 10
          },
          {
            "id": 1007868956,
            "plain_value": "New",
            "html_value": "<span class=\"status-pill\" title=\"New\" style=\"border: none; background-color: #F1F5E8\">New</span>",
            "rich_value": {
              "id": 934242751,
              "name": "New",
              "color": "dce7c6"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 11
          },
          {
            "id": 1055237874,
            "plain_value": "John Long (john@long.com)",
            "html_value": "<a data-drawer-url=\"/ideas/idea_users/1056507375\" href=\"/ideas/idea_users/1056507375\">John Long (john@long.com)</a>",
            "rich_value": {
              "id": 1056507375,
              "name": "John Long (john@long.com)"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 12
          }
        ],
        [
          {
            "id": 622562724,
            "plain_value": "PRJ1-2",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-2\" href=\"/features/PRJ1-2\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-2</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-2</aha-record-reference>",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 9
          },
          {
            "id": 622562724,
            "plain_value": "Another Feature",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-2\" href=\"/features/PRJ1-2\">Another Feature</a>",
            "rich_value": "Another Feature",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 10
          },
          {
            "id": 622562724,
            "plain_value": "Designed",
            "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
            "rich_value": {
              "id": 962984386,
              "name": "Designed",
              "color": "ecdd8f"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 12
          }
        ],
        [
          {
            "id": 303873333,
            "plain_value": "PRJ1-3",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-3\" href=\"/features/PRJ1-3\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-3</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-3</aha-record-reference>",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 9
          },
          {
            "id": 303873333,
            "plain_value": "Another Third Feature",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-3\" href=\"/features/PRJ1-3\">Another Third Feature</a>",
            "rich_value": "Another Third Feature",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 10
          },
          {
            "id": 303873333,
            "plain_value": "Designed",
            "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
            "rich_value": {
              "id": 962984386,
              "name": "Designed",
              "color": "ecdd8f"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 12
          }
        ],
        [
          {
            "id": 209201304,
            "plain_value": "PRJ1-4",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-4\" href=\"/features/PRJ1-4\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-4</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-4</aha-record-reference>",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 9
          },
          {
            "id": 209201304,
            "plain_value": "Another Fourth Feature",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-4\" href=\"/features/PRJ1-4\">Another Fourth Feature</a>",
            "rich_value": "Another Fourth Feature",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 10
          },
          {
            "id": 209201304,
            "plain_value": "Designed",
            "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
            "rich_value": {
              "id": 962984386,
              "name": "Designed",
              "color": "ecdd8f"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 12
          }
        ],
        [
          {
            "id": 998184963,
            "plain_value": "PRJ1-5",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-5\" href=\"/features/PRJ1-5\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-5</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ1-5</aha-record-reference>",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 9
          },
          {
            "id": 998184963,
            "plain_value": "Another Fifth Feature",
            "html_value": "<a data-drawer-url=\"/features/PRJ1-5\" href=\"/features/PRJ1-5\">Another Fifth Feature</a>",
            "rich_value": "Another Fifth Feature",
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 10
          },
          {
            "id": 998184963,
            "plain_value": "Designed",
            "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
            "rich_value": {
              "id": 962984386,
              "name": "Designed",
              "color": "ecdd8f"
            },
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 4,
            "column_ref": 1,
            "field_definition_ref": 12
          }
        ]
      ],
      [],
      []
    ],
    [
      [],
      [
        [
          {
            "id": 101074039,
            "plain_value": "PRJ2-1",
            "html_value": "<a data-drawer-url=\"/features/PRJ2-1\" href=\"/features/PRJ2-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ2-1</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ2-1</aha-record-reference>",
            "row_ref": 5,
            "column_ref": 2,
            "field_definition_ref": 9
          },
          {
            "id": 101074039,
            "plain_value": "A feature in project 2",
            "html_value": "<a data-drawer-url=\"/features/PRJ2-1\" href=\"/features/PRJ2-1\">A feature in project 2</a>",
            "rich_value": "A feature in project 2",
            "row_ref": 5,
            "column_ref": 2,
            "field_definition_ref": 10
          },
          {
            "id": 101074039,
            "plain_value": "Designed",
            "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
            "rich_value": {
              "id": 962984386,
              "name": "Designed",
              "color": "ecdd8f"
            },
            "row_ref": 5,
            "column_ref": 2,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 5,
            "column_ref": 2,
            "field_definition_ref": 12
          }
        ]
      ],
      []
    ],
    [
      [],
      [],
      [
        [
          {
            "id": 229579240,
            "plain_value": "PRJ3-1",
            "html_value": "<a data-drawer-url=\"/features/PRJ3-1\" href=\"/features/PRJ3-1\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-1</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-1</aha-record-reference>",
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 9
          },
          {
            "id": 229579240,
            "plain_value": "Feature without Requirements",
            "html_value": "<a data-drawer-url=\"/features/PRJ3-1\" href=\"/features/PRJ3-1\">Feature without Requirements</a>",
            "rich_value": "Feature without Requirements",
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 10
          },
          {
            "id": 229579240,
            "plain_value": "New",
            "html_value": "<span class=\"status-pill\" title=\"New\" style=\"border: none; background-color: #F1F5E8\">New</span>",
            "rich_value": {
              "id": 934242751,
              "name": "New",
              "color": "dce7c6"
            },
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 12
          }
        ],
        [
          {
            "id": 959120953,
            "plain_value": "PRJ3-2",
            "html_value": "<a data-drawer-url=\"/features/PRJ3-2\" href=\"/features/PRJ3-2\"><aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-2</aha-record-reference></a>",
            "rich_value": "<aha-record-reference record-type=\"Feature\" size=\"small\">PRJ3-2</aha-record-reference>",
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 9
          },
          {
            "id": 959120953,
            "plain_value": "A third Feature",
            "html_value": "<a data-drawer-url=\"/features/PRJ3-2\" href=\"/features/PRJ3-2\">A third Feature</a>",
            "rich_value": "A third Feature",
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 10
          },
          {
            "id": 959120953,
            "plain_value": "Designed",
            "html_value": "<span class=\"status-pill\" title=\"Designed\" style=\"border: none; background-color: #F7F1D2\">Designed</span>",
            "rich_value": {
              "id": 962984386,
              "name": "Designed",
              "color": "ecdd8f"
            },
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 11
          },
          {
            "id": null,
            "plain_value": null,
            "html_value": null,
            "rich_value": null,
            "row_ref": 6,
            "column_ref": 3,
            "field_definition_ref": 12
          }
        ]
      ]
    ]
  ],
  "field_definitions": {
    "7": {
      "ref": 7,
      "table": "projects",
      "field": "name",
      "title": "Workspace name"
    },
    "8": {
      "ref": 8,
      "table": "releases",
      "field": "name",
      "title": "Release name"
    },
    "9": {
      "ref": 9,
      "table": "features",
      "field": "reference_num",
      "title": "Feature reference #"
    },
    "10": {
      "ref": 10,
      "table": "features",
      "field": "name",
      "title": "Feature name"
    },
    "11": {
      "ref": 11,
      "table": "features",
      "field": "status",
      "title": "Feature status"
    },
    "12": {
      "ref": 12,
      "table": "ideas",
      "field": "created_by_user_id",
      "title": "Idea created by"
    }
  }
}
```

---
