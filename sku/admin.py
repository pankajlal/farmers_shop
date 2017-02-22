from django.contrib import admin

# Register your models here.
from .models import SKUCategory, SKU, Unit


admin.site.register(SKUCategory)

@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    def Units(self, obj):
        return obj.unit.all().values_list('utype', flat=True)
    list_display = ('name', 'Units')


admin.site.register(Unit)
