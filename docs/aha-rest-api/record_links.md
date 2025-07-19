# Record links

## List record links for a feature

**GET** `/api/v1/features/:id/record_links`

### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `parent_and_child_links` () - Optional - Include links where the record is both the parent and the child of the linked record (boolean)

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/1007868956/record_links" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "record_links": [
    {
      "id": 170959948,
      "link_type": "Depends on",
      "link_type_id": 20,
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_record_type": "feature",
      "parent_record_id": 1007868956,
      "child_record_type": "feature",
      "child_record_id": 622562724,
      "parent": true,
      "parent_record": {
        "record_type": "feature",
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "child_record": {
        "record_type": "feature",
        "id": "622562724",
        "reference_num": "PRJ1-2",
        "name": "Another Feature",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
        "product_id": "131414752"
      }
    }
  ]
}
```

---

## List record links including both parent and child records

**GET** `/api/v1/features/:id/record_links`

### Parameters
- `id` () - **Required** - Numeric ID or key of the feature
- `parent_and_child_links` () - Optional - Include links where the record is both the parent and the child of the linked record (boolean)

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/features/1007868956/record_links?parent_and_child_links=true" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "record_links": [
    {
      "id": 170959948,
      "link_type": "Depends on",
      "link_type_id": 20,
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_record_type": "feature",
      "parent_record_id": 1007868956,
      "child_record_type": "feature",
      "child_record_id": 622562724,
      "parent": true,
      "parent_record": {
        "record_type": "feature",
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      },
      "child_record": {
        "record_type": "feature",
        "id": "622562724",
        "reference_num": "PRJ1-2",
        "name": "Another Feature",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-2",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
        "product_id": "131414752"
      }
    },
    {
      "id": "6776757454438662145",
      "link_type": "Depends on",
      "link_type_id": 20,
      "created_at": "2019-01-01T00:00:00.000Z",
      "parent_record_type": "master_feature",
      "parent_record_id": 999605892,
      "child_record_type": "feature",
      "child_record_id": 1007868956,
      "parent": false,
      "parent_record": {
        "record_type": "master_feature",
        "id": "999605892",
        "reference_num": "PRJ1-E-1",
        "name": "Epic 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/epics/PRJ1-E-1",
        "resource": "http://company.aha.io/api/v1/epics/PRJ1-E-1"
      },
      "child_record": {
        "record_type": "feature",
        "id": "1007868956",
        "reference_num": "PRJ1-1",
        "name": "Feature 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "url": "http://company.aha.io/features/PRJ1-1",
        "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
        "product_id": "131414752"
      }
    }
  ]
}
```

---

## Get a specific record link

**GET** `/api/v1/record_links/:id`

### Parameters
- `id` () - **Required** - Numeric ID or key of the record link

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/record_links/170959948" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "record_link": {
    "id": 170959948,
    "link_type": "Depends on",
    "link_type_id": 20,
    "created_at": "2019-01-01T00:00:00.000Z",
    "parent_record_type": "feature",
    "parent_record_id": 1007868956,
    "child_record_type": "feature",
    "child_record_id": 622562724,
    "parent": true,
    "parent_record": {
      "record_type": "feature",
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "child_record": {
      "record_type": "feature",
      "id": "622562724",
      "reference_num": "PRJ1-2",
      "name": "Another Feature",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-2",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-2",
      "product_id": "131414752"
    }
  }
}
```

---

## Create a record link for a feature

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a requirement

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a epic

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a release

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a release phase

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a idea

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a goal

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a initiative

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Create a record link for a page

**POST** `/api/v1/:record_type/:id/record_links`

### Parameters
- `record_type` () - **Required** - Type of the record being linked to. One of `feature`, `release`, `idea`, `epic`, `release_phase`, `initiative`, `page`, `goal`.
- `record_id` () - **Required** - Id of the record being linked to.
- `link_type` () - **Required** - Type of link; one of `10` (Relates to), `20` (depends on), `30` (duplicated by), `40` (contained by), `50` (impacted by), `60` (blocked by), or `80` (research for).

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/pages/1051981226/record_links" -d '{"record_link":{"record_type":"feature","record_id":303873333,"link_type":10}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---

## Delete a record link

**DELETE** `/api/v1/record_links/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the record link

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/record_links/170959948" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
