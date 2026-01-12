from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction, CreditCard
from .serializers import TransactionSerializer , CreditCardSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def all_transactions(request):
    if request.method =="GET":
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            qs =Transaction.objects.filter(date__range=[start_date, end_date])
        else:
            qs =Transaction.objects.all()
        serializer = TransactionSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method =="POST":
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def transaction_detail(request,id):
    try:
        transaction = Transaction.objects.get(id =id)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    
    if request.method =="PATCH":
        serializer = TransactionSerializer(transaction, data=request.data, partial=True) #partial update 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        transaction.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def all_creditcards(request):
    if request.method =='GET':
        qss = CreditCard.objects.all()
        serializer = CreditCardSerializer(qss, many =True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method =='POST':
        serializer = CreditCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PATCH', 'DELETE']) 
def creditcard_detail(request,number):
    try:
        creditcard = CreditCard.objects.get(id=number)
    except CreditCard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer =CreditCardSerializer(creditcard)
        return Response(serializer.data)
    
    if request.method =='PATCH':
        serializer =CreditCardSerializer(creditcard,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
        creditcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

