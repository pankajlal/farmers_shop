from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SKUCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SKU Categories"

class Unit(models.Model):
    KG = 'KG'
    GM = 'GM'
    NOS = 'NO'
    LTR = 'L'
    ML = 'ML'
    UNIT_CHOICES = (
        (KG, 'Kg'),
        (GM, 'Gm'),
        (NOS, 'Nos'),
        (LTR, 'Ltr'),
        (ML, 'Ml')
    )
    utype = models.CharField(max_length=2, choices=UNIT_CHOICES, default=None, unique=True)

    def __str__(self):
        return self.utype


class SKU(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SKUCategory)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SKUs"





