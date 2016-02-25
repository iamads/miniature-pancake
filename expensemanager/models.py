from django.db import models
from datetime import datetime
# Create your models here.
categories = Category.objects.all()
category_choice = tuple([(i,i) for i in categories])
class Transaction(models.Model):
    userid= models.IntegerField()
    name = models.CharField(max_length=300)
    amount = models.FloatField(default=0.00)
    category = models.CharField(max_length=50, blank=True)
    transaction_date = models.DateField()   # change this to be able to select date
    is_debit = models.BooleanField(default=True)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    public = models.BooleanField(default=False)


    def __str__(self):
        return self.name
