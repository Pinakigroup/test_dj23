from django.db import models
from category.models import Category
from stock.models import Stock
from datetime import date
# Create your models here.


class Store2(models.Model):
    address = models.CharField(max_length=124)
    birth_date = models.DateField(blank=True, null=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return self.address
    
    def age(self):
        today = date.today()
        years_difference = today.year - self.birth_date.year
        is_before_birthday = (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        if is_before_birthday:
            return years_difference - 1
        return years_difference