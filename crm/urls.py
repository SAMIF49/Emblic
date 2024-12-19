from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/delete/<int:customer_id>/', views.customer_delete, name='customer_delete'),
    path('add-customer/', views.add_customer, name='add_customer'),
]
