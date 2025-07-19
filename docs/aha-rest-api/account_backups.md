# Account backups

## List account backups

**GET** `/api/v1/account_backups`

### Description
Account backups let you create a complete off-site backup of your Aha! account.
They can be [created](/api/resources/account_backups/create_an_account_backup),
[listed](/api/resources/account_backups/list_account_backups), and [downloaded](/api/resources/account_backups/download_an_account_backup) via the API.

An account backup may only be created once every 24 hours.

The backup file contains a representation of all of the data in the Aha! account, including all relationships. 
It does not contain user authentication data or integration secrets. The backup does not include any uploaded files.

**[Account backups](https://www.aha.io/support/roadmaps/account/security-and-system-requirements/export-backup-aha-data) are an Enterprise+ exclusive feature.**


### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/account_backups" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "account_backups": []
}
```

---

## Create an account backup

**POST** `/api/v1/account_backups`

### Description
Account backups let you create a complete off-site backup of your Aha! account.
They can be [created](/api/resources/account_backups/create_an_account_backup),
[listed](/api/resources/account_backups/list_account_backups), and [downloaded](/api/resources/account_backups/download_an_account_backup) via the API.

An account backup may only be created once every 24 hours.

The backup file contains a representation of all of the data in the Aha! account, including all relationships. 
It does not contain user authentication data or integration secrets. The backup does not include any uploaded files.

**[Account backups](https://www.aha.io/support/roadmaps/account/security-and-system-requirements/export-backup-aha-data) are an Enterprise+ exclusive feature.**


### Additional Information
The backup may take some time to generate (as long as ten minutes in a 
large account). You should poll the GET endpoint to see when the backup 
is complete. You should not poll more frequently than once every twenty 
seconds. Returns an HTTP status of 429 if a backup was already created
within the last 24 hours.


### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/account_backups" -d '' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "account_backup": {
    "id": "6776757454440047725",
    "status_code": 0,
    "status_description": "In Queue",
    "created_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## Get a specific account backup

**GET** `/api/v1/account_backups/:id`

### Description
Account backups let you create a complete off-site backup of your Aha! account.
They can be [created](/api/resources/account_backups/create_an_account_backup),
[listed](/api/resources/account_backups/list_account_backups), and [downloaded](/api/resources/account_backups/download_an_account_backup) via the API.

An account backup may only be created once every 24 hours.

The backup file contains a representation of all of the data in the Aha! account, including all relationships. 
It does not contain user authentication data or integration secrets. The backup does not include any uploaded files.

**[Account backups](https://www.aha.io/support/roadmaps/account/security-and-system-requirements/export-backup-aha-data) are an Enterprise+ exclusive feature.**


### Additional Information
The status field indicates whether the backup is ready. The possible
values are: 0 (queued), 1 (in progress), 2 (completed), 3 (error).


### Parameters
- `id` () - **Required** - Numeric ID of the backup

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/account_backups/6776757454441337868" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "account_backup": {
    "id": "6776757454441337868",
    "status_code": 3,
    "status_description": "Error",
    "created_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## Download an account backup

**GET** `/api/v1/account_backups/:id.tgz`

### Description
Account backups let you create a complete off-site backup of your Aha! account.
They can be [created](/api/resources/account_backups/create_an_account_backup),
[listed](/api/resources/account_backups/list_account_backups), and [downloaded](/api/resources/account_backups/download_an_account_backup) via the API.

An account backup may only be created once every 24 hours.

The backup file contains a representation of all of the data in the Aha! account, including all relationships. 
It does not contain user authentication data or integration secrets. The backup does not include any uploaded files.

**[Account backups](https://www.aha.io/support/roadmaps/account/security-and-system-requirements/export-backup-aha-data) are an Enterprise+ exclusive feature.**


### Parameters
- `id` () - **Required** - Numeric ID of the backup

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/account_backups/6776757454434946819.tgz" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
