# Ideas

## Create an idea

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","description":"\u003cp\u003eThis is the description\u003c/p\u003e","initial_votes":3}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149498133193",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 3,
    "initial_votes": 3,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149491007680",
      "body": "<p>This is the description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea without a submitted_idea_portal

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"skip_portal":true,"idea":{"name":"New idea","description":"\u003cp\u003eThis is the description\u003c/p\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149484567296",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149493505600",
      "body": "<p>This is the description</p>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Not visible in portals",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "integration_fields": []
  }
}
```

---

## Create an idea created by a ideas portal user

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","created_by_portal_user":{"id":384687358,"name":"Sammy Smith"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149487577144",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149489732632",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
    "product": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_portal_user": {
      "id": "384687358",
      "name": "Sammy Smith",
      "email": "sammy@smith.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "created_by_idea_user": {
      "id": "244576613",
      "name": "Sammy Smith",
      "email": "sammy@smith.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "assigned_to_user": null,
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with an admin response

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea with admin response","admin_response":"This is a new admin response \u003cb\u003ewith HTML\u003c/b\u003e"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149488893707",
    "name": "New idea with admin response",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149484741899",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "admin_response": {
      "id": "6776881149489925368",
      "body": "This is a new admin response <b>with HTML</b>",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": [],
      "responded_by_user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with a specific submitted_idea_portal

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","submitted_idea_portal_id":650606523}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149490549207",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149495498605",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with comma-separated tags

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","tags":"tag1, tag2"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149487402960",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149486351445",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [
      "tag1",
      "tag2"
    ],
    "full_tags": [
      {
        "id": "6776881149483963960",
        "name": "tag2",
        "color": "#52d3e0"
      },
      {
        "id": "6776881149493213277",
        "name": "tag1",
        "color": "#52e077"
      }
    ],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with watchers

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"fields":"*,watchers","idea":{"name":"New idea","watchers":"689956296,16338845"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149483698608",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149484442997",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "watchers": [
      {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "integration_fields": []
  }
}
```

---

## Create an idea with a score

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","score_facts":[{"name":"Benefit","value":10},{"name":"Effort","value":3}]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149486651286",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 13,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149489879059",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [
      {
        "id": "6776881149493035943",
        "value": 3,
        "name": "Effort"
      },
      {
        "id": "6776881149498224807",
        "value": 10,
        "name": "Benefit"
      }
    ],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with custom fields

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","custom_fields":{"priority":"P3"}}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149498597119",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149494338413",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [
      {
        "id": "6776881149486205536",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
      }
    ],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with a specific visibility

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","visibility":"public"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149490594303",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149494125544",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with a set creation date

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea","created_at":"2019-01-01T00:00:00Z"}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149491885999",
    "name": "New idea",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149485217306",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with a category

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea with category","categories":["Storage"]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149484843289",
    "name": "New idea with category",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149490979633",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [
      {
        "id": "552935478",
        "name": "Storage",
        "parent_id": null,
        "project_id": 131414752,
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## Create an idea with multiple categories

**POST** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal. We strongly suggest you set this if the creator is an idea user.
- `name` () - **Required** - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/ideas" -d '{"idea":{"name":"New idea with category","categories":["Storage","Usability"]}}' -X POST \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "6776881149498516261",
    "name": "New idea with category",
    "reference_num": "PRJ1-I-10",
    "score": 2,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
    "initial_votes": 0,
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "3259216",
      "name": "New",
      "position": 1,
      "complete": false,
      "color": "#dce7c6"
    },
    "description": {
      "id": "6776881149497744455",
      "body": "",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-10",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-10",
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
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [
      {
        "id": "251347229",
        "name": "Usability",
        "parent_id": null,
        "project_id": 131414752,
        "created_at": "2019-01-01T00:00:00.000Z"
      },
      {
        "id": "552935478",
        "name": "Storage",
        "parent_id": null,
        "project_id": 131414752,
        "created_at": "2019-01-01T00:00:00.000Z"
      }
    ],
    "custom_fields": [],
    "workflow_status_times": [
      {
        "status_id": "3259216",
        "status_name": "New",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://testideaportal1.ideas.aha.io:8338/ideas/PRJ1-I-10",
    "integration_fields": []
  }
}
```

---

## List ideas

**GET** `/api/v1/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `q` () - Optional - Search term to match against the idea name
- `spam` () - Optional - When true, shows ideas that have been marked as spam. By default, no spam ideas will be shown.
- `workflow_status` () - Optional - When present, filters to ideas with the provided workflow status ID or name.
- `sort` () - Optional - Sorting of the list of ideas. Accepted values are `recent`, `trending`, or `popular`.
- `created_before` () - Optional - UTC timestamp (in ISO8601 format). If provided, only ideas created before the timestamp will be returned.
- `created_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only ideas created after the timestamp will be returned.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only ideas updated or created after the timestamp will be returned.
- `tag` () - Optional - String tag value. If provided, only ideas with the associated tag will be returned.
- `user_id` () - Optional - ID of a user. If provided, only ideas created by that user will be returned.
- `idea_user_id` () - Optional - ID of an idea user. If provided, only ideas created by that idea user will be returned.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "ideas": [
    {
      "id": "58056975",
      "reference_num": "PRJ1-I-1",
      "name": "Idea 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
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
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-1",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-1"
    },
    {
      "id": "68691224",
      "reference_num": "PRJ1-I-12",
      "name": "Idea 5",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "6776881149496975329",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-12",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-12"
    },
    {
      "id": "140490859",
      "reference_num": "PRJ1-I-8",
      "name": "Some idea name 3",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "6776881149490339654",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-8",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-8"
    },
    {
      "id": "162120796",
      "reference_num": "PRJ1-I-5",
      "name": "Idea 4",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "478357480",
        "body": "Description of idea custom tables",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-5",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-5"
    },
    {
      "id": "245519441",
      "reference_num": "PRJ1-I-7",
      "name": "Some idea name 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "716451363",
        "body": "Description of idea endorsement 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-7",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-7"
    },
    {
      "id": "290908627",
      "reference_num": "PRJ1-I-9",
      "name": "Some idea name 4",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "6776881149487070955",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-9",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-9"
    },
    {
      "id": "397084149",
      "reference_num": "PRJ1-I-6",
      "name": "Some idea name 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "868056987",
        "body": "Description of idea endorsement 1",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-6",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-6"
    },
    {
      "id": "444379319",
      "reference_num": "PRJ1-I-2",
      "name": "Idea 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "378547141",
        "body": "Description of idea 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-2",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-2"
    },
    {
      "id": "731163180",
      "reference_num": "PRJ2-I-2",
      "name": "Idea 2 project 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "928262307",
        "body": "Description of idea 2 project2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ2-I-2",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ2-I-2"
    },
    {
      "id": "849214356",
      "reference_num": "PRJ2-I-1",
      "name": "Idea 1 project 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "5445688",
        "body": "Description of idea 1 project2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ2-I-1",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ2-I-1"
    },
    {
      "id": "857675141",
      "reference_num": "PRJ1-I-11",
      "name": "Idea 004",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "6776881149490209373",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-11",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-11"
    },
    {
      "id": "926598431",
      "reference_num": "PRJ5-I-1",
      "name": "Idea 1 Project 5",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "6776881149499801353",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ5-I-1",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ5-I-1"
    },
    {
      "id": "1055237874",
      "reference_num": "PRJ1-I-3",
      "name": "Idea 3 Merged",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "506957205",
        "body": "Description of idea 3",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-3",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-3"
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

## List ideas for a product

**GET** `/api/v1/products/:product_id/ideas`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `q` () - Optional - Search term to match against the idea name
- `spam` () - Optional - When true, shows ideas that have been marked as spam. By default, no spam ideas will be shown.
- `workflow_status` () - Optional - When present, filters to ideas with the provided workflow status ID or name.
- `sort` () - Optional - Sorting of the list of ideas. Accepted values are `recent`, `trending`, or `popular`.
- `created_before` () - Optional - UTC timestamp (in ISO8601 format). If provided, only ideas created before the timestamp will be returned.
- `created_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only ideas created after the timestamp will be returned.
- `updated_since` () - Optional - UTC timestamp (in ISO8601 format). If provided, only ideas updated or created after the timestamp will be returned.
- `tag` () - Optional - String tag value. If provided, only ideas with the associated tag will be returned.
- `user_id` () - Optional - ID of a user. If provided, only ideas created by that user will be returned.
- `idea_user_id` () - Optional - ID of an idea user. If provided, only ideas created by that idea user will be returned.

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/ideas" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "ideas": [
    {
      "id": "58056975",
      "reference_num": "PRJ1-I-1",
      "name": "Idea 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
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
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-1",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-1"
    },
    {
      "id": "68691224",
      "reference_num": "PRJ1-I-12",
      "name": "Idea 5",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "6776881149489796142",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-12",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-12"
    },
    {
      "id": "162120796",
      "reference_num": "PRJ1-I-5",
      "name": "Idea 4",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "478357480",
        "body": "Description of idea custom tables",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-5",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-5"
    },
    {
      "id": "444379319",
      "reference_num": "PRJ1-I-2",
      "name": "Idea 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "378547141",
        "body": "Description of idea 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-2",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-2"
    },
    {
      "id": "857675141",
      "reference_num": "PRJ1-I-11",
      "name": "Idea 004",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      "description": {
        "id": "6776881149494497309",
        "body": "",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-11",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-11"
    },
    {
      "id": "1055237874",
      "reference_num": "PRJ1-I-3",
      "name": "Idea 3 Merged",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "506957205",
        "body": "Description of idea 3",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-3",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-3"
    }
  ],
  "pagination": {
    "total_records": 6,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Get a specific idea

**GET** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -X GET \
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

**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -X GET \
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
    "admin_response": {
      "id": "6776881149495006288",
      "body": "This is a great idea! We'll get started right away.",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": [],
      "responded_by_user": {
        "id": "530313708",
        "name": "Bill Billings",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
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

## Get a specific idea with plain text body

**GET** `/api/v1/ideas/:id?fields=description,plain_text_body`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-1?fields=description,plain_text_body" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "58056975",
    "product_id": "131414752",
    "description": {
      "id": "103757394",
      "body": "<p>Description of idea 1</p>",
      "plain_text_body": "Description of idea 1"
    }
  }
}
```

---

## Get duplicates of a specific idea

**GET** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-2" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "444379319",
    "name": "Idea 2",
    "reference_num": "PRJ1-I-2",
    "score": 0,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 2,
    "initial_votes": 1,
    "status_changed_at": null,
    "workflow_status": {
      "id": "1009437757",
      "name": "In progress",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "description": {
      "id": "378547141",
      "body": "Description of idea 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "duplicates": [
      {
        "id": "1055237874",
        "reference_num": "PRJ1-I-3",
        "name": "Idea 3 Merged",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "workflow_status": {
          "id": "1009437757",
          "name": "In progress",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        "description": {
          "id": "506957205",
          "body": "Description of idea 3",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "url": "http://company.aha.io/ideas/ideas/PRJ1-I-3",
        "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-3"
      }
    ],
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-2",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-2",
    "product": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "created_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
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
    "endorsements_count": 1,
    "comments_count": 12,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "submitted_idea_portal_record_url": "https://ideas.example.com:8338/ideas/PRJ1-I-2",
    "integration_fields": []
  }
}
```

**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-2" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "444379319",
    "name": "Idea 2",
    "reference_num": "PRJ1-I-2",
    "score": 0,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 2,
    "initial_votes": 1,
    "status_changed_at": null,
    "workflow_status": {
      "id": "1009437757",
      "name": "In progress",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "description": {
      "id": "378547141",
      "body": "Description of idea 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "duplicates": [
      {
        "id": "1055237874",
        "reference_num": "PRJ1-I-3",
        "name": "Idea 3 Merged",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "workflow_status": {
          "id": "1009437757",
          "name": "In progress",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        "description": {
          "id": "506957205",
          "body": "Description of idea 3",
          "created_at": "2019-01-01T00:00:00.000Z",
          "updated_at": "2019-01-01T00:00:00.000Z",
          "attachments": []
        },
        "url": "http://company.aha.io/ideas/ideas/PRJ1-I-3",
        "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-3"
      }
    ],
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-2",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-2",
    "product": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "created_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "assigned_to_user": {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "default_assignee": false
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
    "endorsements_count": 1,
    "comments_count": 12,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "submitted_idea_portal_record_url": "https://ideas.example.com:8338/ideas/PRJ1-I-2",
    "integration_fields": []
  }
}
```

---

## Get a specific idea that is merged (has a duplicate_of)

**GET** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-3" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "1055237874",
    "name": "Idea 3 Merged",
    "reference_num": "PRJ1-I-3",
    "score": 0,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 2,
    "initial_votes": 2,
    "status_changed_at": null,
    "workflow_status": {
      "id": "1009437757",
      "name": "In progress",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "description": {
      "id": "506957205",
      "body": "Description of idea 3",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "duplicate_of": {
      "id": "444379319",
      "reference_num": "PRJ1-I-2",
      "name": "Idea 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "378547141",
        "body": "Description of idea 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-2",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-2"
    },
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-3",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-3",
    "product": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "created_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "assigned_to_user": null,
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "submitted_idea_portal_record_url": "https://ideas.example.com:8338/ideas/PRJ1-I-3",
    "integration_fields": []
  }
}
```

**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/PRJ1-I-3" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "1055237874",
    "name": "Idea 3 Merged",
    "reference_num": "PRJ1-I-3",
    "score": 0,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 2,
    "initial_votes": 2,
    "status_changed_at": null,
    "workflow_status": {
      "id": "1009437757",
      "name": "In progress",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
    },
    "description": {
      "id": "506957205",
      "body": "Description of idea 3",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "duplicate_of": {
      "id": "444379319",
      "reference_num": "PRJ1-I-2",
      "name": "Idea 2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "workflow_status": {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      },
      "description": {
        "id": "378547141",
        "body": "Description of idea 2",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z",
        "attachments": []
      },
      "url": "http://company.aha.io/ideas/ideas/PRJ1-I-2",
      "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-2"
    },
    "url": "http://company.aha.io/ideas/ideas/PRJ1-I-3",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ1-I-3",
    "product": {
      "id": "131414752",
      "reference_prefix": "PRJ1",
      "name": "Project 1",
      "product_line": false,
      "created_at": "2019-01-01T00:00:00.000Z",
      "workspace_type": "product_workspace",
      "url": "http://company.aha.io/projects/PRJ1"
    },
    "created_by_portal_user": {
      "id": "646391926",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "created_by_idea_user": {
      "id": "1056507375",
      "name": "John Long",
      "email": "john@long.com",
      "created_at": "2019-01-01T00:00:00.000Z"
    },
    "assigned_to_user": null,
    "feature": {
      "id": "1007868956",
      "reference_num": "PRJ1-1",
      "name": "Feature 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-1",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-1",
      "product_id": "131414752"
    },
    "endorsements_count": 0,
    "comments_count": 0,
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [],
    "submitted_idea_portal_record_url": "https://ideas.example.com:8338/ideas/PRJ1-I-3",
    "integration_fields": []
  }
}
```

---

## List ideas related to a particular term

**GET** `/api/v1/ideas/related`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `q` () - Optional - Query string to search against idea name, description or ID

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/ideas/related?q=ideas+are+a+dime+a+dozen" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "ideas": [],
  "pagination": {
    "total_records": 0,
    "total_pages": 0,
    "current_page": 1
  }
}
```

---

## Update an idea

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"name":"New idea name","description":"New description"}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "58056975",
    "name": "New idea name",
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
      "body": "New description",
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

## Update an idea's submitted_idea_portal

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"submitted_idea_portal_id":1070474755}}' -X PUT \
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

## Update an idea's custom fields

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"custom_fields":{"priority":"P3"}}}' -X PUT \
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
        "id": "6776881149497736437",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
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

## Update an idea's custom fields with an array value

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"custom_fields":[{"key":"priority","value":"P3"}]}}' -X PUT \
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
        "id": "6776881149496785120",
        "key": "priority",
        "name": "Priority",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "P3",
        "type": "string"
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

## Update an idea's visibility

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"visibility":"public"}}' -X PUT \
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

## Update a idea's watchers

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"watchers":[689956296]}}' -X PUT \
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

## Mark an idea as spam

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"spam":true}}' -X PUT \
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

## Un-promote an idea from a feature

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"feature":null}}' -X PUT \
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

## Un-promote an idea from an epic

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"epic":null}}' -X PUT \
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

## Un-promote an idea from an initiative

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '{"idea":{"initiative":null}}' -X PUT \
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

## Move an idea to a different workspace

**PUT** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `submitted_idea_portal_id` () - Optional - Numeric ID of the ideas portal
- `name` () - Optional - Name of the idea
- `description` () - Optional - Description of the idea — may include HTML formatting.
- `workflow_status` () - Optional - Status of the idea — must be a valid status for the selected product.
- `tags` () - Optional - Tags to add to the idea. Multiple tags must be separated by commas.
- `categories` () - Optional - Names of any existing categories the idea should be assigned to. Multiple categories must be separated by commas.
- `created_by` () - **Required** - Email address of user who created the idea — does not need to be an Aha! user email.
- `assigned_to_user` () - Optional - Email address of user that is assigned the idea.
- `feature` () - Optional - Name or ID of the feature that the idea was promoted to
- `initiative` () - Optional - Name or ID of the initiative that the idea was promoted to
- `epic` () - Optional - Name or ID of the epic that the idea was promoted to
- `duplicate_idea` () - Optional - Idea ID or key for an idea which this idea duplicates. Setting this value will merge this idea into the provided idea ID; setting it to a null or blank value will unmerge this idea. Note that in the API response, this attribute is called duplicate_of.
- `initial_votes` () - Optional - Number of votes to seed the vote count with when importing from other systems
- `visibility` () - Optional - Initial visibility of the idea (aha, creator, employee, employee_or_creator, creator_organization, or public - aha is the default)
- `created_at` () - Optional - Date of idea creation. In UTC timezone with format YYYY-MM-DD or YYYY-MM-DD HH:MM:SS.
- `spam` () - Optional - Whether the idea is considered spam. Must be 'true' or 'false'

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ2-I-1" -d '{"idea":{"project_id":131414752}}' -X PUT \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "idea": {
    "id": "849214356",
    "name": "Idea 1 project 2",
    "reference_num": "PRJ2-I-1",
    "score": 15,
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "product_id": "131414752",
    "votes": 0,
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
      "id": "5445688",
      "body": "Description of idea 1 project2",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "attachments": []
    },
    "visibility": "Visible to all ideas portal users",
    "url": "http://company.aha.io/ideas/ideas/PRJ2-I-1",
    "resource": "http://company.aha.io/api/v1/ideas/PRJ2-I-1",
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
    "score_facts": [],
    "tags": [],
    "full_tags": [],
    "categories": [],
    "custom_fields": [
      {
        "id": 549257455,
        "key": "text_field1",
        "name": "TextField1",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Marrakech",
        "type": "string"
      },
      {
        "id": 968118615,
        "key": "text_field2",
        "name": "TextField2",
        "updatedAt": "2019-01-01T00:00:00Z",
        "value": "Lyon",
        "type": "string"
      }
    ],
    "submitted_idea_portal_record_url": "https://ideas999999.example.com:8338/ideas/PRJ2-I-1",
    "integration_fields": []
  }
}
```

---

## Promote an idea

**PUT** `/api/v1/ideas/:id/promote`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea
- `promotable_type` () - **Required** - Specify what to promote the idea to. Allowed values: epic, feature, initiative, requirement
- `release_id` () - Optional - Numeric ID or key of a release. Required when promoting to features/epics.
- `feature_id` () - Optional - Numeric ID or key of a feature. Required when promoting to requirements.
- `product_id` () - Optional - Numeric ID or key of the product. Required when promoting to initiatives.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1/promote" -d '{"promotable_type":"feature","release_id":278327321}' -X PUT \
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
    "status_changed_at": "2019-01-01T00:00:00.000Z",
    "workflow_status": {
      "id": "1009437757",
      "name": "In progress",
      "position": 2,
      "complete": false,
      "color": "#ecdd8f"
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
    "feature": {
      "id": "6776881149484319461",
      "reference_num": "PRJ1-251",
      "name": "Idea 1",
      "created_at": "2019-01-01T00:00:00.000Z",
      "url": "http://company.aha.io/features/PRJ1-251",
      "resource": "http://company.aha.io/api/v1/features/PRJ1-251",
      "product_id": "131414752"
    },
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
    "workflow_status_times": [
      {
        "status_id": "1009437757",
        "status_name": "In progress",
        "started_at": "2019-01-01T00:00:00.000Z",
        "ended_at": null
      }
    ],
    "submitted_idea_portal_record_url": "https://ideas.example.com:8338/ideas/PRJ1-I-1",
    "integration_fields": []
  }
}
```

---

## Delete an idea

**DELETE** `/api/v1/ideas/:id`

### Description
When creating an idea where the creator is an idea user we strongly suggest
to provide the `submitted_idea_portal_id` attribute to the idea
to ensure that the idea is created in the correct ideas portal and the user
gets access to the portal.

If you don't want the idea to be submitted to any portal, you can skip this
by setting `skip_portal: true` in the request body.


### Parameters
- `id` () - **Required** - Numeric ID or key of the idea

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/ideas/PRJ1-I-1" -d '' -X DELETE \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

---
