from django.contrib import admin
from .models import StoreBill, StoreItem

# Register your models here. StoreItem


@admin.register(StoreBill)
class StoreBillAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'buyer_name', 'report', 'report_no', 'report_date', 'po_no', 'lc', 'style_no', 'file_no', 'lot_no', 'fabric_detail', 'store_location', 'order_qty']
    
@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ['stock', 'category', 'quantity', 'unit_price', 'uom', 'fabric_color']