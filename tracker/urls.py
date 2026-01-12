from django.urls import path
from .views import all_transactions, transaction_detail, creditcard_detail, all_creditcards

urlpatterns = [
    path('transactions/', all_transactions, name='transactions_list'),
    path('transactions/<int:id>/', transaction_detail, name='transaction-detail'),
    path('creditcards/', all_creditcards,name='creditcards_list'),
    path('creditcards/<int:number>/', creditcard_detail, name='creditcard-detail')

]