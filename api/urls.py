from django.urls import path
from .views import EmployeeListView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView, BillItemListCreateAPIView, BillItemRetrieveUpdateDestroyAPIView, SaleListAPIView, SaleRetrieveAPIView, StockListCreateAPIView, StockRetrieveUpdateDestroyAPIView, BillListAPIView, BillRetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),
    path('stocks/', StockListCreateAPIView.as_view(), name='stock_list_create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyAPIView.as_view(), name='stock_retrieve_update_destroy'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer_list_create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer_retrieve_update_destroy'),
    path('billitems/', BillItemListCreateAPIView.as_view(), name='billitem_list_create'),
    path('billitems/<int:pk>/', BillItemRetrieveUpdateDestroyAPIView.as_view(), name='billitem_retrieve_update_destroy'),
    path('bills/', BillListAPIView.as_view(), name='bill_retrieve'),
    path('bills/<int:pk>/', BillRetrieveUpdateAPIView.as_view(), name='bill_retrieve_update_destroy'),
    path('analytics/sales/', SaleListAPIView.as_view(), name='sales_analytics'),
    path('analytics/sales/<int:pk>/', SaleRetrieveAPIView.as_view(), name='sales_analytics_retrieve_'),
]