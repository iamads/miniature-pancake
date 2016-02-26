from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,primary_key=True)


    def __str__(self):
        return self.name

class Transaction(models.Model):
    userid= models.IntegerField()
    name = models.CharField(max_length=300)
    amount = models.FloatField(default=0.00)
    category = models.ForeignKey(Category)
    transaction_date = models.DateField()
    is_debit = models.BooleanField(default=True)


    def __str__(self):
        return self.name

