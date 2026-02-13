# Schema Definition - Sakila Web Interface

**Date**: 2026-02-13
**Phase**: Phase 1 - Schema/Terminology Definition
**Level**: Dynamic (Fullstack Web Application)

## Overview

Sakila 영화 대여 데이터베이스를 위한 웹 인터페이스의 데이터 스키마 정의 문서입니다.

## Core Entities (핵심 엔티티)

### 1. Film (영화)
| Field | Type | Description |
|-------|------|-------------|
| film_id | Integer (PK) | 영화 고유 ID |
| title | String(255) | 영화 제목 |
| description | Text | 영화 설명 |
| release_year | String(4) | 개봉 연도 |
| language | ForeignKey(Language) | 더빙 언어 |
| original_language | ForeignKey(Language) | 원본 언어 (선택) |
| rental_duration | SmallInt | 대여 기간 (일) |
| rental_rate | Decimal(4,2) | 대여 요금 |
| length | SmallInt | 상영 시간 (분) |
| replacement_cost | Decimal(5,2) | 분실 시 보상비 |
| rating | String(10) | 등급 (G, PG, PG-13, R, NC-17) |
| special_features | String(100) | 특수 기능 (Trailers, Commentaries, Deleted Scenes, Behind the Scenes) |
| last_update | DateTime | 마지막 업데이트 |

### 2. Actor (배우)
| Field | Type | Description |
|-------|------|-------------|
| actor_id | Integer (PK) | 배우 고유 ID |
| first_name | String(45) | 이름 |
| last_name | String(45) | 성 |
| last_update | DateTime | 마지막 업데이트 |

**Relation**: M:N with Film through FilmActor

### 3. Category (카테고리)
| Field | Type | Description |
|-------|------|-------------|
| category_id | Integer (PK) | 카테고리 고유 ID |
| name | String(25) | 카테고리명 |
| last_update | DateTime | 마지막 업데이트 |

**Relation**: M:N with Film through FilmCategory

### 4. Customer (고객)
| Field | Type | Description |
|-------|------|-------------|
| customer_id | Integer (PK) | 고객 고유 ID |
| store | ForeignKey(Store) | 소속 매장 |
| first_name | String(45) | 이름 |
| last_name | String(45) | 성 |
| email | String(50) | 이메일 |
| address | ForeignKey(Address) | 주소 |
| active | String(1) | 활성 상태 (Y/N) |
| create_date | DateTime | 가입일 |
| last_update | DateTime | 마지막 업데이트 |

### 5. Rental (대여)
| Field | Type | Description |
|-------|------|-------------|
| rental_id | Integer (PK) | 대여 고유 ID |
| rental_date | DateTime | 대여일 |
| inventory | ForeignKey(Inventory) | 재고 항목 |
| customer | ForeignKey(Customer) | 고객 |
| return_date | DateTime | 반납일 (nullable) |
| staff | ForeignKey(Staff) | 담당 직원 |
| last_update | DateTime | 마지막 업데이트 |

### 6. Payment (결제)
| Field | Type | Description |
|-------|------|-------------|
| payment_id | Integer (PK) | 결제 고유 ID |
| customer | ForeignKey(Customer) | 고객 |
| staff | ForeignKey(Staff) | 직원 |
| rental | ForeignKey(Rental) | 대여 건 (nullable) |
| amount | Decimal(5,2) | 결제 금액 |
| payment_date | DateTime | 결제일 |
| last_update | DateTime | 마지막 업데이트 |

## Supporting Entities (지원 엔티티)

### 7. Inventory (재고)
- **Fields**: inventory_id, film (FK), store (FK), last_update
- **Purpose**: 특정 매장의 영화 재고 관리

### 8. Store (매장)
- **Fields**: store_id, manager_staff (FK), address (FK), last_update
- **Purpose**: 대여점 매장 정보

### 9. Staff (직원)
- **Fields**: staff_id, first_name, last_name, address (FK), picture, email, store (FK), active, username, password, last_update
- **Purpose**: 매장 직원 정보

### 10. Address (주소)
- **Fields**: address_id, address, address2, district, city (FK), postal_code, phone, last_update
- **Purpose**: 주소 정보

### 11. City (도시)
- **Fields**: city_id, city, country (FK), last_update
- **Purpose**: 도시 정보

### 12. Country (국가)
- **Fields**: country_id, country, last_update
- **Purpose**: 국가 정보

### 13. Language (언어)
- **Fields**: language_id, name, last_update
- **Purpose**: 영화 더빙 언어 정보

## Relationships (관계)

### Many-to-Many Relationships
1. **Film ↔ Actor**: `film_actor` (중간 테이블)
2. **Film ↔ Category**: `film_category` (중간 테이블)

### One-to-Many Relationships
- **Store → Inventory**: 한 매장은 여러 재고 항목을 보유
- **Store → Staff**: 한 매장은 여러 직원을 고용
- **Film → Inventory**: 한 영화는 여러 재고 항목을 가질 수 있음
- **Customer → Rental**: 한 고객은 여러 대여 기록을 가짐
- **Customer → Payment**: 한 고객은 여러 결제 기록을 가짐
- **Rental → Payment**: 한 대여는 하나의 결제를 가짐 (1:1)
- **City → Address**: 한 도시는 여러 주소를 가짐
- **Country → City**: 한 국가는 여러 도시를 가짐
- **Language → Film**: 한 언어는 여러 영화를 가짐

## Database Views (데이터베이스 뷰)

### 1. film_list
- 영화 카탈로그 정보 (카테고리, 배우, 재고 포함)

### 2. customer_list
- 고객 상세 정보 (주소, 매장 포함)

### 3. staff_list
- 직원 상세 정보 (주소, 매장 포함)

### 4. sales_by_film_category
- 카테고리별 판매 통계

### 5. sales_by_store
- 매장별 판매 통계

## Web Interface Scope (웹 인터페이스 범위)

### Primary Features (주요 기능)
1. **영화 카탈로그 뷰어**: 모든 영화 검색 및 상세 정보 조회
2. **배우 프로필**: 배우별 출연 영화 목록
3. **카테고리 브라우징**: 카테고리별 영화 분류
4. **고객 관리**: 고객 정보 및 대여 기록 조회
5. **대여 현황**: 현재 대여 중인 영화 목록
6. **매장 통계**: 매장별 판매/대여 통계

### Secondary Features (차선 기능)
1. 결제 내역 조회
2. 재고 관리
3. 직원 정보 관리

## Managed vs Unmanaged

모든 모델은 `managed = False`로 설정되어 있음:
- 데이터베이스 스키마는 Django 외부에서 관리됨
- Django는 마이그레이션을 생성하지 않음
- 기존 Sakila 데이터베이스를 읽기 전용으로 활용

## Schema Diagram (ERD)

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Actor     │────────>│ Film_Actor  │<────────│    Film     │
└─────────────┘         └─────────────┘         └─────────────┘
                                                         │
                                                         │
                                                         ▼
                                                  ┌─────────────┐
                                                  │  Inventory  │
                                                  └─────────────┘
                                                         │
                                                         ▼
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  Customer   │────────>│   Rental    │────────>│   Payment   │
└─────────────┘         └─────────────┘         └─────────────┘

┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  Category   │────────>│Film_Category│<────────│    Film     │
└─────────────┘         └─────────────┘         └─────────────┘
```

---

**Next Step**: [terminology.md](terminology.md) - 도메인 용어 정의
