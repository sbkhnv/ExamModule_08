from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductView.as_view(), name='shop'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/delete/<int:pk>/', product_delete, name='delete'),
    path('products/add/', AddProduct.as_view(), name='add_product'),
    path('price/', PriceView.as_view(), name='coupons'),
    path('price/<int:pk>/', PriceView.as_view(), name='coupon-detail'),
    path('price/delete/<int:pk>/', coupon_delete, name='delete-coupon'),
    path('price/add/', AddPrice.as_view(), name='add_coupon'),
    path('payments/', PaymentView.as_view(), name='payments'),
    path('payments/<int:pk>/', PaymentView.as_view(), name='payment-detail'),
    path('payments/delete/<int:pk>/', pay_delete, name='delete-payment'),
    path('payments/add/', AddPay.as_view(), name='add_payment'),
    path('user/', UsersView.as_view(), name='telegram_users'),
    path('user/<int:pk>/', UsersView.as_view(), name='telegram_user-detail'),
    path('user/delete/<int:pk>/', user_delete, name='delete-telegram_user'),
    path('user/add/', AddUser.as_view(), name='add_telegram_user'),
    path('service/', StaffView.as_view(), name='service'),
]
