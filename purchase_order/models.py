from django.db import models
from supplier.models import Supplier
from stock.models import Stock
# Create your models here.


#contains the purchase bills made
class PurchasesBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return PurchasesItem.objects.filter(billno=self)

    def get_total_price(self):
        purchaseitems = PurchasesItem.objects.filter(billno=self)
        total = 0
        for item in purchaseitems:
            total = total + item.totalprice
        return total

#contains the purchase stocks made   ----->purchase  (Liton)<-----
class PurchasesItem(models.Model):
    billno = models.ForeignKey(PurchasesBill, on_delete = models.CASCADE, related_name='purchasesbillno')
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name='purchasesitem')
    quantity = models.IntegerField(default=1)
    unit_price = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    
    
#contains the other details in the purchases bill
class PurchasesBillDetails(models.Model):
    billno = models.ForeignKey(PurchasesBill, on_delete = models.CASCADE, related_name='purchasesdetailsbillno')
    
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