from django.db import models
from stock.models import Stock
from category. models import Category
from django.utils.timezone import now
from supplier.models import Supplier
# Create your models here.

class StoreBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False, related_name='suppliername')
    buyer_name = models.CharField(max_length=64, blank=False, null=True)
    REPORT = (
        ('', 'Select'),
        ('Invoice', 'Invoice'),
        ('DC', 'DC'),
    )
    report = models.CharField(max_length=64, null=True, blank=False, choices=REPORT)
    report_no = models.CharField(max_length=64, blank=True, null=True)
    report_date = models.DateField(default= now)
    po_no = models.CharField(max_length=64, blank=True, null=True)
    lc = models.CharField(max_length=64, blank=False, null=True)
    style_no = models.CharField(max_length=32, null=True, blank=True)
    file_no = models.CharField(max_length=64, blank=True, null=True)
    lot_no = models.CharField(max_length=64, blank=True, null=True)
    
    fabric_detail = models.TextField()
    store_location = models.CharField(max_length=64, blank=True, null=True)
    order_qty = models.IntegerField(default=0)
    
    # name = models.CharField(max_length=150)
    # phone = models.CharField(max_length=12)
    # address = models.CharField(max_length=200)
    # email = models.EmailField(max_length=254)

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return StoreItem.objects.filter(billno=self)
        
    def get_total_price(self):
        storeitems = StoreItem.objects.filter(billno=self)
        total = 0
        for item in storeitems:
            total += item.totalprice
        return total
    
class StoreItem(models.Model):
    billno = models.ForeignKey(StoreBill, on_delete = models.CASCADE, related_name='storebillno')
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, blank=False, null=True)
    
    quantity = models.IntegerField(default=1)
    unit_price = models.IntegerField(default=0)
    totalprice = models.IntegerField(default=0)
    fabric_color = models.CharField(max_length=64, blank=True, null=True)
    UOM = (
        ('', 'Select'),
        ('kg', 'kg'),
        ('miter', 'miter'),
        ('yard', 'yard'),
        ('pcs', 'pcs'),
        ('pound', 'pound'),
        ('g', 'g'),
        ('gg', 'gg'),
        ('litre', 'litre'),
        ('dg', 'dg'),
        ('1000 pcs', '1000 pcs'),
    )
    uom = models.CharField(max_length=64, null=True, blank=False, choices=UOM)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
class StoreBillDetails(models.Model):
    billno = models.ForeignKey(StoreBill, on_delete = models.CASCADE, related_name='storedetailsbillno')
    
    eway = models.CharField(max_length=50, blank=True, null=True)    
    veh = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)
    
    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)