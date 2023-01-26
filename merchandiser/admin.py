from django.contrib import admin
from .models import Merchandiser

# Register your models here.
@admin.register(Merchandiser)
class MerchandiserAdmin(admin.ModelAdmin):
    list_display = ['office_id', 'name', 'phone', 'email', 'designation', 'access_area', 'profile_img', 'joining_date', 'dob']
