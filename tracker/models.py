from django.db import models
from datetime import date

# Create your models here.

class CreditCard(models.Model):
    card_name =models.CharField(max_length=40)
    credit_limit =models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.card_name} - Limit: {self.credit_limit}'

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=date.today)
    class Category(models.TextChoices):
        income = 'Income'
        need ='Need'
        want ='Want'
        saving ='Saving'
    category = models.CharField(max_length=10, choices=Category.choices)

    
    class PaymentMethod(models.TextChoices):
        cash = 'Cash'
        credit_card= 'Credit Card'

        
    
    def __str__(self):
        return f'{self.title} : {self.amount} on {self.date}'
    
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    
    description = models.CharField(max_length=100)


