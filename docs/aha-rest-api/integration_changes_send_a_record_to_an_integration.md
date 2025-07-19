# Integration changes

## Send a record to an integration

**POST** `/api/v1/integration_changes`

### Description
This endpoint mimicks the "Send to integration" button on a record in the UI.


### Parameters
- `integration_id` () - **Required** - Record ID of the integration.
- `model_class` () - **Required** - Record type name of the record to send - Feature, Epic, Release, etc...
- `model_id` () - **Required** - Record ID of the model to send.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/integration_changes" -d '{"integration_id":204584239,"model_class":"Feature","model_id":1007868956}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "status": "success"
}
```

---
