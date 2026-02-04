from django.db import models


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address'

    def __str__(self):
        return self.address


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city'

    def __str__(self):
        return self.city


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    active = models.CharField(max_length=1)
    create_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'language'

    def __str__(self):
        return self.name


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.CharField(max_length=4, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='films')
    original_language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, related_name='original_films')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film'

    def __str__(self):
        return self.title


class FilmActor(models.Model):
    # SQLite의 rowid를 명시적으로 primary key로 사용
    id = models.IntegerField(db_column='rowid', primary_key=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, db_column='actor_id', related_name='film_actors')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, db_column='film_id', related_name='film_actors')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'

    def __str__(self):
        return f"{self.actor} in {self.film}"


class FilmCategory(models.Model):
    # SQLite의 rowid를 명시적으로 primary key로 사용
    id = models.IntegerField(db_column='rowid', primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, db_column='film_id', related_name='film_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id', related_name='film_categories')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film', 'category'),)

    def __str__(self):
        return f"{self.film} - {self.category}"


class FilmText(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_text'

    def __str__(self):
        return self.title


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='managed_stores')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store'

    def __str__(self):
        return f"Store {self.store_id}"


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventory'

    def __str__(self):
        return f"Inventory {self.inventory_id}: {self.film}"


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    picture = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='staff_members')
    active = models.SmallIntegerField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)

    def __str__(self):
        return f"Rental {self.rental_id}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'

    def __str__(self):
        return f"Payment {self.payment_id}: ${self.amount}"
