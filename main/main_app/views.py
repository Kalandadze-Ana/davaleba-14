from django.shortcuts import render
from .models import Customer, Product, Cart

# Create your views here.

def home(request):
    return render(request, 'home.html')


def products(request):
    all_products = Product.objects.all()
    context = {'products': all_products}
    return render(request, 'products.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def cart(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    items = Cart.objects.filter(customer=customer)
    total = sum(item.product.price * item.quantity for item in items)
    context = {'customer': customer, 'items': items, 'total': total}
    return render(request, 'cart.html', context)