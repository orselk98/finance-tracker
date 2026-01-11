from django.urls import path
from .views import all_transactions, transaction_detail

urlpatterns = [
    path('transactions/', all_transactions, name='transactions_list'),
    path('transactions/<int:id>/', transaction_detail, name='transaction-detail'),
]