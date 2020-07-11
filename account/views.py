from django.shortcuts import render

from .models import *

from django.http import HttpResponse
# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    orders_delivered = orders.filter(status = 'Delivered').count()
    pending_orders = orders.filter(status = 'Pending').count()

    context = {'customers': customers, 'orders' : orders,
    'total_orders':total_orders, 'orders_delivered': orders_delivered,
    'pending_orders': pending_orders}

    return render(request,'account/dashboard.html', context )

def products(request):
    products = Product.objects.all()
    return render(request,'account/products.html', {'products': products})

def contact(request):
    return HttpResponse('Contact us')

def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    # to get all objects of customer we can use order set
    # orders = Order.objects.filter(customer = pk)

    orders = customer.order_set.all()

    order_count = orders.count()

    context = {'customer': customer, 'orders' : orders,'order_count':order_count}

    return render(request, 'account/customers.html', context)

