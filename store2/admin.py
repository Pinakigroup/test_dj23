from django.contrib import admin
from .models import Store2
# Register your models here. StoreItem


@admin.register(Store2)
class Store2Admin(admin.ModelAdmin):
    list_display = ['address', 'birth_date', 'category', 'stock']