from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import *

def order(request):
    try:
        Profile = apps.get_model('users.Profile')
        profile = Profile.objects.get(profile=request.user)
        orders = Order.objects.filter(id_user=profile)
        carts = []
        for order in orders:
            carts += Cart.objects.filter(id_order=order)
    except TypeError:
        return HttpResponse('Пожалуйста войдите в аккаунт, чтобы пользоваться корзиной')
    
    if request.method == 'POST':
        if 'complete' in request.POST:
            address = request.POST.get('address')
            orderText = request.POST.get('orders')
            for order in orders:
                if order.placed is not True:
                    order.address = address
                    order.orderText = orderText
                    order.date_executed = datetime.datetime.today() + datetime.timedelta(days=10)
                    order.placed = True
                    
                    order.save(update_fields=['address', 'date_executed', 'placed', 'orderText'])
                    for cart in carts:
                        cart.delete()
                    print(carts)
            return HttpResponseRedirect('/user/profile/')
    else:
        return render(request, 'order.html', {'carts': carts, 'orders': orders})


def delete_cart(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete_cart()
    return HttpResponseRedirect('/orders/')

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete_order()
    return HttpResponseRedirect('/user/profile/')