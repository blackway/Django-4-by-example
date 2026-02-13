"""
Serializers for Sakila API
"""
from rest_framework import serializers
from .models import (
    Film, Actor, Category, Customer,
    Rental, Payment, Inventory, Store, Staff, Address
)


class CategorySerializer(serializers.ModelSerializer):
    """카테고리 시리얼라이저"""

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'last_update']


class LanguageSerializer(serializers.Serializer):
    """언어 시리얼라이저 (모델이 아닌 dict에서 사용)"""

    language_id = serializers.IntegerField()
    name = serializers.CharField()


class ActorBasicSerializer(serializers.ModelSerializer):
    """배우 기본 시리얼라이저"""

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ['actor_id', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj):
        """전체 이름을 반환합니다."""
        return f"{obj.first_name} {obj.last_name}"


class ActorSerializer(serializers.ModelSerializer):
    """배우 상세 시리얼라이저"""

    full_name = serializers.SerializerMethodField()
    film_count = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = [
            'actor_id', 'first_name', 'last_name', 'full_name',
            'film_count', 'last_update'
        ]

    def get_full_name(self, obj):
        """전체 이름을 반환합니다."""
        return f"{obj.first_name} {obj.last_name}"

    def get_film_count(self, obj):
        """출연 영화 수를 반환합니다."""
        return obj.film_actors.count()


class FilmSerializer(serializers.ModelSerializer):
    """영화 시리얼라이저"""

    categories = serializers.SerializerMethodField()
    actors = ActorBasicSerializer(many=True, read_only=True, source='film_actors.actor')
    language_name = serializers.CharField(source='language.name', read_only=True)
    original_language_name = serializers.CharField(
        source='original_language.name',
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = Film
        fields = [
            'film_id', 'title', 'description', 'release_year',
            'language', 'language_name', 'original_language_name',
            'rental_duration', 'rental_rate', 'length',
            'replacement_cost', 'rating', 'special_features',
            'categories', 'actors', 'last_update'
        ]

    def get_categories(self, obj):
        """영화의 카테고리 목록을 반환합니다."""
        return [cat.category_id for cat in obj.film_categories.all()]


class FilmListSerializer(serializers.ModelSerializer):
    """영화 목록 전용 시리얼라이저"""

    categories = serializers.SerializerMethodField()
    language_name = serializers.CharField(source='language.name', read_only=True)
    actor_count = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = [
            'film_id', 'title', 'description', 'release_year',
            'language_name', 'rental_duration', 'rental_rate',
            'length', 'rating', 'categories', 'actor_count'
        ]

    def get_categories(self, obj):
        """영화의 카테고리 목록을 반환합니다."""
        return [cat.category.name for cat in obj.film_categories.all()]

    def get_actor_count(self, obj):
        """출연 배우 수를 반환합니다."""
        return obj.film_actors.count()


class FilmDetailSerializer(FilmSerializer):
    """영화 상세 시리얼라이저"""

    category_names = serializers.SerializerMethodField()

    class Meta(FilmSerializer.Meta):
        fields = FilmSerializer.Meta.fields + ['category_names']

    def get_category_names(self, obj):
        """영화의 카테고리 이름 목록을 반환합니다."""
        return [cat.category.name for cat in obj.film_categories.all()]


class AddressSerializer(serializers.ModelSerializer):
    """주소 시리얼라이저"""

    city_name = serializers.CharField(source='city.city', read_only=True)
    country_name = serializers.CharField(source='city.country.country', read_only=True)

    class Meta:
        model = Address
        fields = [
            'address_id', 'address', 'address2', 'district',
            'city', 'city_name', 'country_name', 'postal_code',
            'phone', 'last_update'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    """고객 시리얼라이저"""

    full_name = serializers.SerializerMethodField()
    address = AddressSerializer(read_only=True)
    store_id = serializers.IntegerField(source='store.store_id', read_only=True)
    rental_count = serializers.SerializerMethodField()
    payment_count = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = [
            'customer_id', 'store_id', 'first_name', 'last_name',
            'full_name', 'email', 'address', 'active', 'create_date',
            'rental_count', 'payment_count', 'last_update'
        ]

    def get_full_name(self, obj):
        """전체 이름을 반환합니다."""
        return f"{obj.first_name} {obj.last_name}"

    def get_rental_count(self, obj):
        """대여 횟수를 반환합니다."""
        return obj.rental_set.count()

    def get_payment_count(self, obj):
        """결제 횟수를 반환합니다."""
        return obj.payment_set.count()


class StoreSerializer(serializers.ModelSerializer):
    """매장 시리얼라이저"""

    address = AddressSerializer(read_only=True)
    manager_name = serializers.CharField(source='manager_staff.full_name', read_only=True)

    class Meta:
        model = Store
        fields = [
            'store_id', 'manager_name', 'address',
            'last_update'
        ]


class RentalSerializer(serializers.ModelSerializer):
    """대여 시리얼라이저"""

    customer_name = serializers.CharField(source='customer.full_name', read_only=True)
    film_title = serializers.CharField(source='inventory.film.title', read_only=True)
    staff_name = serializers.CharField(source='staff.full_name', read_only=True)

    class Meta:
        model = Rental
        fields = [
            'rental_id', 'rental_date', 'inventory',
            'customer', 'customer_name', 'film_title',
            'return_date', 'staff', 'staff_name', 'last_update'
        ]


class PaymentSerializer(serializers.ModelSerializer):
    """결제 시리얼라이저"""

    customer_name = serializers.CharField(source='customer.full_name', read_only=True)
    staff_name = serializers.CharField(source='staff.full_name', read_only=True)
    rental_id = serializers.IntegerField(source='rental.rental_id', read_only=True, allow_null=True)

    class Meta:
        model = Payment
        fields = [
            'payment_id', 'customer', 'customer_name',
            'staff', 'staff_name', 'rental_id',
            'amount', 'payment_date', 'last_update'
        ]


class InventorySerializer(serializers.ModelSerializer):
    """재고 시리얼라이저"""

    film_title = serializers.CharField(source='film.title', read_only=True)
    store_id = serializers.IntegerField(source='store.store_id', read_only=True)

    class Meta:
        model = Inventory
        fields = [
            'inventory_id', 'film', 'film_title',
            'store', 'store_id', 'last_update'
        ]
