from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BillItem, Bill, Sale, Stock
from decimal import Decimal

@receiver(post_save, sender=BillItem)
def update_bill(sender, instance, created, **kwargs):

    if created:
        bill, ct = Bill.objects.get_or_create(customer=instance.customer)
        if ct:
            bill.customer = instance.customer
            bill.billitems = str(instance.product.name) + " : " + str(instance.product.price) + " x " + str(instance.quantity) + "\n"
            price = Decimal(instance.product.price) * Decimal(instance.quantity)
            bill.total_amount = price
            bill.save()
        else:
            bill.customer = instance.customer
            if bill.billitems.split(':')[0].strip() == instance.product.name:
                q = int(bill.billitems.split('x')[-1].strip()) + 1
                bill.billitems = str(instance.product.name) + " : " + str(instance.product.price) + " x " + str(q) + " "
            else:
                bill.billitems += str(instance.product.name) + " : " + str(instance.product.price) + " x " + str(instance.quantity) + " "
            price = Decimal(instance.product.price) * Decimal(instance.quantity)
            bill.total_amount += price
            bill.save()

@receiver(post_save, sender=BillItem)
def update_bill(sender, instance, created, **kwargs):
    if created:
        stock, _ = Stock.objects.get_or_create(product=instance.product)
        stock.product = instance.product
        stock.quantity -= instance.quantity
        stock.save()

@receiver(post_save, sender=BillItem)
def update_bill(sender, instance, created, **kwargs):
    if created:
        sale_amount = Decimal(instance.product.price) * Decimal(instance.quantity)
        sale, ct = Sale.objects.get_or_create(product=instance.product)
        if ct :
            sale.product = instance.product
            sale.stock_quantity = instance.quantity
            sale.sales = sale_amount
            sale.save()
        else:
            sale.product = instance.product
            sale.stock_quantity += instance.quantity
            sale.sales += sale_amount
            sale.save()




