# Coding Convention - Sakila Web Interface

**Date**: 2026-02-13
**Phase**: Phase 2 - Coding Convention
**Level**: Dynamic (Fullstack Web Application)

## Overview

Django 프로젝트를 위한 코드 작성 규칙과 컨벤션을 정의합니다.

## Python/Django Standards (Python/Django 표준)

### Style Guide (스타일 가이드)
- **Python**: PEP 8 준수
- **Django**: Django Coding Style 준수
- **Line Length**: 최대 88자 (Black formatter 기준)
- **Indentation**: 4 spaces (탭 사용 금지)
- **Encoding**: UTF-8

### Import Order (임포트 순서)

```python
# 1. Standard library imports
import os
from datetime import datetime

# 2. Third-party imports
from django.db import models
from django.shortcuts import render, redirect
from rest_framework import viewsets

# 3. Local imports
from .models import Film, Actor
from .serializers import FilmSerializer
```

## Naming Conventions (명명 규칙)

### Variables (변수)
- **Convention**: `snake_case`
- **Descriptive**: 의미 있는 이름 사용

```python
# Good
customer_name = "John Doe"
total_payment = 99.99
active_rentals = []

# Bad
cn = "John Doe"
tp = 99.99
ar = []
```

### Functions (함수)
- **Convention**: `snake_case`
- **Verb-based**: 동사로 시작

```python
# Good
def get_customer_rentals(customer_id):
    pass

def calculate_total_payment(payments):
    pass

# Bad
def CustomerRentals(customer_id):
    pass

def calc(payments):
    pass
```

### Classes (클래스)
- **Convention**: `PascalCase`
- **Singular**: 단수형 사용

```python
# Good
class FilmViewSet(viewsets.ModelViewSet):
    pass

class CustomerDetail(View):
    pass

# Bad
class filmViewSet:
    pass

class CustomerDetails:
    pass
```

### Constants (상수)
- **Convention**: `UPPER_SNAKE_CASE`
- **Module-level**: 모듈 최상단에 정의

```python
# Good
DEFAULT_RENTAL_DURATION = 3
MAX_RENTAL_ITEMS = 10
PAGINATION_PAGE_SIZE = 20

# Bad
default_rental_duration = 3
MAX_RENTALITEMS = 10
```

## Django-Specific Conventions (Django 특화 컨벤션)

### Models (모델)

#### Model Class (모델 클래스)
```python
from django.db import models


class Film(models.Model):
    """영화 모델

    Sakila 데이터베이스의 film 테이블을 나타냅니다.
    """

    # Fields
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.title

    @property
    def full_info(self):
        """영화의 전체 정보를 반환합니다."""
        return f"{self.title} ({self.release_year})"
```

#### Foreign Keys (외래키)
```python
# Related name 설정
class Rental(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='rentals'  # 복수형 사용
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='rentals'
    )
```

### Views (뷰)

#### Function-Based Views (FBV)
```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Film


def film_list(request: HttpRequest) -> HttpResponse:
    """영화 목록을 렌더링합니다."""
    films = Film.objects.all().select_related('language')
    context = {
        'films': films,
        'title': 'Film Catalog'
    }
    return render(request, 'sakila_app/film_list.html', context)


def film_detail(request: HttpRequest, film_id: int) -> HttpResponse:
    """영화 상세 정보를 렌더링합니다."""
    film = get_object_or_404(Film, pk=film_id)
    context = {
        'film': film,
        'title': film.title
    }
    return render(request, 'sakila_app/film_detail.html', context)
```

#### Class-Based Views (CBV)
```python
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film


class FilmListView(ListView):
    """영화 목록 뷰"""

    model = Film
    template_name = 'sakila_app/film_list.html'
    context_object_name = 'films'
    paginate_by = 20
    ordering = ['title']


class FilmDetailView(DetailView):
    """영화 상세 뷰"""

    model = Film
    template_name = 'sakila_app/film_detail.html'
    context_object_name = 'film'
    slug_field = 'film_id'
    slug_url_kwarg = 'film_id'


class FilmCreateView(CreateView):
    """영화 생성 뷰"""

    model = Film
    template_name = 'sakila_app/film_form.html'
    fields = ['title', 'description', 'release_year', 'language']
    success_url = reverse_lazy('sakila_app:film-list')
```

### URLs (URL 패턴)

```python
# sakila_app/urls.py
from django.urls import path
from . import views

app_name = 'sakila_app'

urlpatterns = [
    # List views
    path('films/', views.film_list, name='film-list'),
    path('actors/', views.actor_list, name='actor-list'),
    path('categories/', views.category_list, name='category-list'),

    # Detail views
    path('films/<int:film_id>/', views.film_detail, name='film-detail'),
    path('actors/<int:actor_id>/', views.actor_detail, name='actor-detail'),
]
```

### Templates (템플릿)

#### Directory Structure (디렉토리 구조)
```
sakila_app/
└── templates/
    └── sakila_app/
        ├── base.html           # 기본 템플릿
        ├── film_list.html      # 영화 목록
        ├── film_detail.html    # 영화 상세
        ├── actor_list.html     # 배우 목록
        └── partials/           # 부분 템플릿
            ├── navbar.html
            └── pagination.html
```

#### Template Conventions (템플릿 컨벤션)
```html
{% extends "sakila_app/base.html" %}

{% block title %}{{ film.title }} - Sakila{% endblock %}

{% block content %}
<div class="film-detail">
  <h1>{{ film.title }}</h1>
  <p>{{ film.description }}</p>

  <dl>
    <dt>Release Year</dt>
    <dd>{{ film.release_year }}</dd>

    <dt>Rating</dt>
    <dd>{{ film.rating }}</dd>

    <dt>Rental Rate</dt>
    <dd>${{ film.rental_rate }}</dd>
  </dl>

  <h2>Cast</h2>
  <ul>
    {% for actor in film.actors.all %}
      <li>{{ actor.first_name }} {{ actor.last_name }}</li>
    {% empty %}
      <li>No cast information available.</li>
    {% endfor %}
  </ul>
</div>
{% endblock %}
```

### Forms (폼)

```python
from django import forms
from .models import Film


class FilmSearchForm(forms.Form):
    """영화 검색 폼"""

    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search films...'
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories"
    )

    rating = forms.ChoiceField(
        choices=[('', 'All Ratings')] + Film.RATING_CHOICES,
        required=False
    )
```

### Serializers (Django REST Framework)

```python
from rest_framework import serializers
from .models import Film, Actor


class FilmSerializer(serializers.ModelSerializer):
    """영화 시리얼라이저"""

    categories = serializers.SerializerMethodField()
    actors = ActorSerializer(many=True, read_only=True)
    language_name = serializers.CharField(source='language.name', read_only=True)

    class Meta:
        model = Film
        fields = [
            'film_id', 'title', 'description', 'release_year',
            'language', 'language_name', 'categories', 'actors',
            'rental_duration', 'rental_rate', 'length',
            'replacement_cost', 'rating'
        ]

    def get_categories(self, obj):
        """영화의 카테고리 목록을 반환합니다."""
        return [cat.name for cat in obj.categories.all()]
```

## Project Structure (프로젝트 구조)

```
sakila/
├── manage.py
├── sakila/                  # 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── sakila_app/              # 애플리케이션
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── serializers.py
    ├── admin.py
    ├── apps.py
    ├── tests.py
    ├── templates/
    │   └── sakila_app/
    │       ├── base.html
    │       ├── film_list.html
    │       └── film_detail.html
    └── static/
        └── sakila_app/
            ├── css/
            │   └── main.css
            └── js/
                └── main.js
```

## Database Query Conventions (데이터베이스 쿼리 컨벤션)

### Query Optimization (쿼리 최적화)

```python
# Bad (N+1 query problem)
films = Film.objects.all()
for film in films:
    print(film.language.name)  # 각 영화마다 별도 쿼리 실행

# Good (select_related)
films = Film.objects.all().select_related('language')
for film in films:
    print(film.language.name)  # JOIN으로 한 번에 조회

# Good (prefetch_related for Many-to-Many)
films = Film.objects.all().prefetch_related('actors', 'categories')
for film in films:
    for actor in film.actors.all():
        print(actor.name)
```

### Query Naming (쿼리 네이밍)
```python
# Repository pattern 같은 경우
def get_active_rentals():
    """활성 대여 목록을 반환합니다."""
    return Rental.objects.filter(return_date__isnull=True)

def get_customer_payment_history(customer_id, limit=10):
    """고객의 결제 내역을 반환합니다."""
    return Payment.objects.filter(
        customer_id=customer_id
    ).order_by('-payment_date')[:limit]
```

## Error Handling (에러 처리)

```python
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.exceptions import NotFound


# View에서의 에러 처리
def film_detail(request, film_id):
    try:
        film = Film.objects.get(pk=film_id)
    except Film.DoesNotExist:
        raise Http404("Film does not exist")

    # 또는 get_object_or_404 사용
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'film_detail.html', {'film': film})


# API에서의 에러 처리
class FilmViewSet(viewsets.ModelViewSet):
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound("Film not found")
```

## Documentation (문서화)

### Docstring Format (독스트링 형식)
```python
def calculate_late_fees(rental, daily_rate=0.99):
    """연체 수수료를 계산합니다.

    Args:
        rental (Rental): 대여 객체
        daily_rate (float): 일일 연체 요금. 기본값은 0.99.

    Returns:
        float: 연체 수수료 총액

    Example:
        >>> rental = Rental.objects.get(pk=1)
        >>> calculate_late_fees(rental)
        5.94
    """
    if not rental.return_date:
        return 0

    overdue_days = (rental.return_date - rental.rental.due_date).days
    return max(0, overdue_days * daily_rate)
```

## Testing (테스트)

```python
from django.test import TestCase, Client
from django.urls import reverse
from .models import Film


class FilmViewTests(TestCase):
    """영화 뷰 테스트"""

    def setUp(self):
        """테스트 데이터를 설정합니다."""
        self.client = Client()
        self.film = Film.objects.create(title="Test Film")

    def test_film_list_view(self):
        """영화 목록 뷰를 테스트합니다."""
        url = reverse('sakila_app:film-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Film")

    def test_film_detail_view(self):
        """영화 상세 뷰를 테스트합니다."""
        url = reverse('sakila_app:film-detail', args=[self.film.film_id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Film")
```

## Logging (로깅)

```python
import logging

logger = logging.getLogger(__name__)


def process_payment(rental_id, amount):
    """결제를 처리합니다."""
    try:
        rental = Rental.objects.get(pk=rental_id)
        # 결제 처리 로직
        logger.info(f"Payment processed: ${amount} for rental {rental_id}")
    except Rental.DoesNotExist:
        logger.error(f"Rental not found: {rental_id}")
        raise
```

## Comments (주석)

```python
# Good: 설명이 필요한 복잡한 로직에만 주석 사용
# 대여 기간이 3일이므로, 반납 예정일은 대여일 + 3일입니다.
due_date = rental.rental_date + timedelta(days=rental.film.rental_duration)

# Bad: 자명한 코드에 주석 금지
# 고객 이름 변수 설정
customer_name = customer.first_name  # 불필요한 주석
```

---

**Next Step**: Phase 3 - 목업 개발
