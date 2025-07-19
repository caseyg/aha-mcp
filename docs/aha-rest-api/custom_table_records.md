# Custom table records

## Create a custom table record

**POST** `/api/v1/products/:product_id/custom_objects/:key/records`

### Description
Custom tables have a different set of records for each product.
This means that if you want to
[create one](/api/resources/custom_table_records/create_a_custom_table_record)
or
[list them](/api/resources/custom_table_records/list_records_in_a_custom_table_for_a_product)
you must scope them to a product.

Once you have the ID of a specific custom table record, you can
[get](/api/resources/custom_table_records/get_a_specific_custom_table_record),
[modify](/api/resources/custom_table_records/update_a_custom_table_record),
or
[delete](/api/resources/custom_table_records/delete_a_custom_table_record)
them on the root custom table records resource.

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `key` () - **Required** - API key of the custom table for which to create a record

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/custom_objects/customers/records" -d '{"custom_object_record":{"custom_fields":{"name":"Major conglomerate","website":"www.conglom.com"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "custom_object_record": {
    "id": "6776757454428589549",
    "product_id": "131414752",
    "key": "customers",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "custom_fields": [
      {
        "id": "6776757454435187338",
        "key": "name",
        "name": "Name",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Major conglomerate",
        "type": "string"
      },
      {
        "id": "6776757454431187810",
        "key": "website",
        "name": "Website",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "www.conglom.com",
        "type": "url"
      }
    ],
    "custom_object_links": [],
    "linked_records": [],
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

## List records in a custom table for a product

**GET** `/api/v1/products/:product_id/custom_objects/:key/records`

### Description
Custom tables have a different set of records for each product.
This means that if you want to
[create one](/api/resources/custom_table_records/create_a_custom_table_record)
or
[list them](/api/resources/custom_table_records/list_records_in_a_custom_table_for_a_product)
you must scope them to a product.

Once you have the ID of a specific custom table record, you can
[get](/api/resources/custom_table_records/get_a_specific_custom_table_record),
[modify](/api/resources/custom_table_records/update_a_custom_table_record),
or
[delete](/api/resources/custom_table_records/delete_a_custom_table_record)
them on the root custom table records resource.

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `key` () - **Required** - API key of the custom table for which to list records
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only records updated after the timestamp will be returned.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/custom_objects/customers/records" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "custom_object_records": [
    {
      "id": "8397122",
      "product_id": "131414752",
      "key": "customers",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "custom_fields": [
        {
          "id": 564906240,
          "key": "name",
          "name": "Name",
          "updatedAt": "2019-01-01T00:00:00Z",
          "value": "Zane Corp",
          "type": "string"
        }
      ],
      "custom_object_links": [
        {
          "key": "custom_table_name_link_many",
          "name": "Custom Table Linked Records",
          "record_type": "CustomObjectRecord",
          "record_ids": []
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
          "record_ids": []
        }
      ],
      "linked_records": [],
      "created_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
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
          "record_ids": []
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
  ],
  "pagination": {
    "total_records": 2,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific custom table record

**GET** `/api/v1/custom_object_records/:id`

### Description
Custom tables have a different set of records for each product.
This means that if you want to
[create one](/api/resources/custom_table_records/create_a_custom_table_record)
or
[list them](/api/resources/custom_table_records/list_records_in_a_custom_table_for_a_product)
you must scope them to a product.

Once you have the ID of a specific custom table record, you can
[get](/api/resources/custom_table_records/get_a_specific_custom_table_record),
[modify](/api/resources/custom_table_records/update_a_custom_table_record),
or
[delete](/api/resources/custom_table_records/delete_a_custom_table_record)
them on the root custom table records resource.

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID of the custom table record

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/custom_object_records/640362830" -X GET \
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
        "record_ids": []
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

## Update a custom table record

**PUT** `/api/v1/custom_object_records/:id`

### Description
Custom tables have a different set of records for each product.
This means that if you want to
[create one](/api/resources/custom_table_records/create_a_custom_table_record)
or
[list them](/api/resources/custom_table_records/list_records_in_a_custom_table_for_a_product)
you must scope them to a product.

Once you have the ID of a specific custom table record, you can
[get](/api/resources/custom_table_records/get_a_specific_custom_table_record),
[modify](/api/resources/custom_table_records/update_a_custom_table_record),
or
[delete](/api/resources/custom_table_records/delete_a_custom_table_record)
them on the root custom table records resource.

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID of the custom table record

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_object_records/640362830" -d '{"custom_object_record":{"custom_fields":{"name":"Acme parent corp","website":"www.acmeparent.com"}}}' -X PUT \
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
        "value": "Acme parent corp",
        "type": "string"
      },
      {
        "id": 883926222,
        "key": "website",
        "name": "Website",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "www.acmeparent.com",
        "type": "url"
      }
    ],
    "custom_object_links": [],
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

## Delete a custom table record

**DELETE** `/api/v1/custom_object_records/:id`

### Description
Custom tables have a different set of records for each product.
This means that if you want to
[create one](/api/resources/custom_table_records/create_a_custom_table_record)
or
[list them](/api/resources/custom_table_records/list_records_in_a_custom_table_for_a_product)
you must scope them to a product.

Once you have the ID of a specific custom table record, you can
[get](/api/resources/custom_table_records/get_a_specific_custom_table_record),
[modify](/api/resources/custom_table_records/update_a_custom_table_record),
or
[delete](/api/resources/custom_table_records/delete_a_custom_table_record)
them on the root custom table records resource.

**[Custom tables](https://www.aha.io/support/roadmaps/strategic-roadmaps/customizations/custom-tables) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID of the custom table record

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_object_records/640362830" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
