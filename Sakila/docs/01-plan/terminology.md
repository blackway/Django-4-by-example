# Terminology Definition - Sakila Web Interface

**Date**: 2026-02-13
**Phase**: Phase 1 - Schema/Terminology Definition
**Level**: Dynamic (Fullstack Web Application)

## Overview

Sakila 영화 대여 시스템의 도메인 용어와 데이터 구조 표현법을 정의하는 문서입니다.

## Domain Terms (도메인 용어)

### Core Business Terms (핵심 비즈니스 용어)

| 용어 (영어) | 용어 (한국어) | 정의 |
|-----------|-------------|-----|
| **Film** | 영화 | 대여 가능한 영화 컨텐츠. 제목, 설명, 등급, 대여 요금 등의 정보를 포함 |
| **Actor** | 배우 | 영화에 출연하는 배우. 이름 정보 포함 |
| **Category** | 카테고리 | 영화 장르 분류 (Action, Comedy, Drama 등) |
| **Customer** | 고객 | 영화를 대여하는 사람. 이름, 이메일, 주소 정보 포함 |
| **Rental** | 대여 | 고객이 영화를 빌리는 거래. 대여일, 반납일 포함 |
| **Payment** | 결제 | 대여에 대한 지불. 금액, 결제일 포함 |
| **Inventory** | 재고 | 매장이 보유한 특정 영화의 복제본 |
| **Store** | 매장 | 영화 대여점. 재고와 직원을 보유 |
| **Staff** | 직원 | 매장에서 근무하며 대여/결제를 처리하는 사람 |
| **Address** | 주소 | 고객, 직원, 매장의 지리적 위치 정보 |

### Film Attributes (영화 속성)

| 용어 | 정의 |
|-----|-----|
| **Title** | 영화 제목 |
| **Description** | 영화 줄거리 설명 |
| **Release Year** | 개봉 연도 |
| **Language** | 더빙 언어 (영어, 일본어, 이탈리아어 등) |
| **Original Language** | 원본 언어 (선택 사항) |
| **Rental Duration** | 대여 가능 기간 (일 단위, 기본 3일) |
| **Rental Rate** | 대여 요금 (기본 $4.99) |
| **Length** | 상영 시간 (분 단위) |
| **Replacement Cost** | 분실 시 보상 비용 (기본 $19.99) |
| **Rating** | 영화 등급 (G, PG, PG-13, R, NC-17) |
| **Special Features** | 특수 기능 (예고편, Commentary, 삭제된 장면 등) |

### Rental Attributes (대여 속성)

| 용어 | 정의 |
|-----|-----|
| **Rental Date** | 대여 시작일 |
| **Return Date** | 반납일 (null일 경우 대여 중) |
| **Overdue** | 연체 (반납일이 지난 상태) |
| **Active Rental** | 대여 중인 항목 (return_date가 null) |

### Customer Attributes (고객 속성)

| 용어 | 정의 |
|-----|-----|
| **Active** | 활성 상태 (Y: 활성, N: 비활성) |
| **Create Date** | 고객 등록일 |
| **Email** | 이메일 주소 |

### Location Hierarchy (위치 계층 구조)

```
Country (국가)
  └─> City (도시)
       └─> Address (주소)
```

| 레벨 | 용어 | 설명 |
|-----|-----|-----|
| 1 | Country | 국가 (예: United States, Japan) |
| 2 | City | 도시 (예: Seattle, Tokyo) |
| 3 | Address | 상세 주소 (거리명, 우편번호, 전화번호) |

## Data Representation Conventions (데이터 표현 규약)

### Naming Conventions (명명 규칙)

#### Database (데이터베이스)
- **테이블명**: 소문자, 언더스코어 구분 (예: `film_actor`, `customer_list`)
- **컬럼명**: 소문자, 언더스코어 구분 (예: `first_name`, `rental_date`)

#### Django Models (Django 모델)
- **모델 클래스명**: PascalCase, 단수형 (예: `Film`, `FilmActor`, `Customer`)
- **필드명**: snake_case (예: `first_name`, `rental_rate`)

#### API/JSON (API/JSON)
- **Key**: camelCase 또는 snake_case (프론트엔드 컨벤션에 따름)
- **예시**: `{"filmId": 1, "title": "Academy Dinosaur"}`

### Date/Time Formats (날짜/시간 형식)

| 형식 | 예시 | 설명 |
|-----|-----|-----|
| **Database** | 2026-02-13 14:30:00 | DATETIME 포맷 |
| **API ISO 8601** | 2026-02-13T14:30:00Z | ISO 8601 표준 |
| **Display (KO)** | 2026년 2월 13일 | 사용자 표시용 |
| **Display (EN)** | February 13, 2026 | 사용자 표시용 |

### Currency Format (통화 형식)

| 형식 | 예시 | 설명 |
|-----|-----|-----|
| **Database** | 4.99 | DECIMAL(5,2) |
| **API** | 4.99 또는 "$4.99" | JSON 숫자 또는 문자열 |
| **Display (KO)** | ₩5,900 | 원화 표시 (환율 적용) |
| **Display (EN)** | $4.99 | 달러 표시 |

### Rating Values (등급 값)

| 등급 | 설명 |
|-----|-----|
| **G** | General Audiences (전체 관람가) |
| **PG** | Parental Guidance (부모 지도) |
| **PG-13** | Parents Strongly Cautioned (13세 미만 부모 지도) |
| **R** | Restricted (17세 미만 보호자 동반) |
| **NC-17** | Adults Only (18세 이상) |

### Special Features Values (특수 기능 값)

| 값 | 설명 |
|-----|-----|
| **Trailers** | 예고편 포함 |
| **Commentaries** | 감독/출연진 코멘터리 포함 |
| **Deleted Scenes** | 삭제된 장면 포함 |
| **Behind the Scenes** | 메이킹 다큐멘터리 포함 |

*참고: 여러 값은 쉼표로 구분된 문자열로 저장*

### Active Status Values (활성 상태 값)

| 값 | 설명 |
|-----|-----|
| **Y** | 활성 (Active) |
| **N** | 비활성 (Inactive) |

## Query Terminology (쿼리 용어)

### Common Filters (일반 필터)

| 용어 | 설명 | 예시 |
|-----|-----|-----|
| **search** | 텍스트 검색 | `?query=dinosaur` |
| **category** | 카테고리 필터 | `?category=Action` |
| **rating** | 등급 필터 | `?rating=PG-13` |
| **actor** | 배우 필터 | `?actor_id=1` |
| **language** | 언어 필터 | `?language_id=1` |
| **page** | 페이지 번호 | `?page=1` |
| **limit** | 페이지 크기 | `?limit=20` |
| **sort_by** | 정렬 기준 | `?sort_by=title` |
| **order** | 정렬 순서 | `?order=asc` 또는 `desc` |

### API Response Structure (API 응답 구조)

```json
{
  "count": 1000,           // 전체 항목 수
  "next": "/api/films/?page=2",
  "previous": null,
  "results": [             // 데이터 목록
    {
      "film_id": 1,
      "title": "Academy Dinosaur",
      "description": "...",
      "release_year": "2006",
      "language": {
        "language_id": 1,
        "name": "English"
      },
      "categories": ["Action", "Comedy"],
      "actors": [
        {"actor_id": 1, "name": "PENELOPE GUINESS"}
      ],
      "rental_rate": 4.99,
      "rating": "PG"
    }
  ]
}
```

## User Roles (사용자 역할)

| 역할 | 권한 |
|-----|-----|
| **Guest** | 영화 목록 조회, 영화 상세 조회 (읽기 전용) |
| **Customer** | 내 대여 기록 조회, 내 결제 내역 조회 |
| **Staff** | 매장 재고 관리, 대여/반납 처리, 매장 통계 조회 |
| **Admin** | 전체 데이터 CRUD, 시스템 설정 관리 |

## UI Terminology (UI 용어)

### Navigation Items (네비게이션 항목)

| 영어 | 한국어 | 설명 |
|-----|--------|-----|
| **Home** | 홈 | 메인 페이지 |
| **Films** | 영화 | 영화 카탈로그 |
| **Actors** | 배우 | 배우 목록 |
| **Categories** | 카테고리 | 장르별 분류 |
| **Customers** | 고객 | 고객 관리 |
| **Rentals** | 대여 | 대여 현황 |
| **Stores** | 매장 | 매장 정보 |
| **Reports** | 리포트 | 통계 리포트 |

### Action Buttons (액션 버튼)

| 영어 | 한국어 | 설명 |
|-----|--------|-----|
| **View Details** | 상세 보기 | 상세 정보 조회 |
| **Edit** | 편집 | 데이터 수정 |
| **Delete** | 삭제 | 데이터 삭제 |
| **Search** | 검색 | 검색 실행 |
| **Filter** | 필터 | 필터 적용 |
| **Export** | 내보내기 | 데이터 내보내기 |

---

**Next Step**: Phase 2 - Coding Convention 정의
