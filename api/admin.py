from django.contrib import admin
from .models import Product, Customer, Stock, Bill, BillItem, Sale

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','price', 'created_by']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','contact_number','email']

@admin.register(Stock)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','updated_at']

@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = ['customer','product','quantity']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['customer','billitems','total_amount','paid_amount','payment_method','payment_status','created_at']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['product','stock_quantity','sales']