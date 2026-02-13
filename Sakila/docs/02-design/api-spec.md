# API Specification - Sakila Web Interface

**Date**: 2026-02-13
**Phase**: Phase 4 - API Design/Implementation
**Level**: Dynamic (Fullstack Web Application)

## Overview

Sakila 영화 대여 시스템을 위한 REST API 명세서입니다. Django REST Framework를 사용하여 구현됩니다.

## Base URL

```
http://localhost:8000/
```

## Authentication

현재 버전에서는 인증이 필요하지 않는 읽기 전용 API를 제공합니다.

## Common Response Format

### Success Response
```json
{
    "count": 1000,
    "next": "http://localhost:8000/api/films/?page=2",
    "previous": null,
    "results": [...]
}
```

### Error Response
```json
{
    "detail": "Not found."
}
```

## API Endpoints

### 1. Films API

#### List Films
```
GET /api/films/
```

**Query Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| page | integer | Page number | `?page=2` |
| rating | string | Filter by rating | `?rating=PG-13` |
| release_year | integer | Filter by year | `?release_year=2006` |
| language | integer | Filter by language ID | `?language=1` |
| search | string | Search in title/description | `?search=dinosaur` |
| ordering | string | Sort results | `?ordering=-release_year` |

**Response (List):**
```json
{
    "count": 1000,
    "next": "http://localhost:8000/api/films/?page=2",
    "previous": null,
    "results": [
        {
            "film_id": 1,
            "title": "Academy Dinosaur",
            "description": "A Epic Drama of a Feminist...",
            "release_year": 2006,
            "language_name": "English",
            "rental_duration": 6,
            "rental_rate": "0.99",
            "length": 86,
            "rating": "PG",
            "categories": ["Documentary"],
            "actor_count": 3
        }
    ]
}
```

#### Retrieve Film
```
GET /api/films/{id}/
```

**Response (Detail):**
```json
{
    "film_id": 1,
    "title": "Academy Dinosaur",
    "description": "A Epic Drama of a Feminist...",
    "release_year": 2006,
    "language": {
        "language_id": 1,
        "name": "English"
    },
    "language_name": "English",
    "original_language_name": null,
    "rental_duration": 6,
    "rental_rate": "0.99",
    "length": 86,
    "replacement_cost": "20.99",
    "rating": "PG",
    "special_features": "Trailers,Commentaries",
    "categories": [1],
    "category_names": ["Documentary"],
    "actors": [
        {
            "actor_id": 1,
            "first_name": "PENELOPE",
            "last_name": "GUINESS",
            "full_name": "PENELOPE GUINESS"
        }
    ],
    "last_update": "2006-02-15T05:03:42Z"
}
```

#### Film Actions

**Get Film Actors:**
```
GET /api/films/{id}/actors/
```

**Get Film Categories:**
```
GET /api/films/{id}/categories/
```

---

### 2. Actors API

#### List Actors
```
GET /api/actors/
```

**Query Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| page | integer | Page number | `?page=2` |
| search | string | Search by name | `?search=penelope` |
| ordering | string | Sort results | `?ordering=last_name` |

**Response:**
```json
{
    "count": 200,
    "results": [
        {
            "actor_id": 1,
            "first_name": "PENELOPE",
            "last_name": "GUINESS",
            "full_name": "PENELOPE GUINESS",
            "film_count": 19,
            "last_update": "2006-02-15T04:34:33Z"
        }
    ]
}
```

#### Retrieve Actor
```
GET /api/actors/{id}/
```

#### Get Actor Films
```
GET /api/actors/{id}/films/
```

---

### 3. Categories API

#### List Categories
```
GET /api/categories/
```

**Response:**
```json
{
    "count": 16,
    "results": [
        {
            "category_id": 1,
            "name": "Action",
            "last_update": "2006-02-15T04:46:27Z"
        }
    ]
}
```

#### Retrieve Category
```
GET /api/categories/{id}/
```

#### Get Category Films
```
GET /api/categories/{id}/films/
```

---

### 4. Customers API

#### List Customers
```
GET /api/customers/
```

**Query Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| page | integer | Page number | `?page=2` |
| active | boolean | Filter by active status | `?active=true` |
| store | integer | Filter by store ID | `?store=1` |
| search | string | Search by name/email | `?search=mary` |
| ordering | string | Sort results | `?ordering=last_name` |

**Response:**
```json
{
    "count": 599,
    "results": [
        {
            "customer_id": 1,
            "store_id": 1,
            "first_name": "MARY",
            "last_name": "SMITH",
            "full_name": "MARY SMITH",
            "email": "mary.smith@sakilacustomer.org",
            "address": {
                "address_id": 5,
                "address": "1913 Hanoi Way",
                "district": "Nagasaki",
                "city_name": "Sasebo",
                "country_name": "Japan",
                "postal_code": "14103",
                "phone": "28303384290"
            },
            "active": true,
            "create_date": "2006-02-14T22:04:36Z",
            "rental_count": 32,
            "payment_count": 32,
            "last_update": "2006-02-15T04:57:20Z"
        }
    ]
}
```

#### Retrieve Customer
```
GET /api/customers/{id}/
```

#### Get Customer Rentals
```
GET /api/customers/{id}/rentals/
```

#### Get Customer Payments
```
GET /api/customers/{id}/payments/
```

---

### 5. Stores API

#### List Stores
```
GET /api/stores/
```

**Response:**
```json
{
    "count": 2,
    "results": [
        {
            "store_id": 1,
            "manager_name": "Mike Hillyer",
            "address": {
                "address_id": 1,
                "address": "47 MySakila Drive",
                "district": "Alberta",
                "city_name": "Lethbridge",
                "country_name": "Canada",
                "postal_code": "T1H 1H6",
                "phone": "14033335588"
            },
            "last_update": "2006-02-15T04:57:16Z"
        }
    ]
}
```

#### Retrieve Store
```
GET /api/stores/{id}/
```

#### Get Store Staff
```
GET /api/stores/{id}/staff/
```

#### Get Store Inventory
```
GET /api/stores/{id}/inventory/
```

---

## Pagination

All list endpoints support pagination with `PageNumberPagination`.

**Query Parameters:**
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 20, max: 100)

**Example:**
```
GET /api/films/?page=2&page_size=50
```

## Filtering

### Filter Backends

1. **DjangoFilterBackend**: Exact match filtering
2. **SearchFilter**: Full-text search
3. **OrderingFilter**: Result sorting

### Ordering

**Ascending:**
```
?ordering=title
?ordering=release_year
```

**Descending:**
```
?ordering=-title
?ordering=-release_year
```

**Multiple:**
```
?ordering=-release_year,title
```

## Error Codes

| Status Code | Description |
|------------|-------------|
| 200 | Success |
| 404 | Not Found |
| 400 | Bad Request |
| 500 | Server Error |

## Rate Limiting

현재 버전에서는 Rate Limiting이 적용되지 않습니다.

## CORS

CORS가 다음 Origin에 대해 허용됩니다:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

## Usage Examples

### cURL

```bash
# Get all films
curl http://localhost:8000/api/films/

# Get film by ID
curl http://localhost:8000/api/films/1/

# Search films
curl http://localhost:8000/api/films/?search=dinosaur

# Filter by rating
curl http://localhost:8000/api/films/?rating=PG-13

# Sort by release year
curl http://localhost:8000/api/films/?ordering=-release_year
```

### JavaScript (Fetch)

```javascript
// Get films
const response = await fetch('http://localhost:8000/api/films/');
const data = await response.json();

console.log(data.results);

// Search films
const searchResponse = await fetch('http://localhost:8000/api/films/?search=dinosaur');
const searchData = await searchResponse.json();

console.log(searchData.results);
```

### Python (requests)

```python
import requests

# Get films
response = requests.get('http://localhost:8000/api/films/')
data = response.json()

print(data['results'])

# Search films
search_response = requests.get('http://localhost:8000/api/films/', params={'search': 'dinosaur'})
search_data = search_response.json()

print(search_data['results'])
```

---

**Next Step**: Phase 5 - 디자인 시스템 구축
