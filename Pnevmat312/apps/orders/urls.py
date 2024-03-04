from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
]