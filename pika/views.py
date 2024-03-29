from django.shortcuts import render
from .models import*
# Create your views here.
def store(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()   # parent ko pehle call then . child then some attribute like _set
    else:
        items = []
        order = {'cart_price': 0, 'cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()  # parent ko pehle call then . child then some attribute like _set
    else:
        items = []
        order = {'cart_price': 0, 'cart_items': 0}
    context = {'items': items, 'order': order}

    return render(request, 'checkout.html', context)