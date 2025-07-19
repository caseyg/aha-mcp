# Historical Audits

## Read the contents of the historical index

**GET** `/api/v1/historical_audits`

### Description
The historical audits endpoint is similar to the the Audits endpoint, but searches for audit records generated older than 12 calendar months ago. For searches of more recent data, the much more performant [Audits API](/api/resources/audits) should be used.

The [historical index](/api/resources/historical_audits/read_the_contents_of_the_historical_index) should first be used to identify time-periods of interest, and then a search can be conducted to fetch the full details of the audit records from that period.

There are two important caveats to using this API:
1. Searching through historical audits is an asynchronous operation. A search must first be [created](/api/resources/historical_audits/create_an_audit_search), and then the data may be [consumed later](/api/resources/historical_audits/read_the_results_of_an_audit_search)
2. Searching through historical audits imposes a stricter rate-limit than the general rate limit of the API. This API also enforces rate-limiting through a *token-based system.*
  a. Each Audits search consumes a specific number of tokens. The token cost of a search will be presented to the user through the [read results operation.](/api/resources/historical_audits/read_the_results_of_an_audit_search)
  b. The token cost of a request is only known after the search completes, and corresponds to the amount of data which was required to be scanned to fulfill the request. Specifying additional filters, such as `user_id`, `auditable_type`, and `audit_action` will decrease the token cost. 
  c. Upon making a request, the maximum token cost for a query will be charged to your account. The difference between the actual token cost and the maximum token cost will be refunded when the search completes and you read the search data.
  d. Tokens are continually replenished. You can see the current number of tokens available in the `X-Historical-Tokens-Available` header, present on every response to these resources.
  e. Reading from the [historical index](/api/resources/historical_audits/read_the_contents_of_the_historical_index) does not consume any tokens.

### Parameters
- `created_since` () - **Required** - ISO8601 timestamp determining the beginning of the search range for historical changes
- `created_before` () - **Required** - ISO8601 timestamp determining the end of the search window for historical changes
- `user_id` () - Optional - Numeric user ID, which searches only for audit records where one particular user was the actor
- `auditable_id` () - Optional - Numeric ID of the record for which history should be retrieved
- `auditable_type` () - Optional - String identifier of the type of record for which history should be retrieved
- `associated_id` () - Optional - Numeric ID of the primary record for which history should be retrieved. Use these parameters to fetch only the history for secondary records, like descriptions and custom field values.
- `associated_type` () - Optional - String identifier of the type of the primary record for which history should be retrieved

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/historical_audits?created_since=2019-01-01T00%3A00%3A00Z&created_before=2019-01-01T00%3A00%3A00Z&auditable_type=Feature&user_id=1049303076" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "historical_audits": [
    {
      "auditable_id": 1007868956,
      "auditable_type": "Feature",
      "id": "1049303076",
      "name": "George Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "dates_active": [
        "2019-01-01",
        "2019-01-01",
        "2019-01-01",
        "2019-01-01"
      ]
    },
    {
      "auditable_id": 1007868956,
      "auditable_type": "Feature",
      "id": "1049303076",
      "name": "George Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "dates_active": [
        "2019-01-01",
        "2019-01-01",
        "2019-01-01",
        "2019-01-01"
      ]
    },
    {
      "auditable_id": 1007868956,
      "auditable_type": "Feature",
      "id": "1049303076",
      "name": "George Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "dates_active": [
        "2019-01-01",
        "2019-01-01",
        "2019-01-01",
        "2019-01-01"
      ]
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

## Create an audit search

**POST** `/api/v1/historical_audits`

### Description
The historical audits endpoint is similar to the the Audits endpoint, but searches for audit records generated older than 12 calendar months ago. For searches of more recent data, the much more performant [Audits API](/api/resources/audits) should be used.

The [historical index](/api/resources/historical_audits/read_the_contents_of_the_historical_index) should first be used to identify time-periods of interest, and then a search can be conducted to fetch the full details of the audit records from that period.

There are two important caveats to using this API:
1. Searching through historical audits is an asynchronous operation. A search must first be [created](/api/resources/historical_audits/create_an_audit_search), and then the data may be [consumed later](/api/resources/historical_audits/read_the_results_of_an_audit_search)
2. Searching through historical audits imposes a stricter rate-limit than the general rate limit of the API. This API also enforces rate-limiting through a *token-based system.*
  a. Each Audits search consumes a specific number of tokens. The token cost of a search will be presented to the user through the [read results operation.](/api/resources/historical_audits/read_the_results_of_an_audit_search)
  b. The token cost of a request is only known after the search completes, and corresponds to the amount of data which was required to be scanned to fulfill the request. Specifying additional filters, such as `user_id`, `auditable_type`, and `audit_action` will decrease the token cost. 
  c. Upon making a request, the maximum token cost for a query will be charged to your account. The difference between the actual token cost and the maximum token cost will be refunded when the search completes and you read the search data.
  d. Tokens are continually replenished. You can see the current number of tokens available in the `X-Historical-Tokens-Available` header, present on every response to these resources.
  e. Reading from the [historical index](/api/resources/historical_audits/read_the_contents_of_the_historical_index) does not consume any tokens.

### Parameters
- `created_since` () - **Required** - ISO8601 timestamp determining the beginning of the search range for historical changes
- `created_before` () - **Required** - ISO8601 timestamp determining the end of the search window for historical changes
- `auditable_id` () - Optional - Numeric ID of the record for which history should be retrieved
- `auditable_type` () - Optional - String identifier of the type of record for which history should be retrieved
- `associated_id` () - Optional - Numeric ID of the primary record for which history should be retrieved. Use these parameters to fetch only the history for secondary records, like descriptions and custom field values.
- `associated_type` () - Optional - String identifier of the type of the primary record for which history should be retrieved
- `audit_action` () - Optional - Type of action. Options are 'create', 'update', and 'destroy'
- `after_id` () - Optional - Numeric identifier which filters result record to only records with ID larger than the parameter. This can be used for cursor-based searches, and is more efficient than pagination for large data sets.
- `user_id` () - Optional - Numeric user ID, which searches only for audit records where one particular user was the actor

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/historical_audits" -d '{"search":{"created_since":"2019-01-01T00:00:00Z","created_before":"2019-01-01T00:00:00Z","auditable_type":"Feature","auditable_id":1007868956}}' -X POST \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "search_id": "6776757454428658092"
}
```

---

## Read the results of an audit search

**GET** `/api/v1/historical_audits/:search_id`

### Description
The historical audits endpoint is similar to the the Audits endpoint, but searches for audit records generated older than 12 calendar months ago. For searches of more recent data, the much more performant [Audits API](/api/resources/audits) should be used.

The [historical index](/api/resources/historical_audits/read_the_contents_of_the_historical_index) should first be used to identify time-periods of interest, and then a search can be conducted to fetch the full details of the audit records from that period.

There are two important caveats to using this API:
1. Searching through historical audits is an asynchronous operation. A search must first be [created](/api/resources/historical_audits/create_an_audit_search), and then the data may be [consumed later](/api/resources/historical_audits/read_the_results_of_an_audit_search)
2. Searching through historical audits imposes a stricter rate-limit than the general rate limit of the API. This API also enforces rate-limiting through a *token-based system.*
  a. Each Audits search consumes a specific number of tokens. The token cost of a search will be presented to the user through the [read results operation.](/api/resources/historical_audits/read_the_results_of_an_audit_search)
  b. The token cost of a request is only known after the search completes, and corresponds to the amount of data which was required to be scanned to fulfill the request. Specifying additional filters, such as `user_id`, `auditable_type`, and `audit_action` will decrease the token cost. 
  c. Upon making a request, the maximum token cost for a query will be charged to your account. The difference between the actual token cost and the maximum token cost will be refunded when the search completes and you read the search data.
  d. Tokens are continually replenished. You can see the current number of tokens available in the `X-Historical-Tokens-Available` header, present on every response to these resources.
  e. Reading from the [historical index](/api/resources/historical_audits/read_the_contents_of_the_historical_index) does not consume any tokens.

### Parameters
- `search_id` () - **Required** - The identifier returned from the [Create](/api/resources/historical_audits/create_an_audit_search) call
- `next_token` () - Optional - Pagination token returned from the previous call to this endpoint. This token is used to retrieve the next page of results.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/historical_audits/6776757454428607616" -X GET \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "audits": [
    {
      "id": "6776757454434427078",
      "audit_action": "update",
      "created_at": "2019-01-01T00:00:00.000Z",
      "interesting": true,
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      "contributors": [
        {
          "user": {
            "id": "1049303076",
            "name": "George Gently",
            "email": "no-reply@aha.io",
            "created_at": "2019-01-01T00:00:00.000Z",
            "updated_at": "2019-01-01T00:00:00.000Z"
          }
        }
      ],
      "auditable_type": "feature",
      "auditable_id": 1007868956,
      "associated_type": "release",
      "associated_id": 278327321,
      "description": "updated feature PRJ1-1 Changed feature name",
      "auditable_url": "https://company.aha.io:8338/features/PRJ1-1",
      "changes": [
        {
          "field_name": "Name",
          "value": "Feature 1 &rarr; Changed feature name"
        }
      ]
    }
  ],
  "running": false,
  "next_token": null,
  "results_complete": true
}
```

---
