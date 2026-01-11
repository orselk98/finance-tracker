from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def all_transactions(request):
    if request.method =="GET":
        qs =Transaction.objects.all()
        serializer = TransactionSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method =="POST":
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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





