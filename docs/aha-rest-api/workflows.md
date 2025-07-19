# Workflows

## List workflows

**GET** `/api/v1/products/:product_id/workflows`

### Parameters
- `product_id` () - **Required** - Numeric ID or key of the product

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/workflows" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "workflows": [
    {
      "id": 61191651,
      "name": "Account initiative workflow",
      "statusable_type": "Initiative",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "53968949",
          "name": "Not Started",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "851912549",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136128",
          "name": "Sample 15",
          "position": 17,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136148",
          "name": "Sample 3",
          "position": 5,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136158",
          "name": "Sample 1",
          "position": 3,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136168",
          "name": "Sample 2",
          "position": 4,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136178",
          "name": "Sample 14",
          "position": 16,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881408",
          "name": "Sample 12",
          "position": 14,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881428",
          "name": "Sample 7",
          "position": 9,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881438",
          "name": "Sample 5",
          "position": 7,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881448",
          "name": "Sample 4",
          "position": 6,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166979456424024",
          "name": "Sample 19",
          "position": 21,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166979457568121",
          "name": "Sample 16",
          "position": 18,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983749861123",
          "name": "Sample 18",
          "position": 20,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983750348036",
          "name": "Sample 20",
          "position": 22,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983752519805",
          "name": "Sample 17",
          "position": 19,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983754160302",
          "name": "Sample 21",
          "position": 23,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275675082840",
          "name": "Sample 13",
          "position": 15,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275678580297",
          "name": "Sample 11",
          "position": 13,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275679470036",
          "name": "Sample 10",
          "position": 12,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275679792248",
          "name": "Sample 9",
          "position": 11,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053284264084983",
          "name": "Sample 8",
          "position": 10,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053284269398016",
          "name": "Sample 6",
          "position": 8,
          "complete": false,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "196299900",
          "name": "Improvement"
        },
        {
          "id": "654498607",
          "name": "New"
        }
      ]
    },
    {
      "id": 80245244,
      "name": "Account product idea workflow",
      "statusable_type": "Idea",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "3259216",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "349486678",
          "name": "Shipped",
          "position": 4,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "509459046",
          "name": "Done",
          "position": 4,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "1009437757",
          "name": "In progress",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "1809278",
          "name": "Improvement"
        },
        {
          "id": "787053401",
          "name": "New"
        }
      ]
    },
    {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "118531893",
          "name": "Already Exists",
          "position": 7,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "327385593",
          "name": "In progress",
          "position": 3,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "348961883",
          "name": "Won't Do",
          "position": 6,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "597153450",
          "name": "Done",
          "position": 4,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "922838743",
          "name": "Not started",
          "position": 8,
          "complete": false,
          "color": "#dce790"
        },
        {
          "id": "934242751",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "962984386",
          "name": "Designed",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "1025247908",
          "name": "Shipped",
          "position": 5,
          "complete": true,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "98484309",
          "name": "New"
        },
        {
          "id": "714950177",
          "name": "Improvement"
        }
      ]
    },
    {
      "id": 717623509,
      "name": "Account product release workflow",
      "statusable_type": "Release",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "738862546",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "920959666",
          "name": "In progress",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "1040256814",
          "name": "Shipped",
          "position": 3,
          "complete": true,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "97513727",
          "name": "Improvement"
        },
        {
          "id": "706521964",
          "name": "New"
        },
        {
          "id": "6053108729101086872",
          "name": "Sample 1"
        }
      ]
    },
    {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "412273758",
          "name": "Not Started",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        }
      ],
      "workflow_kinds": [
        {
          "id": "146845716",
          "name": "New"
        },
        {
          "id": "618789532",
          "name": "Improvement"
        }
      ]
    },
    {
      "id": 1024772447,
      "name": "Account product key result workflow",
      "statusable_type": "KeyResult",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "76947914",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "496533981",
          "name": "Not Started",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        }
      ],
      "workflow_kinds": [
        {
          "id": "318525598",
          "name": "New"
        },
        {
          "id": "941130642",
          "name": "Improvement"
        }
      ]
    }
  ]
}
```

**Request:**
```bash
curl -g "https://company.aha.io/api/v1/products/PRJ1/workflows" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "workflows": [
    {
      "id": 61191651,
      "name": "Account initiative workflow",
      "statusable_type": "Initiative",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "53968949",
          "name": "Not Started",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "851912549",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136128",
          "name": "Sample 15",
          "position": 17,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136148",
          "name": "Sample 3",
          "position": 5,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136158",
          "name": "Sample 1",
          "position": 3,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136168",
          "name": "Sample 2",
          "position": 4,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "398063383401136178",
          "name": "Sample 14",
          "position": 16,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881408",
          "name": "Sample 12",
          "position": 14,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881428",
          "name": "Sample 7",
          "position": 9,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881438",
          "name": "Sample 5",
          "position": 7,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "420001850772881448",
          "name": "Sample 4",
          "position": 6,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166979456424024",
          "name": "Sample 19",
          "position": 21,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166979457568121",
          "name": "Sample 16",
          "position": 18,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983749861123",
          "name": "Sample 18",
          "position": 20,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983750348036",
          "name": "Sample 20",
          "position": 22,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983752519805",
          "name": "Sample 17",
          "position": 19,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6001166983754160302",
          "name": "Sample 21",
          "position": 23,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275675082840",
          "name": "Sample 13",
          "position": 15,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275678580297",
          "name": "Sample 11",
          "position": 13,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275679470036",
          "name": "Sample 10",
          "position": 12,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053275679792248",
          "name": "Sample 9",
          "position": 11,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053284264084983",
          "name": "Sample 8",
          "position": 10,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "6013053284269398016",
          "name": "Sample 6",
          "position": 8,
          "complete": false,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "196299900",
          "name": "Improvement"
        },
        {
          "id": "654498607",
          "name": "New"
        }
      ]
    },
    {
      "id": 80245244,
      "name": "Account product idea workflow",
      "statusable_type": "Idea",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "3259216",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "349486678",
          "name": "Shipped",
          "position": 4,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "509459046",
          "name": "Done",
          "position": 4,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "1009437757",
          "name": "In progress",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "1809278",
          "name": "Improvement"
        },
        {
          "id": "787053401",
          "name": "New"
        }
      ]
    },
    {
      "id": 499195972,
      "name": "Account product feature workflow",
      "statusable_type": "Feature",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "118531893",
          "name": "Already Exists",
          "position": 7,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "327385593",
          "name": "In progress",
          "position": 3,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "348961883",
          "name": "Won't Do",
          "position": 6,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "597153450",
          "name": "Done",
          "position": 4,
          "complete": true,
          "color": "#ecdd8f"
        },
        {
          "id": "922838743",
          "name": "Not started",
          "position": 8,
          "complete": false,
          "color": "#dce790"
        },
        {
          "id": "934242751",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "962984386",
          "name": "Designed",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "1025247908",
          "name": "Shipped",
          "position": 5,
          "complete": true,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "98484309",
          "name": "New"
        },
        {
          "id": "714950177",
          "name": "Improvement"
        }
      ]
    },
    {
      "id": 717623509,
      "name": "Account product release workflow",
      "statusable_type": "Release",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "738862546",
          "name": "New",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        },
        {
          "id": "920959666",
          "name": "In progress",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "1040256814",
          "name": "Shipped",
          "position": 3,
          "complete": true,
          "color": "#ecdd8f"
        }
      ],
      "workflow_kinds": [
        {
          "id": "97513727",
          "name": "Improvement"
        },
        {
          "id": "706521964",
          "name": "New"
        },
        {
          "id": "6053108729101086872",
          "name": "Sample 1"
        }
      ]
    },
    {
      "id": 883066232,
      "name": "Account goal workflow",
      "statusable_type": "StrategicImperative",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "396368932",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "412273758",
          "name": "Not Started",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        }
      ],
      "workflow_kinds": [
        {
          "id": "146845716",
          "name": "New"
        },
        {
          "id": "618789532",
          "name": "Improvement"
        }
      ]
    },
    {
      "id": 1024772447,
      "name": "Account product key result workflow",
      "statusable_type": "KeyResult",
      "transitions_only": false,
      "workflow_statuses": [
        {
          "id": "76947914",
          "name": "On Track",
          "position": 2,
          "complete": false,
          "color": "#ecdd8f"
        },
        {
          "id": "496533981",
          "name": "Not Started",
          "position": 1,
          "complete": false,
          "color": "#dce7c6"
        }
      ],
      "workflow_kinds": [
        {
          "id": "318525598",
          "name": "New"
        },
        {
          "id": "941130642",
          "name": "Improvement"
        }
      ]
    }
  ]
}
```

---

## Get a specific workflow

**GET** `/api/v1/workflows/:id`

### Parameters
- `id` () - **Required** - Numeric ID of the workflow 

### Example
**Request:**
```bash
curl -g "https://company.aha.io/api/v1/workflows/80245244" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "workflow": {
    "id": 80245244,
    "name": "Account product idea workflow",
    "statusable_type": "Idea",
    "transitions_only": false,
    "workflow_statuses": [
      {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      {
        "id": "349486678",
        "name": "Shipped",
        "position": 4,
        "complete": true,
        "color": "#ecdd8f"
      },
      {
        "id": "509459046",
        "name": "Done",
        "position": 4,
        "complete": true,
        "color": "#ecdd8f"
      },
      {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
    ],
    "workflow_kinds": [
      {
        "id": "1809278",
        "name": "Improvement"
      },
      {
        "id": "787053401",
        "name": "New"
      }
    ]
  }
}
```

**Request:**
```bash
curl -g "https://company.aha.io/api/v1/workflows/80245244" -X GET \
	-H "Authorization: Bearer 15b60d42d4bc417284a246ced6877b0bf13fb4aca415f7b55f7006bc3694a8ab" \
	-H "Content-Type: application/json" \
	-H "Accept: application/json"
```

**Response:**
```json
{
  "workflow": {
    "id": 80245244,
    "name": "Account product idea workflow",
    "statusable_type": "Idea",
    "transitions_only": false,
    "workflow_statuses": [
      {
        "id": "3259216",
        "name": "New",
        "position": 1,
        "complete": false,
        "color": "#dce7c6"
      },
      {
        "id": "349486678",
        "name": "Shipped",
        "position": 4,
        "complete": true,
        "color": "#ecdd8f"
      },
      {
        "id": "509459046",
        "name": "Done",
        "position": 4,
        "complete": true,
        "color": "#ecdd8f"
      },
      {
        "id": "1009437757",
        "name": "In progress",
        "position": 2,
        "complete": false,
        "color": "#ecdd8f"
      }
    ],
    "workflow_kinds": [
      {
        "id": "1809278",
        "name": "Improvement"
      },
      {
        "id": "787053401",
        "name": "New"
      }
    ]
  }
}
```

---
