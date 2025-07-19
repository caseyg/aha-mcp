# Attachments

## Create an attachment on a comment

**POST** `/api/v1/comments/:comment_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `comment_id` () - **Required** - Numeric ID of the comment for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/comments/933135074/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454436351294",
    "download_url": "https://company.aha.io/attachments/6776757454436351294/token/5e0be1000083f3f9.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 27,
    "content_type": "text/plain",
    "file_name": "sample_plain_text.txt",
    "file_size": 27
  }
}
```

---

## Create an attachment on a comment via a link

**POST** `/api/v1/comments/:comment_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `comment_id` () - **Required** - Numeric ID of the comment for which the attachment should be created

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/comments/933135074/attachments" -d '------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_url]"

http://www.aha.io/
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[content_type]"

text/html
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_name]"

home_page.html
------------XnJLe9ZIbbGUYtzPQJ16u1--
' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: multipart/form-data; boundary=----------XnJLe9ZIbbGUYtzPQJ16u1" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454438844608",
    "download_url": "https://company.aha.io/attachments/6776757454438844608/token/5e0be100006c4cfa.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 0,
    "content_type": "text/html",
    "file_name": "home_page.html",
    "file_size": 0
  }
}
```

---

## Create an attachment on an idea comment

**POST** `/api/v1/idea_comments/:idea_comment_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `idea_comment_id` () - **Required** - Numeric ID of the idea comment for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/idea_comments/622085811/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454435971172",
    "download_url": "https://company.aha.io/attachments/6776757454435971172/token/5e0be10000d58f2c.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 27,
    "content_type": "text/plain",
    "file_name": "sample_plain_text.txt",
    "file_size": 27
  }
}
```

---

## Create an attachment on an idea comment via a link

**POST** `/api/v1/idea_comments/:idea_comment_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `idea_comment_id` () - **Required** - Numeric ID of the idea comment for which the attachment should be created

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/idea_comments/622085811/attachments" -d '------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_url]"

http://www.aha.io/
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[content_type]"

text/html
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_name]"

home_page.html
------------XnJLe9ZIbbGUYtzPQJ16u1--
' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: multipart/form-data; boundary=----------XnJLe9ZIbbGUYtzPQJ16u1" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454441551224",
    "download_url": "https://company.aha.io/attachments/6776757454441551224/token/5e0be100006af027.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 0,
    "content_type": "text/html",
    "file_name": "home_page.html",
    "file_size": 0
  }
}
```

---

## Create an attachment on a to-do

**POST** `/api/v1/tasks/:task_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `task_id` () - **Required** - Numeric ID of the to-do for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/tasks/1041191038/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454428337955",
    "download_url": "https://company.aha.io/attachments/6776757454428337955/token/5e0be100009c449b.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 27,
    "content_type": "text/plain",
    "file_name": "sample_plain_text.txt",
    "file_size": 27
  }
}
```

---

## Create an attachment on a to-do via a link

**POST** `/api/v1/tasks/:task_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `task_id` () - **Required** - Numeric ID of the to-do for which the attachment should be created

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/tasks/1041191038/attachments" -d '------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_url]"

http://www.aha.io/
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[content_type]"

text/html
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_name]"

home_page.html
------------XnJLe9ZIbbGUYtzPQJ16u1--
' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: multipart/form-data; boundary=----------XnJLe9ZIbbGUYtzPQJ16u1" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454434420116",
    "download_url": "https://company.aha.io/attachments/6776757454434420116/token/5e0be10000a14554.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 0,
    "content_type": "text/html",
    "file_name": "home_page.html",
    "file_size": 0
  }
}
```

---

## Create an attachment on a custom note field

**POST** `/api/v1/custom_fields/:custom_field_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `custom_field_id` () - **Required** - Numeric ID of the custom field for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/custom_fields/432637490/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454439581011",
    "download_url": "https://company.aha.io/attachments/6776757454439581011/token/5e0be10000ecbef9.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 27,
    "content_type": "text/plain",
    "file_name": "sample_plain_text.txt",
    "file_size": 27
  }
}
```

---

## Create an attachment on a custom note field via a link

**POST** `/api/v1/custom_fields/:custom_field_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `custom_field_id` () - **Required** - Numeric ID of the custom field for which the attachment should be created

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_fields/432637490/attachments" -d '------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_url]"

http://www.aha.io/
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[content_type]"

text/html
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_name]"

home_page.html
------------XnJLe9ZIbbGUYtzPQJ16u1--
' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: multipart/form-data; boundary=----------XnJLe9ZIbbGUYtzPQJ16u1" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454432929406",
    "download_url": "https://company.aha.io/attachments/6776757454432929406/token/5e0be10000e0d32f.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 0,
    "content_type": "text/html",
    "file_name": "home_page.html",
    "file_size": 0
  }
}
```

---

## Create an attachment on a custom attachment field

**POST** `/api/v1/custom_field_values/:custom_field_value_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `custom_field_value_id` () - **Required** - Numeric ID of the custom field value for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/custom_field_values/432637490/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454430585507",
    "download_url": "https://company.aha.io/attachments/6776757454430585507/token/5e0be10000e3d29e.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 27,
    "content_type": "text/plain",
    "file_name": "sample_plain_text.txt",
    "file_size": 27
  }
}
```

---

## Create an attachment on a custom attachment field via a link

**POST** `/api/v1/custom_field_values/:custom_field_value_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `custom_field_value_id` () - **Required** - Numeric ID of the custom field value for which the attachment should be created

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/custom_field_values/432637490/attachments" -d '------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_url]"

http://www.aha.io/
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[content_type]"

text/html
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_name]"

home_page.html
------------XnJLe9ZIbbGUYtzPQJ16u1--
' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: multipart/form-data; boundary=----------XnJLe9ZIbbGUYtzPQJ16u1" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454441129155",
    "download_url": "https://company.aha.io/attachments/6776757454441129155/token/5e0be10000f7d402.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 0,
    "content_type": "text/html",
    "file_name": "home_page.html",
    "file_size": 0
  }
}
```

---

## Create an attachment on a record description

**POST** `/api/v1/notes/:note_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Additional Information
Many records throughout Aha! have an associated description: features, requirements, ideas, etc. You can find the ID of a record's description within the `description` attribute returned by any record show endpoint. You can then use that description ID to create an attachment on the record by providing it as the `note_id` URL parameter for this endpoint.


### Parameters
- `note_id` () - **Required** - Numeric ID of the record description for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/notes/793547626/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454441050004",
    "download_url": "https://company.aha.io/attachments/6776757454441050004/token/5e0be1000086735c.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 27,
    "content_type": "text/plain",
    "file_name": "sample_plain_text.txt",
    "file_size": 27
  }
}
```

---

## Create an attachment on a record description via a link

**POST** `/api/v1/notes/:note_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Additional Information
Many records throughout Aha! have an associated description: features, requirements, ideas, etc. You can find the ID of a record's description within the `description` attribute returned by any record show endpoint. You can then use that description ID to create an attachment on the record by providing it as the `note_id` URL parameter for this endpoint.


### Parameters
- `note_id` () - **Required** - Numeric ID of the record description for which the attachment should be created

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/notes/793547626/attachments" -d '------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_url]"

http://www.aha.io/
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[content_type]"

text/html
------------XnJLe9ZIbbGUYtzPQJ16u1
content-disposition: form-data; name="attachment[file_name]"

home_page.html
------------XnJLe9ZIbbGUYtzPQJ16u1--
' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: multipart/form-data; boundary=----------XnJLe9ZIbbGUYtzPQJ16u1" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "attachment": {
    "id": "6776757454430120916",
    "download_url": "https://company.aha.io/attachments/6776757454430120916/token/5e0be100003396dd.download?size=original",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "original_file_size": 0,
    "content_type": "text/html",
    "file_name": "home_page.html",
    "file_size": 0
  }
}
```

---

## Reject duplicate attachments

**POST** `/api/v1/notes/:note_id/attachments`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Additional Information
If the "If-None-Match" header is passed, Aha! will check the file's MD5 against other files uploaded that also used the If-None-Match header. If a file shares the same file size, name, and md5, a new attachment will not be created, and an HTTP 412 status code will be returned.


### Parameters
- `note_id` () - **Required** - Numeric ID of the record description for which the attachment should be created

### Example
**Request:**
```bash
curl "/api/v1/notes/793547626/attachments" -F "attachment[data]=@sample_plain_text.txt" -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Accept: application/json" \
	-H "If-None-Match: sample_etag"
```

**Response:**
```json
{
  "status": "duplicate",
  "success": false,
  "attachmentId": "6776757454432640272",
  "attachmentUrl": "https://company.aha.io/attachments/6776757454432640272/token/5e0be10000ac2936?size=original"
}
```

---

## Delete an attachment

**DELETE** `/api/v1/attachments/:attachment_id`

### Description
Files can be uploaded to Aha! as a sub-resource on any resource that supports them.
These resources support attachments:

- [Record descriptions](/api/resources/attachments/create_an_attachment_on_a_record_description) (the description of a feature, requirement, etc.)
- [Comments](/api/resources/attachments/create_an_attachment_on_a_comment)
- [To-dos](/api/resources/attachments/create_an_attachment_on_a_to-do)
- [Custom note fields](/api/resources/attachments/create_an_attachment_on_a_custom_note_field)

The format of an attachment is either a `multipart/form-data` upload with
the input name `attachment[data]` or a JSON payload pointing to an URL link:

```json
{
  "attachment": {
    "file_url": "http://www.aha.io/",
    "content_type": "text/html",
    "file_name": "home_page.html"
  }
}
```


### Parameters
- `attachment_id` () - **Required** - Numeric ID of the attachment

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/attachments/744925247" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
