from django.contrib import admin
from .models import Transaction, CreditCard
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'category', 'payment_method')
    list_filter = ('category', 'payment_method', 'date')
    search_fields = ('title',)


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'credit_limit')
    search_fields = ('card_name',)

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CreditCard, CreditCardAdmin)



