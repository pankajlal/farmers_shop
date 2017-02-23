from __future__ import unicode_literals

from django.db import models
from sku.models import SKU, Unit
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Locality(models.Model):
    address = models.TextField()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Localities"

class Community(models.Model):
    community_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=20)
    locality = models.ForeignKey(Locality)

    def __str__(self):
        return "%s %s"%(self.community_name, self.street_name)

    class Meta:
        verbose_name_plural = "Communities"

class Customer(models.Model):
    u = models.OneToOneField(User)
    phone = PhoneNumberField()
    door_number = models.CharField(max_length=20)
    community = models.ForeignKey(Community)

    def __str__(self):
        return "%s %s"%(self.u.first_name, self.u.last_name)

class Vendor(models.Model):
    u = models.OneToOneField(User)
    phone = PhoneNumberField()
    address = models.TextField()

class MelaLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Mela Locations"

class Mela(models.Model):
    date = models.DateField()


class Item(models.Model):
    sku = models.ForeignKey(SKU)
    min_qty = models.IntegerField()
    mela = models.ForeignKey(Mela)
    ordered_loose = models.BooleanField(default=False)
    sold_loose = models.BooleanField(default=False)
    unit = models.ForeignKey(Unit)

class DaysItem(models.Model):
    item = models.ForeignKey(Item)
    price_per_unit = models.IntegerField()
    mela = models.ForeignKey(Mela)

class Cart(models.Model):
    DRAFT = 'DRAFT'
    COMMITTED = 'COMMITTED'
    ORDERED = 'ORDERED'
    EXPIRED = 'EXPIRED'
    UNIT_CHOICES = (
        (DRAFT, 'Draft'),
        (COMMITTED, 'Committed'),
        (ORDERED, 'Ordered'),
        (EXPIRED, 'Expired'),
    )
    customer = models.ForeignKey(User)
    created = models.DateField(auto_now_add=True)
    mela = models.ForeignKey(Mela)
    location = models.ForeignKey(MelaLocation)
    order_value = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    order_time = models.DateTimeField
    bill_value = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)

class CartItem(models.Model):
    daysItem = models.ForeignKey(DaysItem)
    order_qty = models.IntegerField()
    order_value = models.DecimalField(decimal_places=2, max_digits=6)
    sale_qty = models.IntegerField()
    sale_value = models.DecimalField(decimal_places=2, max_digits=6)

class LocationItem(models.Model):
    location = models.ForeignKey(MelaLocation)
    daysItem = models.ForeignKey(DaysItem)
    order_qty = models.IntegerField()
    order_value = models.DecimalField(decimal_places=2, max_digits=8)
    deliver_qty = models.IntegerField()
    deliver_value = models.DecimalField(decimal_places=2, max_digits=8)

class LocationValue(models.Model):
    mela = models.ForeignKey(Mela)
    value = models.DecimalField(decimal_places=2, max_digits=8)

class MelaItem(models.Model):
    daysItem = models.ForeignKey(DaysItem)
    order_qty = models.IntegerField()
    order_value = models.DecimalField(decimal_places=2, max_digits=8)
    deliver_qty = models.IntegerField()
    deliver_value = models.DecimalField(decimal_places=2, max_digits=8)

class MelaValue(models.Model):
    mela = models.ForeignKey(Mela)
    value = models.DecimalField(decimal_places=2, max_digits=8)
