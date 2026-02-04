# Sakila Database Django Web Application

Sakila 영화 대여점 데이터베이스를 Django 웹 프레임워크로 관리하는 웹 애플리케이션입니다.

## 프로젝트 구조

```
Sakila/
├── sakila/                 # Django 프로젝트 디렉토리
│   ├── manage.py          # Django 관리 명령어 실행 파일
│   ├── sakila/            # 프로젝트 설정 디렉토리
│   │   ├── settings.py    # Django 설정 파일
│   │   ├── urls.py        # 메인 URL 설정
│   │   └── wsgi.py        # WSGI 설정
│   ├── sakila_app/        # Sakila 앱 디렉토리
│   │   ├── models.py      # 데이터베이스 모델
│   │   ├── views.py       # 뷰 함수
│   │   ├── urls.py        # 앱 URL 설정
│   │   ├── admin.py       # 관리자 페이지 설정
│   │   └── templates/     # HTML 템플릿
│   └── sakila.db          # SQLite 데이터베이스
└── .venv/                 # Python 가상환경
```

## 주요 기능

### 1. 관리자 페이지 (Django Admin)
- URL: http://127.0.0.1:8000/admin/
- 사용자명: `admin`
- 비밀번호: `admin`

모든 테이블을 Admin 페이지에서 조회, 등록, 수정, 삭제할 수 있습니다:
- Actors (배우)
- Films (영화)
- Customers (고객)
- Categories (카테고리)
- Languages (언어)
- Stores (매장)
- Staff (직원)
- Rentals (대여)
- Inventory (인벤토리)
- Payments (결제)
- Addresses (주소)
- Cities (도시)
- Countries (국가)

### 2. 웹 인터페이스
- URL: http://127.0.0.1:8000/
- 홈 페이지에서 모든 테이블에 대한 링크와 데이터 개수 확인
- 각 테이블별 목록 페이지 (페이지네이션 포함)
- 각 레코드별 상세 정보 페이지
- 관련 데이터 링크 (외래키 관계)

## 데이터베이스 테이블

### 핵심 테이블
- **Actor**: 배우 정보
- **Film**: 영화 정보 (제목, 설명, 개봉년도, 대여료, 등급 등)
- **Customer**: 고객 정보
- **Staff**: 직원 정보
- **Store**: 매장 정보

### 관계 테이블
- **FilmActor**: 영화-배우 관계
- **FilmCategory**: 영화-카테고리 관계
- **Rental**: 대여 기록
- **Payment**: 결제 기록
- **Inventory**: 영화 재고

### 참조 테이블
- **Language**: 언어
- **Category**: 영화 카테고리
- **Address**: 주소
- **City**: 도시
- **Country**: 국가

## 설치 및 실행

### 1. 가상환경 활성화
```bash
source .venv/bin/activate
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션
```bash
cd sakila
python manage.py migrate
```

### 4. 관리자 계정 생성 (이미 생성된 경우 생략)
```bash
python manage.py createsuperuser
```

### 5. 개발 서버 실행
```bash
python manage.py runserver
```

### 6. 브라우저에서 접속
- 메인 페이지: http://127.0.0.1:8000/
- 관리자 페이지: http://127.0.0.1:8000/admin/

## 모델 정보

모든 모델은 기존 `sakila.db` 데이터베이스의 테이블에서 `inspectdb` 명령어로 자동 생성되었으며, Django 표준에 맞게 수정되었습니다:

- `managed = False`: Django가 테이블을 생성/수정하지 않도록 설정
- ForeignKey 관계에 `on_delete=models.CASCADE` 추가
- 모든 CharField에 적절한 `max_length` 설정
- TextField를 DateTimeField로 변경
- 각 모델에 `__str__()` 메서드 추가

## URL 패턴

### 홈
- `/` - 홈 페이지

### 배우 (Actors)
- `/actors/` - 배우 목록
- `/actors/<id>/` - 배우 상세

### 영화 (Films)
- `/films/` - 영화 목록
- `/films/<id>/` - 영화 상세

### 고객 (Customers)
- `/customers/` - 고객 목록
- `/customers/<id>/` - 고객 상세

(기타 모든 테이블도 동일한 패턴)

## 기술 스택

- **Backend**: Django 4.1.13
- **Database**: SQLite3 (sakila.db)
- **Frontend**: Django Templates + CSS
- **Python**: 3.12.11

## 주의사항

- 모든 모델은 `managed = False`로 설정되어 있어 Django migrations로 테이블 구조를 변경할 수 없습니다.
- 기존 데이터베이스의 구조를 변경하려면 SQLite를 직접 사용해야 합니다.

## 개발자

이 프로젝트는 Sakila Sample Database를 기반으로 Django 웹 애플리케이션으로 구현되었습니다.
