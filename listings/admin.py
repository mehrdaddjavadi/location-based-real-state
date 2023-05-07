from django.contrib import admin
from .models import Listing
# Register your models here.
@admin.register(Listing)
class UserAdmin(admin.ModelAdmin):
    pass