from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import (
    Actor, Address, Category, City, Country, Customer,
    Film, FilmActor, FilmCategory, Inventory,
    Language, Payment, Rental, Staff, Store
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
