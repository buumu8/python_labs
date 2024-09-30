from django.db import models
from unicodedata import name


# Create your models here.


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        default=None,
        related_name="category_name",
    )

    def __str__(self):
        return self.name + " : " + self.cuisine


class Menuitems(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()


class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(max_length=255)


class Vehicle(models.Model):
    nmae = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="Vehicle"
    )


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
