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
