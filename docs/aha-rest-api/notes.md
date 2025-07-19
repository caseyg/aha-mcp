# Notes

## Create a note

**POST** `/api/v1/products/:product_id/pages`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `document_type` () - Optional - Type of document to be created - can be: note, whiteboard, folder, internal_link, or external_link. Defaults to note
- `name` () - **Required** - Name of the page.
- `description_attributes` () - Optional - Description of the page — see example.
- `parent_id` () - Optional - ID of a parent page or folder to nest this page under
- `tags` () - Optional - Tags to add to the page. Multiple tags must be separated by commas.
- `editor_width` () - Optional - Controls the width of the page when viewed. Options are: NARROW, FULL

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/pages" -d '{"page":{"name":"Note 3","description_attributes":{"body":"\u003cp\u003eAn awesome new note\u003c/p\u003e"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "6776757454434534575",
    "name": "Note 3",
    "title": "PRJ1-N-11 Note 3",
    "document_title": "Note 3 | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-11",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "NARROW",
    "type_name": "note",
    "position": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-11",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-11",
    "product_id": "131414752",
    "description": {
      "id": "6776757454441918617",
      "body": "<p>An awesome new note</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [],
    "full_tags": [],
    "comments_count": 0,
    "custom_fields": []
  }
}
```

---

## Create an internal link

**POST** `/api/v1/products/:product_id/pages`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `document_type` () - Optional - Type of document to be created - can be: note, whiteboard, folder, internal_link, or external_link. Defaults to note
- `linked_record_id` () - **Required** - The ID for the Aha! record to link to for internal links
- `linked_record_type` () - **Required** - The type of the Aha! record being linked to, e.g. Feature, Epic

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/pages" -d '{"page":{"document_type":"internal_link","linked_record_id":1007868956,"linked_record_type":"Feature"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "6776757454432843159",
    "name": null,
    "title": "PRJ1-N-11 Untitled",
    "document_title": "Untitled | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-11",
    "emoji_value": null,
    "document_type": 80,
    "document_type_name": "internal_link",
    "editor_width": null,
    "type_name": "internal link",
    "position": null,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "linked_record_id": 1007868956,
    "linked_record_type": "Feature",
    "url": "http://company.aha.io/pages/PRJ1-N-11",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-11",
    "product_id": "131414752",
    "description": {
      "id": "6776757454427059594",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [],
    "full_tags": [],
    "comments_count": 0,
    "custom_fields": []
  }
}
```

---

## List notes for a product

**GET** `/api/v1/products/:product_id/pages`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against the note name

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/pages" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "pages": [
    {
      "id": "123524136",
      "name": "Title of the meeting note",
      "title": "PRJ1-N-9 Title of the meeting note",
      "reference_num": "PRJ1-N-9",
      "url": "http://company.aha.io/pages/PRJ1-N-9",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-9",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "199011658",
      "name": "Title of the child note",
      "title": "PRJ1-N-4 Title of the child note",
      "reference_num": "PRJ1-N-4",
      "url": "http://company.aha.io/pages/PRJ1-N-4",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-4",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": 702939369
    },
    {
      "id": "249102634",
      "name": null,
      "title": "PRJ1-N-7 Untitled",
      "reference_num": "PRJ1-N-7",
      "url": "http://company.aha.io/pages/PRJ1-N-7",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-7",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "256116692",
      "name": "Shared page title",
      "title": "PRJ1-N-10 Shared page title",
      "reference_num": "PRJ1-N-10",
      "url": "http://company.aha.io/pages/PRJ1-N-10",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-10",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "280859787",
      "name": "External link",
      "title": "PRJ1-N-6 External link",
      "reference_num": "PRJ1-N-6",
      "url": "http://company.aha.io/pages/PRJ1-N-6",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-6",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "549832152",
      "name": "Title of the second whiteboard",
      "title": "PRJ1-N-6 Title of the second whiteboard",
      "reference_num": "PRJ1-N-6",
      "url": "http://company.aha.io/pages/PRJ1-N-6",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-6",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "666543134",
      "name": "Title of the second note",
      "title": "PRJ1-N-2 Title of the second note",
      "reference_num": "PRJ1-N-2",
      "url": "http://company.aha.io/pages/PRJ1-N-2",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "702939369",
      "name": "Title of the parent note",
      "title": "PRJ1-N-3 Title of the parent note",
      "reference_num": "PRJ1-N-3",
      "url": "http://company.aha.io/pages/PRJ1-N-3",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-3",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "969708644",
      "name": "Title of the first whiteboard",
      "title": "PRJ1-N-5 Title of the first whiteboard",
      "reference_num": "PRJ1-N-5",
      "url": "http://company.aha.io/pages/PRJ1-N-5",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-5",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "970863041",
      "name": null,
      "title": "PRJ1-N-8 Untitled",
      "reference_num": "PRJ1-N-8",
      "url": "http://company.aha.io/pages/PRJ1-N-8",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-8",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    },
    {
      "id": "1051981226",
      "name": "Title of the first note",
      "title": "PRJ1-N-1 Title of the first note",
      "reference_num": "PRJ1-N-1",
      "url": "http://company.aha.io/pages/PRJ1-N-1",
      "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_id": null
    }
  ],
  "pagination": {
    "total_records": 11,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific note

**GET** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID of the note

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/pages/1051981226" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "1051981226",
    "name": "Title of the first note",
    "title": "PRJ1-N-1 Title of the first note",
    "document_title": "Title of the first note | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-1",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "FULL",
    "type_name": "note",
    "position": 100000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-1",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
    "product_id": "131414752",
    "description": {
      "id": "669149001",
      "body": "Description of note 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [
      "Infrastructure",
      "Sales"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      },
      {
        "id": 926098016,
        "name": "Sales",
        "color": "#e0da52"
      }
    ],
    "comments_count": 0,
    "custom_fields": [
      {
        "id": 416524155,
        "key": "review_date",
        "name": "Review date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ]
  }
}
```

---

## Update a note

**PUT** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note
- `name` () - Optional - Name of the page.
- `description_attributes` () - Optional - Description of the page — see example.
- `parent_id` () - Optional - ID of a parent page or folder to nest this page under
- `tags` () - Optional - Tags to add to the page. Multiple tags must be separated by commas.
- `editor_width` () - Optional - Controls the width of the page when viewed. Options are: NARROW, FULL

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226" -d '{"page":{"name":"New name for the note","description_attributes":{"body":"\u003cp\u003eAn awesome new note\u003c/p\u003e"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "1051981226",
    "name": "New name for the note",
    "title": "PRJ1-N-1 New name for the note",
    "document_title": "New name for the note | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-1",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "FULL",
    "type_name": "note",
    "position": 100000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-1",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
    "product_id": "131414752",
    "description": {
      "id": "669149001",
      "body": "<p>An awesome new note</p>",
      "editor_version": 1,
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [
      "Infrastructure",
      "Sales"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      },
      {
        "id": 926098016,
        "name": "Sales",
        "color": "#e0da52"
      }
    ],
    "comments_count": 0,
    "custom_fields": [
      {
        "id": 416524155,
        "key": "review_date",
        "name": "Review date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ]
  }
}
```

---

## Update a note's tags with comma-separated values

**PUT** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note
- `name` () - Optional - Name of the page.
- `description_attributes` () - Optional - Description of the page — see example.
- `parent_id` () - Optional - ID of a parent page or folder to nest this page under
- `tags` () - Optional - Tags to add to the page. Multiple tags must be separated by commas.
- `editor_width` () - Optional - Controls the width of the page when viewed. Options are: NARROW, FULL

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226" -d '{"page":{"tags":"tag2, tag3"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "1051981226",
    "name": "Title of the first note",
    "title": "PRJ1-N-1 Title of the first note",
    "document_title": "Title of the first note | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-1",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "FULL",
    "type_name": "note",
    "position": 100000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-1",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
    "product_id": "131414752",
    "description": {
      "id": "669149001",
      "body": "Description of note 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [
      "tag2",
      "tag3"
    ],
    "full_tags": [
      {
        "id": "6776757454430816874",
        "name": "tag2",
        "color": "#52d3e0"
      },
      {
        "id": "6776757454432173981",
        "name": "tag3",
        "color": "#bb52e0"
      }
    ],
    "comments_count": 0,
    "custom_fields": [
      {
        "id": 416524155,
        "key": "review_date",
        "name": "Review date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ]
  }
}
```

---

## Update a note's tags with an array

**PUT** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note
- `name` () - Optional - Name of the page.
- `description_attributes` () - Optional - Description of the page — see example.
- `parent_id` () - Optional - ID of a parent page or folder to nest this page under
- `tags` () - Optional - Tags to add to the page. Multiple tags must be separated by commas.
- `editor_width` () - Optional - Controls the width of the page when viewed. Options are: NARROW, FULL

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226" -d '{"page":{"tags":["tag2","tag3"]}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "1051981226",
    "name": "Title of the first note",
    "title": "PRJ1-N-1 Title of the first note",
    "document_title": "Title of the first note | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-1",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "FULL",
    "type_name": "note",
    "position": 100000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-1",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
    "product_id": "131414752",
    "description": {
      "id": "669149001",
      "body": "Description of note 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [
      "tag2",
      "tag3"
    ],
    "full_tags": [
      {
        "id": "6776757454425442878",
        "name": "tag2",
        "color": "#52d3e0"
      },
      {
        "id": "6776757454428826448",
        "name": "tag3",
        "color": "#bb52e0"
      }
    ],
    "comments_count": 0,
    "custom_fields": [
      {
        "id": 416524155,
        "key": "review_date",
        "name": "Review date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ]
  }
}
```

---

## Update a note's custom fields

**PUT** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note
- `name` () - Optional - Name of the page.
- `description_attributes` () - Optional - Description of the page — see example.
- `parent_id` () - Optional - ID of a parent page or folder to nest this page under
- `tags` () - Optional - Tags to add to the page. Multiple tags must be separated by commas.
- `editor_width` () - Optional - Controls the width of the page when viewed. Options are: NARROW, FULL

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226" -d '{"page":{"custom_fields":{"review_date":"2019-01-01"}}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "1051981226",
    "name": "Title of the first note",
    "title": "PRJ1-N-1 Title of the first note",
    "document_title": "Title of the first note | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-1",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "FULL",
    "type_name": "note",
    "position": 100000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-1",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
    "product_id": "131414752",
    "description": {
      "id": "669149001",
      "body": "Description of note 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [
      "Infrastructure",
      "Sales"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      },
      {
        "id": 926098016,
        "name": "Sales",
        "color": "#e0da52"
      }
    ],
    "comments_count": 0,
    "custom_fields": [
      {
        "id": 416524155,
        "key": "review_date",
        "name": "Review date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ]
  }
}
```

---

## Update a note's width in a knowledge base

**PUT** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note
- `name` () - Optional - Name of the page.
- `description_attributes` () - Optional - Description of the page — see example.
- `parent_id` () - Optional - ID of a parent page or folder to nest this page under
- `tags` () - Optional - Tags to add to the page. Multiple tags must be separated by commas.
- `editor_width` () - Optional - Controls the width of the page when viewed. Options are: NARROW, FULL

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226" -d '{"page":{"editor_width":"NARROW"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "1051981226",
    "name": "Title of the first note",
    "title": "PRJ1-N-1 Title of the first note",
    "document_title": "Title of the first note | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-1",
    "emoji_value": null,
    "document_type": 10,
    "document_type_name": "note",
    "editor_width": "NARROW",
    "type_name": "note",
    "position": 100000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "url": "http://company.aha.io/pages/PRJ1-N-1",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-1",
    "product_id": "131414752",
    "description": {
      "id": "669149001",
      "body": "Description of note 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [
      "Infrastructure",
      "Sales"
    ],
    "full_tags": [
      {
        "id": 775582684,
        "name": "Infrastructure",
        "color": "#7552e0"
      },
      {
        "id": 926098016,
        "name": "Sales",
        "color": "#e0da52"
      }
    ],
    "comments_count": 0,
    "custom_fields": [
      {
        "id": 416524155,
        "key": "review_date",
        "name": "Review date",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "2019-01-01",
        "type": "date"
      }
    ]
  }
}
```

---

## Update an external link

**PUT** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note
- `name` () - **Required** - Name of the page.
- `external_url` () - **Required** - The URL for an external link

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/280859787" -d '{"page":{"name":"Build products customers love","external_url":"https://www.aha.io/solutions/product"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "page": {
    "id": "280859787",
    "name": "Build products customers love",
    "title": "PRJ1-N-6 Build products customers love",
    "document_title": "Build products customers love | Aha!",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "reference_num": "PRJ1-N-6",
    "emoji_value": null,
    "document_type": 70,
    "document_type_name": "external_link",
    "editor_width": null,
    "type_name": "external link",
    "position": 500000,
    "created_at": "2019-01-01T00:00:00.000Z",
    "location": null,
    "edit_locked": false,
    "external_url": "https://www.aha.io/solutions/product",
    "url": "http://company.aha.io/pages/PRJ1-N-6",
    "resource": "http://company.aha.io/api/v1/pages/PRJ1-N-6",
    "product_id": "131414752",
    "description": {
      "id": "6776757454432622399",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "parent_id": null,
    "tags": [],
    "full_tags": [],
    "comments_count": 0,
    "custom_fields": []
  }
}
```

---

## Delete a note

**DELETE** `/api/v1/pages/:id`

### Description
"Notes" in the web interface are referenced as "pages" from API endpoints.


### Parameters
- `id` () - **Required** - Numeric ID or key of the note

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
