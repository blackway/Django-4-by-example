# CLAUDE.md

이 파일은 이 저장소에서 작업할 때 Claude Code (claude.ai/code)에게 지침을 제공합니다.

## 프로젝트 개요

Sakila 샘플 데이터베이스(영화 대여 데이터베이스)를 사용하는 Django 4.1 프로젝트입니다. Sakila 디렉토리는 더 큰 "Django 4 by Example" 서적 저장소의 일부이지만, 레거시 데이터베이스를 다루는 독립적인 Django 프로젝트로 작동합니다.

**주요 컨텍스트:**
- 프로젝트는 Sakila 스키마가 포함된 기존 SQLite 데이터베이스(`sakila/sakila.db`)를 사용합니다
- Sakila 데이터베이스에는 배우, 영화, 고객, 대여, 결제, 재고 등의 테이블이 포함되어 있습니다
- 학습/연습용 프로젝트이며, 프로덕션 코드가 아닙니다
- 모델은 `inspectdb`를 사용하여 기존 데이터베이스에서 생성해야 합니다

## 프로젝트 구조

```
Sakila/
├── requirements.txt          # Python 의존성
├── .venv/                   # 가상 환경
└── sakila/                  # Django 프로젝트 루트
    ├── manage.py           # Django 관리 스크립트
    ├── sakila.db           # 기존 Sakila SQLite 데이터베이스
    └── sakila/             # Django 프로젝트 패키지
        ├── settings.py     # Django 설정
        ├── urls.py         # URL 구성
        ├── wsgi.py         # WSGI 애플리케이션
        └── asgi.py         # ASGI 애플리케이션
```

## 주요 명령어

### 환경 설정
```bash
# 가상 환경 활성화
source .venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### Django 관리

```bash
# 개발 서버 실행 (Sakila 디렉토리에서)
python sakila/manage.py runserver

# 기존 데이터베이스에서 모델 생성
python sakila/manage.py inspectdb > sakila/models.py

# 특정 테이블에 대한 모델 생성
python sakila/manage.py inspectdb actor film customer > sakila/app/models.py

# 마이그레이션 실행
python sakila/manage.py migrate

# 슈퍼유저 생성
python sakila/manage.py createsuperuser

# Django 셸 열기
python sakila/manage.py shell

# 데이터베이스 셸 열기
python sakila/manage.py dbshell

# 테스트 실행
python sakila/manage.py test

# 특정 테스트 실행
python sakila/manage.py test appname.tests.TestClassName.test_method_name
```

### 데이터베이스 탐색

```bash
# sakila.db의 모든 테이블 나열
sqlite3 sakila/sakila.db ".tables"

# 테이블 스키마 검사
sqlite3 sakila/sakila.db ".schema actor"

# 데이터베이스 쿼리
sqlite3 sakila/sakila.db "SELECT * FROM actor LIMIT 10;"
```

## 데이터베이스 스키마 (Sakila)

sakila.db에는 다음과 같은 주요 테이블이 포함되어 있습니다:
- **actor**: 영화 배우
- **film**: 영화 카탈로그
- **film_actor**: 영화와 배우 간의 다대다 관계
- **category**: 영화 카테고리
- **film_category**: 영화와 카테고리 간의 다대다 관계
- **customer**: 대여 고객
- **rental**: 대여 거래
- **payment**: 결제 기록
- **inventory**: 영화 재고
- **staff**: 매장 직원
- **store**: 매장 위치
- **address, city, country**: 지리적 데이터
- **language**: 영화 언어

뷰는 다음을 포함합니다: `film_list`, `customer_list`, `staff_list`, `sales_by_film_category`, `sales_by_store`

## 레거시 데이터베이스 작업

기존 Sakila 데이터베이스에서 Django 모델을 생성할 때:

1. `inspectdb`를 사용하여 초기 모델 생성
2. 모델에는 기본적으로 `managed = False`가 포함됩니다 (데이터베이스 구조가 Django 외부에서 관리됨)
3. 모든 ForeignKey 및 OneToOneField 관계에 `on_delete` 동작 추가
4. 각 모델에 `primary_key=True`인 필드 하나 설정
5. 데이터베이스는 언더스코어 명명법(예: `film_id`)을 사용하는 반면, Django는 camelCase 모델명을 선호합니다

## Django 설정

- **Database**: `sakila/sakila.db`의 SQLite (레거시 데이터베이스, `db.sqlite3`가 아님)
- **Django Version**: 4.1.x
- **Python Version**: 3.10+ 필수
- **DEBUG**: 현재 활성화됨 (개발 모드)
- **Installed Apps**: 현재 기본 Django 앱만 구성되어 있음

## 개발 참고사항

- `manage.py` 스크립트는 루트 디렉토리가 아닌 `sakila/manage.py`에 위치합니다
- 명령어는 `Sakila` 디렉토리(이 서브 프로젝트의 저장소 루트)에서 실행해야 합니다
- 데이터베이스 파일 `sakila.db`는 미리 채워져 있으며 삭제하면 안 됩니다
- `db.sqlite3` 파일은 Django 마이그레이션으로 생성되지만 프로젝트는 설정에 따라 `sakila.db`를 사용합니다
