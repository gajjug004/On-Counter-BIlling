from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Customer, Bill, BillItem, Stock, Sale
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillSerializer, BillItemSerializer, StockSerializer, SaleSerializer, StockSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticated]

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticated]

class StockListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # permission_classes = [IsAuthenticated]

class StockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # permission_classes = [IsAuthenticated]

class BillItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
    # permission_classes = [IsAuthenticated]

class BillItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
    # permission_classes = [IsAuthenticated]

class BillListAPIView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class SaleListAPIView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    # permission_classes = [IsAuthenticated]

class SaleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    # permission_classes = [IsAuthenticated]

class StockListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer