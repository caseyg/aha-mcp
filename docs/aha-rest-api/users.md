# Users

## Create a user

**POST** `/api/v1/products/:product_id/users`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `first_name` () - **Required** - First name of the user to be created
- `last_name` () - **Required** - Last name of the user to be created
- `email` () - **Required** - Email of the user to be created
- `role` () - **Required** - Permissions of the user to be created in the product one of: product_owner, contributor, reviewer, viewer, none
- `identity_provider_id` () - Optional - The ID of the identity provider that will be used for this user. Not required if user will use a password.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/users" -d '{"user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe","role":"product_owner"}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role": 20,
  "role_description": "Owner",
  "user": {
    "id": "6776757454431877834",
    "name": "sam doe",
    "email": "sam.doe@example.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## Create a contributor user

**POST** `/api/v1/products/:product_id/users`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `first_name` () - **Required** - First name of the user to be created
- `last_name` () - **Required** - Last name of the user to be created
- `email` () - **Required** - Email of the user to be created
- `role` () - **Required** - Permissions of the user to be created in the product one of: product_owner, contributor, reviewer, viewer, none
- `identity_provider_id` () - Optional - The ID of the identity provider that will be used for this user. Not required if user will use a password.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/users" -d '{"user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe","role":"contributor"}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role": 30,
  "role_description": "Contributor",
  "user": {
    "id": "6776757454439815093",
    "name": "sam doe",
    "email": "sam.doe@example.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## Create a viewer user

**POST** `/api/v1/products/:product_id/users`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `first_name` () - **Required** - First name of the user to be created
- `last_name` () - **Required** - Last name of the user to be created
- `email` () - **Required** - Email of the user to be created
- `role` () - **Required** - Permissions of the user to be created in the product one of: product_owner, contributor, reviewer, viewer, none
- `identity_provider_id` () - Optional - The ID of the identity provider that will be used for this user. Not required if user will use a password.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/users" -d '{"user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe","role":"viewer"}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role": 50,
  "role_description": "Viewer",
  "user": {
    "id": "6776757454426723533",
    "name": "sam doe",
    "email": "sam.doe@example.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## Create a user with an identity provider ID

**POST** `/api/v1/products/:product_id/users`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `first_name` () - **Required** - First name of the user to be created
- `last_name` () - **Required** - Last name of the user to be created
- `email` () - **Required** - Email of the user to be created
- `role` () - **Required** - Permissions of the user to be created in the product one of: product_owner, contributor, reviewer, viewer, none
- `identity_provider_id` () - Optional - The ID of the identity provider that will be used for this user. Not required if user will use a password.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/users" -d '{"user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe","role":"product_owner","identity_provider_id":483954339}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role": 20,
  "role_description": "Owner",
  "user": {
    "id": "6776757454437155797",
    "name": "sam doe",
    "email": "sam.doe@example.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## Create a user with a password access

**POST** `/api/v1/products/:product_id/users`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product
- `first_name` () - **Required** - First name of the user to be created
- `last_name` () - **Required** - Last name of the user to be created
- `email` () - **Required** - Email of the user to be created
- `role` () - **Required** - Permissions of the user to be created in the product one of: product_owner, contributor, reviewer, viewer, none
- `identity_provider_id` () - Optional - The ID of the identity provider that will be used for this user. Not required if user will use a password.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/products/PRJ1/users" -d '{"user":{"email":"sam.doe@example.com","first_name":"sam","last_name":"doe","role":"product_owner"}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role": 20,
  "role_description": "Owner",
  "user": {
    "id": "6776757454438125578",
    "name": "sam doe",
    "email": "sam.doe@example.com",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z"
  }
}
```

---

## List users

**GET** `/api/v1/users`

### Description
**[Custom roles](https://www.aha.io/support/roadmaps/account/billing-and-users/custom-user-permission-roles) are an Enterprise+ exclusive feature.**


### Parameters
- `email` () - Optional - Email address to filter users by

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/users" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "users": [
    {
      "id": "16338845",
      "name": "John Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 50,
          "role_description": "Viewer",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "37063167",
      "name": "No Projects",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": true,
        "administer_configuration": true
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "82352673",
      "name": "Bob Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "131414752",
          "product_name": "Project 1"
        },
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "517761884",
          "product_name": null
        },
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "610602692",
          "product_name": null
        },
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "787060436",
          "product_name": null
        },
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "682804944",
          "product_name": null
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": false,
        "administer_configuration": true
      },
      "paid_seat_group": {
        "id": 572805993,
        "name": "Group 2"
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "126225962",
      "name": "Multi Account",
      "email": "mulit-account@trial-account.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": true,
        "administer_configuration": true
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "267654265",
      "name": "John's First (\"name\") \u79c1 Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "268195287",
      "name": "Super Admin",
      "email": "admin@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "289520357",
      "name": "John Doe",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 30,
          "role_description": "Contributor",
          "product_id": "131414752",
          "product_name": "Project 1"
        },
        {
          "role": 50,
          "role_description": "Viewer",
          "product_id": "517761884",
          "product_name": null
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "349538572",
      "name": "Sally Sane",
      "email": "sally.sane@account2.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 30,
          "role_description": "Contributor",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "373433676",
      "name": "Jim Jingles",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": true,
        "administer_configuration": true
      },
      "paid_seat_group": {
        "id": 992805589,
        "name": "Group 1"
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "375285024",
      "name": "Gregory McSmith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 35,
          "role_description": "Developer",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "435166761",
      "name": "Jane Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 50,
          "role_description": "Viewer",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "501775768",
      "name": "Frank Sane",
      "email": "frank.sane@account2.com",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "530313708",
      "name": "Bill Billings",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": true,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "601067208",
      "name": "Jeremy Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 40,
          "role_description": "Reviewer",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "689956296",
      "name": "Henry Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": "2019-01-01T00:00:00.000Z",
      "product_roles": [
        {
          "role": 30,
          "role_description": "Contributor",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "733218216",
      "name": "Everso Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": true,
        "administer_configuration": true
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "787951284",
      "name": "Jeremy Thompson",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 50,
          "role_description": "Viewer",
          "product_id": "1040810565",
          "product_name": null
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "869174989",
      "name": "Dirk Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": true,
        "administer_configuration": true
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "871344824",
      "name": "Joan Smith",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": false,
        "administer_configuration": true
      },
      "paid_seat_group": {
        "id": 572805993,
        "name": "Group 2"
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "1020675218",
      "name": "Mary Humpty",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": "2019-01-01T00:00:00.000Z",
      "product_roles": [
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "131414752",
          "product_name": "Project 1"
        },
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "517761884",
          "product_name": null
        },
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "610602692",
          "product_name": null
        }
      ],
      "user_roles": [],
      "enabled": true,
      "paid_seat": true,
      "administrator": false,
      "administrator_roles": {
        "administer_account": false,
        "administer_billing": false,
        "administer_configuration": false
      },
      "identity_provider": {
        "type": "password"
      }
    },
    {
      "id": "1049303076",
      "name": "George Gently",
      "email": "no-reply@aha.io",
      "created_at": "2019-01-01T00:00:00.000Z",
      "updated_at": "2019-01-01T00:00:00.000Z",
      "accessed_at": null,
      "product_roles": [
        {
          "role": 20,
          "role_description": "Owner",
          "product_id": "131414752",
          "product_name": "Project 1"
        }
      ],
      "user_roles": [
        {
          "role_id": 409541421,
          "name": "Project scoped role 1",
          "scope": {
            "type": "project",
            "name": "Account 1",
            "id": 303742481
          }
        }
      ],
      "enabled": true,
      "paid_seat": true,
      "administrator": true,
      "administrator_roles": {
        "administer_account": true,
        "administer_billing": true,
        "administer_configuration": true
      },
      "identity_provider": {
        "type": "password"
      }
    }
  ],
  "pagination": {
    "total_records": 21,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## List users associated with a product

**GET** `/api/v1/products/:product_id/users`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/users" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab"
```

**Response:**
```json
{
  "project_users": [
    {
      "role": 50,
      "role_description": "Viewer",
      "user": {
        "id": "16338845",
        "name": "John Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 20,
      "role_description": "Owner",
      "user": {
        "id": "82352673",
        "name": "Bob Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 30,
      "role_description": "Contributor",
      "user": {
        "id": "289520357",
        "name": "John Doe",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 30,
      "role_description": "Contributor",
      "user": {
        "id": "349538572",
        "name": "Sally Sane",
        "email": "sally.sane@account2.com",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 35,
      "role_description": "Developer",
      "user": {
        "id": "375285024",
        "name": "Gregory McSmith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 50,
      "role_description": "Viewer",
      "user": {
        "id": "435166761",
        "name": "Jane Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 40,
      "role_description": "Reviewer",
      "user": {
        "id": "601067208",
        "name": "Jeremy Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 30,
      "role_description": "Contributor",
      "user": {
        "id": "689956296",
        "name": "Henry Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 20,
      "role_description": "Owner",
      "user": {
        "id": "871344824",
        "name": "Joan Smith",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 20,
      "role_description": "Owner",
      "user": {
        "id": "1020675218",
        "name": "Mary Humpty",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
    },
    {
      "role": 20,
      "role_description": "Owner",
      "user": {
        "id": "1049303076",
        "name": "George Gently",
        "email": "no-reply@aha.io",
        "created_at": "2019-01-01T00:00:00.000Z",
        "updated_at": "2019-01-01T00:00:00.000Z"
      }
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

## Get a specific user

**GET** `/api/v1/users/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/users/1049303076" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "user": {
    "id": "1049303076",
    "name": "George Gently",
    "email": "no-reply@aha.io",
    "created_at": "2019-01-01T00:00:00.000Z",
    "updated_at": "2019-01-01T00:00:00.000Z",
    "accessed_at": null,
    "product_roles": [
      {
        "role": 20,
        "role_description": "Owner",
        "product_id": "131414752",
        "product_name": "Project 1"
      }
    ],
    "enabled": true,
    "paid_seat": true,
    "administrator": true,
    "administrator_roles": {
      "administer_account": true,
      "administer_billing": true,
      "administer_configuration": true
    },
    "identity_provider": {
      "type": "password"
    }
  }
}
```

---

## Update a user

**PUT** `/api/v1/users/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the user
- `first_name` () - Optional - First name of the user
- `last_name` () - Optional - Last name of the user
- `email` () - Optional - Email of the user
- `enabled` () - Optional - Sets whether the user is enabled
- `administrator` () - Optional - Sets all administrator roles for the user. Must be 'true' or 'false'.
- `administrator_roles` () - Optional - Sets individual administrator roles for the user. Options are: 'administer_account', 'administer_billing', 'administer_configuration'. Must be 'true' or 'false'.

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/users/1020675218" -d '{"user":{"first_name":"Sarah","enabled":false}}' -X PUT \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "id": "1020675218",
  "name": "Sarah Humpty",
  "email": "no-reply@aha.io",
  "created_at": "2019-01-01T00:00:00.000Z",
  "updated_at": "2019-01-01T00:00:00.000Z",
  "accessed_at": "2019-01-01T00:00:00.000Z",
  "product_roles": [
    {
      "role": 20,
      "role_description": "Owner",
      "product_id": "131414752",
      "product_name": "Project 1"
    },
    {
      "role": 20,
      "role_description": "Owner",
      "product_id": "517761884",
      "product_name": null
    },
    {
      "role": 20,
      "role_description": "Owner",
      "product_id": "610602692",
      "product_name": null
    }
  ],
  "enabled": false,
  "paid_seat": true,
  "administrator": false,
  "administrator_roles": {
    "administer_account": false,
    "administer_billing": false,
    "administer_configuration": false
  },
  "identity_provider": {
    "type": "password"
  }
}
```

---

## List a user's product roles

**GET** `/api/v1/users/:id/product_roles`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/users/1049303076/product_roles" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "product_roles": [
    {
      "role": 20,
      "role_description": "Owner",
      "product_id": "131414752",
      "product_name": "Project 1"
    }
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Update a user's product roles

**POST** `/api/v1/users/:id/product_roles`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/users/1020675218/product_roles" -d '{"product_role":{"role":"product_owner","product_id":"PRJ3"}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role": 20,
  "role_description": "Owner",
  "product_id": "702241743",
  "product_name": null
}
```

---

## Delete a user's product role

**DELETE** `/api/v1/users/:id/product_roles/:product_id`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/users/1020675218/product_roles/131414752" -d '' -X DELETE \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

---

## List a user's custom roles

**GET** `/api/v1/users/:id/user_roles`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/users/1049303076/user_roles" -X GET \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "user_roles": [
    {
      "role_id": 409541421,
      "name": "Project scoped role 1",
      "scope": {
        "type": "project",
        "name": "Project 1",
        "id": 131414752
      }
    }
  ],
  "pagination": {
    "total_records": 1,
    "total_pages": 1,
    "current_page": 1
  }
}
```

---

## Update a user's custom roles

**POST** `/api/v1/users/:id/user_roles`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/users/1049303076/user_roles" -d '{"user_role":{"custom_role_id":409541421,"product_id":131414752}}' -X POST \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

**Response:**
```json
{
  "role_id": 409541421,
  "name": "Project scoped role 1",
  "scope": {
    "type": "project",
    "name": "Project 1",
    "id": 131414752
  }
}
```

---

## Delete a user's custom role

**DELETE** `/api/v1/users/:id/user_roles/:product_id`

### Parameters
- `id` () - **Required** - Numeric ID of the user

### Example
**Request:**
```bash
curl "https://company.aha.io/api/v1/users/1020675218/user_roles/131414752" -d '' -X DELETE \
	-H "Content-Type: application/json" \
	-H "Accept: application/json" \
	-H "Authorization: Bearer 584b6d6b83405011f8c6903d2379f4afdf824cef867db391b7bcb5995f603a76"
```

---
