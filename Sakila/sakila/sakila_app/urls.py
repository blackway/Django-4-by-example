from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sakila_app'

# API Router setup
router = DefaultRouter()
router.register(r'films', views.FilmViewSet, basename='api-film')
router.register(r'actors', views.ActorViewSet, basename='api-actor')
router.register(r'categories', views.CategoryViewSet, basename='api-category')
router.register(r'customers', views.CustomerViewSet, basename='api-customer')
router.register(r'stores', views.StoreViewSet, basename='api-store')

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Actor URLs
    path('actors/', views.ActorListView.as_view(), name='actor_list'),
    path('actors/<int:pk>/', views.ActorDetailView.as_view(), name='actor_detail'),

    # Film URLs
    path('films/', views.FilmListView.as_view(), name='film_list'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),

    # Customer URLs
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),

    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    # Language URLs
    path('languages/', views.LanguageListView.as_view(), name='language_list'),
    path('languages/<int:pk>/', views.LanguageDetailView.as_view(), name='language_detail'),

    # Store URLs
    path('stores/', views.StoreListView.as_view(), name='store_list'),
    path('stores/<int:pk>/', views.StoreDetailView.as_view(), name='store_detail'),

    # Staff URLs
    path('staff/', views.StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff_detail'),

    # Rental URLs
    path('rentals/', views.RentalListView.as_view(), name='rental_list'),
    path('rentals/<int:pk>/', views.RentalDetailView.as_view(), name='rental_detail'),

    # Inventory URLs
    path('inventory/', views.InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='inventory_detail'),

    # Payment URLs
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),

    # Address URLs
    path('addresses/', views.AddressListView.as_view(), name='address_list'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),

    # City URLs
    path('cities/', views.CityListView.as_view(), name='city_list'),
    path('cities/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),

    # Country URLs
    path('countries/', views.CountryListView.as_view(), name='country_list'),
    path('countries/<int:pk>/', views.CountryDetailView.as_view(), name='country_detail'),

    # API URLs - prefix with 'api'
    path('api/', include(router.urls)),
]
