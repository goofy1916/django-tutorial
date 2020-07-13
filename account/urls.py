from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('contact/', views.contact, name='contact'),
    path('neworder/', views.createOrder, name='neworder'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order')
]
