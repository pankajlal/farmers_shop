from django.contrib import admin
from .models import MelaLocation, Locality, Community
from .models import Customer

# Register your models here.
@admin.register(MelaLocation)
class MelaLocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    pass

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass