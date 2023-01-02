from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(SaleBill)
admin.site.register(SaleItem)
admin.site.register(SaleBillDetails)