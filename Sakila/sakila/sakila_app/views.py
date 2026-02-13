from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Actor, Address, Category, City, Country, Customer,
    Film, FilmActor, FilmCategory, Inventory,
    Language, Payment, Rental, Staff, Store
)
from .serializers import (
    ActorSerializer, CategorySerializer, CustomerSerializer,
    FilmSerializer, FilmListSerializer, FilmDetailSerializer,
    RentalSerializer, PaymentSerializer, InventorySerializer,
    StoreSerializer
)


# Home view
def home(request):
    """홈 페이지 - 모든 모델에 대한 링크 제공"""
    context = {
        'models': [
            {'name': 'Actors', 'url': 'actor_list', 'count': Actor.objects.count()},
            {'name': 'Films', 'url': 'film_list', 'count': Film.objects.count()},
            {'name': 'Customers', 'url': 'customer_list', 'count': Customer.objects.count()},
            {'name': 'Categories', 'url': 'category_list', 'count': Category.objects.count()},
            {'name': 'Languages', 'url': 'language_list', 'count': Language.objects.count()},
            {'name': 'Stores', 'url': 'store_list', 'count': Store.objects.count()},
            {'name': 'Staff', 'url': 'staff_list', 'count': Staff.objects.count()},
            {'name': 'Rentals', 'url': 'rental_list', 'count': Rental.objects.count()},
            {'name': 'Inventory', 'url': 'inventory_list', 'count': Inventory.objects.count()},
            {'name': 'Payments', 'url': 'payment_list', 'count': Payment.objects.count()},
            {'name': 'Addresses', 'url': 'address_list', 'count': Address.objects.count()},
            {'name': 'Cities', 'url': 'city_list', 'count': City.objects.count()},
            {'name': 'Countries', 'url': 'country_list', 'count': Country.objects.count()},
        ]
    }
    return render(request, 'sakila_app/home.html', context)


# Actor Views
class ActorListView(generic.ListView):
    model = Actor
    template_name = 'sakila_app/actor_list.html'
    context_object_name = 'actors'
    paginate_by = 20


class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'sakila_app/actor_detail.html'
    context_object_name = 'actor'


# Film Views
class FilmListView(generic.ListView):
    model = Film
    template_name = 'sakila_app/film_list.html'
    context_object_name = 'films'
    paginate_by = 20


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = 'sakila_app/film_detail.html'
    context_object_name = 'film'


# Customer Views
class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'sakila_app/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 20


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'sakila_app/customer_detail.html'
    context_object_name = 'customer'


# Category Views
class CategoryListView(generic.ListView):
    model = Category
    template_name = 'sakila_app/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'sakila_app/category_detail.html'
    context_object_name = 'category'


# Language Views
class LanguageListView(generic.ListView):
    model = Language
    template_name = 'sakila_app/language_list.html'
    context_object_name = 'languages'


class LanguageDetailView(generic.DetailView):
    model = Language
    template_name = 'sakila_app/language_detail.html'
    context_object_name = 'language'


# Store Views
class StoreListView(generic.ListView):
    model = Store
    template_name = 'sakila_app/store_list.html'
    context_object_name = 'stores'


class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'sakila_app/store_detail.html'
    context_object_name = 'store'


# Staff Views
class StaffListView(generic.ListView):
    model = Staff
    template_name = 'sakila_app/staff_list.html'
    context_object_name = 'staff_members'
    paginate_by = 20


class StaffDetailView(generic.DetailView):
    model = Staff
    template_name = 'sakila_app/staff_detail.html'
    context_object_name = 'staff'


# Rental Views
class RentalListView(generic.ListView):
    model = Rental
    template_name = 'sakila_app/rental_list.html'
    context_object_name = 'rentals'
    paginate_by = 20


class RentalDetailView(generic.DetailView):
    model = Rental
    template_name = 'sakila_app/rental_detail.html'
    context_object_name = 'rental'


# Inventory Views
class InventoryListView(generic.ListView):
    model = Inventory
    template_name = 'sakila_app/inventory_list.html'
    context_object_name = 'inventories'
    paginate_by = 20


class InventoryDetailView(generic.DetailView):
    model = Inventory
    template_name = 'sakila_app/inventory_detail.html'
    context_object_name = 'inventory'


# Payment Views
class PaymentListView(generic.ListView):
    model = Payment
    template_name = 'sakila_app/payment_list.html'
    context_object_name = 'payments'
    paginate_by = 20


class PaymentDetailView(generic.DetailView):
    model = Payment
    template_name = 'sakila_app/payment_detail.html'
    context_object_name = 'payment'


# Address Views
class AddressListView(generic.ListView):
    model = Address
    template_name = 'sakila_app/address_list.html'
    context_object_name = 'addresses'
    paginate_by = 20


class AddressDetailView(generic.DetailView):
    model = Address
    template_name = 'sakila_app/address_detail.html'
    context_object_name = 'address'


# City Views
class CityListView(generic.ListView):
    model = City
    template_name = 'sakila_app/city_list.html'
    context_object_name = 'cities'
    paginate_by = 20


class CityDetailView(generic.DetailView):
    model = City
    template_name = 'sakila_app/city_detail.html'
    context_object_name = 'city'


# Country Views
class CountryListView(generic.ListView):
    model = Country
    template_name = 'sakila_app/country_list.html'
    context_object_name = 'countries'
    paginate_by = 20


class CountryDetailView(generic.DetailView):
    model = Country
    template_name = 'sakila_app/country_detail.html'
    context_object_name = 'country'


# =============================================================================
# API ViewSets
# =============================================================================

class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    """영화 API ViewSet"""

    queryset = Film.objects.select_related('language', 'original_language').prefetch_related(
        'film_categories__category',
        'film_actors__actor'
    ).all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating', 'release_year', 'language']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'release_year', 'rental_rate', 'length']
    ordering = ['title']

    def get_serializer_class(self):
        """액션에 따라 시리얼라이저 클래스를 반환합니다."""
        if self.action == 'list':
            return FilmListSerializer
        return FilmDetailSerializer

    @action(detail=True, methods=['get'])
    def actors(self, request, pk=None):
        """영화의 배우 목록을 반환합니다."""
        film = self.get_object()
        actors = film.film_actors.select_related('actor').all()
        serializer = ActorSerializer(
            [fa.actor for fa in actors],
            many=True
        )
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def categories(self, request, pk=None):
        """영화의 카테고리 목록을 반환합니다."""
        film = self.get_object()
        categories = film.film_categories.select_related('category').all()
        serializer = CategorySerializer(
            [fc.category for fc in categories],
            many=True
        )
        return Response(serializer.data)


class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    """배우 API ViewSet"""

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']

    @action(detail=True, methods=['get'])
    def films(self, request, pk=None):
        """배우의 출연 영화 목록을 반환합니다."""
        actor = self.get_object()
        film_actors = actor.film_actors.select_related('film').all()
        films = [fa.film for fa in film_actors]
        serializer = FilmListSerializer(films, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """카테고리 API ViewSet"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def films(self, request, pk=None):
        """카테고리의 영화 목록을 반환합니다."""
        category = self.get_object()
        film_categories = category.film_categories.select_related('film').all()
        films = [fc.film for fc in film_categories]
        serializer = FilmListSerializer(films, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """고객 API ViewSet"""

    queryset = Customer.objects.select_related('store', 'address__city__country').all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['active', 'store']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name', 'create_date']
    ordering = ['last_name', 'first_name']

    @action(detail=True, methods=['get'])
    def rentals(self, request, pk=None):
        """고객의 대여 기록을 반환합니다."""
        customer = self.get_object()
        rentals = customer.rental_set.select_related(
            'inventory__film', 'staff'
        ).all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def payments(self, request, pk=None):
        """고객의 결제 내역을 반환합니다."""
        customer = self.get_object()
        payments = customer.payment_set.select_related('staff').all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    """매장 API ViewSet"""

    queryset = Store.objects.select_related('manager_staff', 'address__city__country').all()
    serializer_class = StoreSerializer
    ordering = ['store_id']

    @action(detail=True, methods=['get'])
    def staff(self, request, pk=None):
        """매장의 직원 목록을 반환합니다."""
        store = self.get_object()
        staff_members = store.staff_members.select_related('address').all()
        data = [{
            'staff_id': s.staff_id,
            'full_name': f"{s.first_name} {s.last_name}",
            'email': s.email,
            'active': s.active
        } for s in staff_members]
        return Response(data)

    @action(detail=True, methods=['get'])
    def inventory(self, request, pk=None):
        """매장의 재고 목록을 반환합니다."""
        store = self.get_object()
        inventories = store.inventory_set.select_related('film').all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)
