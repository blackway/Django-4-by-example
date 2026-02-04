from django.contrib import admin
from .models import (
    Actor, Address, Category, City, Country, Customer,
    Film, FilmActor, FilmCategory, FilmText, Inventory,
    Language, Payment, Rental, Staff, Store
)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['actor_id', 'first_name', 'last_name', 'last_update']
    search_fields = ['first_name', 'last_name']
    list_filter = ['last_update']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_id', 'address', 'district', 'city', 'postal_code', 'phone']
    search_fields = ['address', 'district', 'postal_code']
    list_filter = ['district']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name', 'last_update']
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id', 'city', 'country', 'last_update']
    search_fields = ['city']
    list_filter = ['country']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_id', 'country', 'last_update']
    search_fields = ['country']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'first_name', 'last_name', 'email', 'store', 'active', 'create_date']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['active', 'store', 'create_date']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['film_id', 'title', 'release_year', 'language', 'rental_rate', 'length', 'rating']
    search_fields = ['title', 'description']
    list_filter = ['release_year', 'language', 'rating']


@admin.register(FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    list_display = ['actor', 'film', 'last_update']
    search_fields = ['actor__first_name', 'actor__last_name', 'film__title']
    list_filter = ['last_update']


@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = ['film', 'category', 'last_update']
    search_fields = ['film__title', 'category__name']
    list_filter = ['category']


@admin.register(FilmText)
class FilmTextAdmin(admin.ModelAdmin):
    list_display = ['film_id', 'title']
    search_fields = ['title', 'description']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['inventory_id', 'film', 'store', 'last_update']
    search_fields = ['film__title']
    list_filter = ['store']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language_id', 'name', 'last_update']
    search_fields = ['name']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'customer', 'staff', 'amount', 'payment_date']
    search_fields = ['customer__first_name', 'customer__last_name']
    list_filter = ['payment_date', 'staff']


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['rental_id', 'customer', 'inventory', 'rental_date', 'return_date', 'staff']
    search_fields = ['customer__first_name', 'customer__last_name']
    list_filter = ['rental_date', 'return_date', 'staff']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'first_name', 'last_name', 'email', 'store', 'active', 'username']
    search_fields = ['first_name', 'last_name', 'email', 'username']
    list_filter = ['active', 'store']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_id', 'manager_staff', 'address', 'last_update']
    search_fields = ['manager_staff__first_name', 'manager_staff__last_name']
