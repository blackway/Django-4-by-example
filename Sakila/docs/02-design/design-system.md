# Design System - Sakila Web Interface

**Date**: 2026-02-13
**Phase**: Phase 5 - Design System
**Level**: Dynamic (Fullstack Web Application)

## Overview

Sakila 영화 대여 시스템을 위한 디자인 시스템 가이드입니다. Django 템플릿 시스템을 기반으로 일관된 UI를 제공합니다.

## Design Principles (디자인 원칙)

1. **일관성 (Consistency)**: 전체 애플리케이션에서 동일한 디자인 패턴 사용
2. **접근성 (Accessibility)**: WCAG 2.1 AA 준수
3. **응답성 (Responsiveness)**: 모바일, 태블릿, 데스크톱 지원
4. **사용성 (Usability)**: 직관적인 네비게이션과 명확한 피드백

## Color Palette (컬러 팔레트)

### Primary Colors (주요 색상)

| 색상 | Hex 코드 | 용도 | 설명 |
|------|---------|------|------|
| Primary Blue | `#2563eb` | 브랜딩, 링크, 주요 버튼 | 신뢰와 전문성 |
| Primary Hover | `#1d4ed8` | 호버 상태 | 어두운 파란색 |
| Secondary Gray | `#64748b` | 보조 텍스트, 아이콘 | 중립적인 느낌 |

### Semantic Colors (의미 색상)

| 색상 | Hex 코드 | 용도 | 설명 |
|------|---------|------|------|
| Success Green | `#10b981` | 성공, 활성 상태 | 긍정적인 결과 |
| Warning Orange | `#f59e0b` | 경고, 주의 | 주의가 필요함 |
| Danger Red | `#ef4444` | 오류, 삭제, 비활성 | 부정적인 결과 |

### Neutral Colors (중립 색상)

| 색상 | Hex 코드 | 용도 |
|------|---------|------|
| Background | `#f8fafc` | 페이지 배경 |
| Card Background | `#ffffff` | 카드, 모달 배경 |
| Text Primary | `#1e293b` | 주요 텍스트 |
| Text Secondary | `#64748b` | 보조 텍스트 |
| Border | `#e2e8f0` | 테두리 |

### Movie Rating Colors (영화 등급 색상)

| 등급 | 색상 | Hex 코드 |
|------|------|---------|
| G | 녹색 | `#10b981` |
| PG | 파란색 | `#3b82f6` |
| PG-13 | 주황색 | `#f59e0b` |
| R | 빨간색 | `#ef4444` |
| NC-17 | 보라색 | `#7c3aed` |

## Typography (타이포그래피)

### Font Families (폰트 패밀리)

```css
/* 기본 폰트 */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
             Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue',
             sans-serif;

/* 코드/모노스페이스 */
font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Mono',
             'Droid Sans Mono', 'Source Code Pro', monospace;
```

### Type Scale (타입 스케일)

| 스타일 | 폰트 크기 | 용도 | 예시 |
|--------|----------|------|------|
| H1 | 2.5rem (40px) | 페이지 제목 | 영화 목록 |
| H2 | 2rem (32px) | 섹션 제목 | 카테고리별 영화 |
| H3 | 1.5rem (24px) | 카드 제목 | 영화 제목 |
| H4 | 1.25rem (20px) | 소제목 | 배우 이름 |
| Body | 1rem (16px) | 본문 | 영화 설명 |
| Small | 0.875rem (14px) | 작은 텍스트 | 뱃지, 메타데이터 |
| XSmall | 0.75rem (12px) | 아주 작은 텍스트 | 뱃지 번호 |

### Font Weights (폰트 굵기)

| 굵기 | 값 | 용도 |
|------|-----|------|
| Regular | 400 | 본문 텍스트 |
| Medium | 500 | 강조, 버튼 |
| SemiBold | 600 | 소제목 |
| Bold | 700 | 제목 |

## Spacing (간격)

### Base Spacing Unit (기본 간격 단위)

```css
:root {
    --spacing-unit: 0.25rem;  /* 4px */
}
```

### Spacing Scale (간격 스케일)

| 토큰 | 값 | 설명 |
|------|-----|------|
| xs | `calc(var(--spacing-unit) * 1)` | 0.25rem (4px) |
| sm | `calc(var(--spacing-unit) * 2)` | 0.5rem (8px) |
| md | `calc(var(--spacing-unit) * 3)` | 0.75rem (12px) |
| lg | `calc(var(--spacing-unit) * 4)` | 1rem (16px) |
| xl | `calc(var(--spacing-unit) * 6)` | 1.5rem (24px) |
| 2xl | `calc(var(--spacing-unit) * 8)` | 2rem (32px) |
| 3xl | `calc(var(--spacing-unit) * 12)` | 3rem (48px) |

## Components (컴포넌트)

### Buttons (버튼)

#### Primary Button
```html
<a href="/films/1/" class="btn btn-primary">View Details</a>
```

#### Secondary Button
```html
<button class="btn btn-secondary">Back to List</button>
```

#### Outline Button
```html
<button class="btn btn-outline">Edit Film</button>
```

### Cards (카드)

#### Film Card (영화 카드)
```html
<div class="card film-card">
    <div class="card-poster">
        <img src="..." alt="Film Poster">
    </div>
    <div class="card-body">
        <h3 class="card-title">Film Title</h3>
        <div class="card-meta">
            <span class="badge badge-primary">PG-13</span>
            <span class="badge badge-secondary">2026</span>
        </div>
        <p class="card-text">Film description...</p>
        <div class="card-footer">
            <span class="text-primary font-bold">$4.99</span>
            <a href="/films/1/" class="btn btn-primary btn-sm">Details</a>
        </div>
    </div>
</div>
```

#### Stats Card (통계 카드)
```html
<div class="card stat-card">
    <div class="stat-icon">🎬</div>
    <div class="stat-info">
        <h4>Total Films</h4>
        <p class="stat-value">1,000</p>
    </div>
</div>
```

### Badges (뱃지)

```html
<span class="badge badge-primary">Action</span>
<span class="badge badge-warning">PG-13</span>
<span class="badge badge-success">Active</span>
<span class="badge badge-danger">Inactive</span>
```

### Forms (폼)

#### Input Field
```html
<div class="form-group">
    <label for="search">Search Films</label>
    <input type="text" id="search" name="search"
           class="form-control" placeholder="Enter title...">
</div>
```

#### Select Field
```html
<div class="form-group">
    <label for="category">Category</label>
    <select id="category" name="category" class="form-control">
        <option value="">All Categories</option>
        <option value="1">Action</option>
        <option value="2">Comedy</option>
    </select>
</div>
```

### Navigation (네비게이션)

#### Main Navbar
```html
<nav class="navbar">
    <div class="container">
        <div class="navbar-brand">
            <a href="/">Sakila</a>
        </div>
        <ul class="navbar-nav">
            <li><a href="/films/" class="active">Films</a></li>
            <li><a href="/actors/">Actors</a></li>
            <li><a href="/categories/">Categories</a></li>
        </ul>
    </div>
</nav>
```

### Pagination (페이지네이션)

```html
<div class="pagination">
    <a href="?page=1" class="pagination-link active">1</a>
    <a href="?page=2" class="pagination-link">2</a>
    <a href="?page=3" class="pagination-link">3</a>
    <span class="pagination-ellipsis">...</span>
    <a href="?page=50" class="pagination-link">50</a>
    <a href="?page=2" class="pagination-next">Next</a>
</div>
```

### Tables (테이블)

```html
<table class="table">
    <thead>
        <tr>
            <th>Title</th>
            <th>Release Year</th>
            <th>Rating</th>
            <th>Rental Rate</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Academy Dinosaur</td>
            <td>2006</td>
            <td><span class="badge badge-warning">PG</span></td>
            <td>$0.99</td>
            <td>
                <a href="/films/1/" class="btn btn-sm btn-primary">View</a>
            </td>
        </tr>
    </tbody>
</table>
```

## Layout System (레이아웃 시스템)

### Container (컨테이너)

```html
<div class="container">
    <!-- Content here -->
</div>
```

- 최대 너비: 1200px
- 반응형 패딩: 1rem (모바일: 20px)

### Grid System (그리드 시스템)

```html
<div class="row">
    <div class="col-md-4 col-sm-6">
        <!-- Column 1 -->
    </div>
    <div class="col-md-4 col-sm-6">
        <!-- Column 2 -->
    </div>
    <div class="col-md-4 col-sm-12">
        <!-- Column 3 -->
    </div>
</div>
```

## Responsive Breakpoints (반응형 브레이크포인트)

| 브레이크포인트 | 최소 너비 | 대상 디바이스 |
|--------------|----------|--------------|
| xs | < 576px | 모바일 (세로) |
| sm | ≥ 576px | 모바일 (가로) |
| md | ≥ 768px | 태블릿 |
| lg | ≥ 992px | 노트북 |
| xl | ≥ 1200px | 데스크톱 |
| xxl | ≥ 1400px | 큰 화면 |

## Icons (아이콘)

### Emoji Icons (이모지 아이콘)

| 아이콘 | 용도 |
|------|------|
| 🎬 | 영화 |
| 👥 | 배우 |
| 🏪 | 매장 |
| 👤 | 고객 |
| 💰 | 결제 |
| 📅 | 대여 |
| 📊 | 통계 |

### SVG Icons (SVG 아이콘)

향후 Font Awesome이나 Heroicons와 같은 SVG 아이콘 라이브러리 통합 고려

## Animation (애니메이션)

### Transitions (전환 효과)

```css
/* 기본 전환 */
transition: all 0.3s ease;

/* 호버 효과 */
.card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
}
```

### Keyframes (키프레임)

```css
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideDown {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}
```

## Accessibility (접근성)

### ARIA Labels (ARIA 라벨)

```html
<button aria-label="Close modal" class="btn-close">&times;</button>
<nav aria-label="Main navigation">...</nav>
```

### Keyboard Navigation (키보드 네비게이션)

- `Tab`: 포커스 이동
- `Shift + Tab`: 포커스 역방향 이동
- `Enter`: 링크/버튼 활성화
- `Escape`: 모달 닫기

### Focus Indicators (포커스 표시기)

```css
:focus-visible {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}
```

## Django Template Integration (Django 템플릿 통합)

### Base Template (기본 템플릿)

```html
<!-- sakila_app/templates/sakila_app/base.html -->
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Sakila{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'sakila_app/css/main.css' %}">
</head>
<body>
    <nav class="navbar">{% include "sakila_app/partials/navbar.html" %}</nav>

    <main class="main-content">
        {% block content %}{% endblock %}
    </main>

    <footer class="footer">{% include "sakila_app/partials/footer.html" %}</footer>

    <script src="{% static 'sakila_app/js/main.js' %}"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

### Template Inheritance (템플릿 상속)

```html
<!-- sakila_app/templates/sakila_app/film_list.html -->
{% extends "sakila_app/base.html" %}

{% block title %}Films - {% endblock %}

{% block content %}
<div class="container">
    <h1>Film Catalog</h1>
    <div class="film-grid">
        {% for film in films %}
            {% include "sakila_app/partials/film_card.html" %}
        {% endfor %}
    </div>
</div>
{% endblock %}
```

---

**Next Step**: Phase 6 - UI 구현
