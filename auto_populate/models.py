from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name