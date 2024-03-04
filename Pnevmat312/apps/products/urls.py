from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/<int:product_id>/', views.product, name='product'),
    path('category/', views.category, name='category'),
    path('actions/<int:id_action>/', views.action, name='action'),
    path('test/', views.test, name='test'),
    path('fabricators/', views.fabricators, name='fabricators'),
    path('pay/', views.pay, name='pay'),
    path('guarantees/', views.guarantees, name='guarantees')
]