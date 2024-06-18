from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'count', 'endurance', 'image']

    def save(self, commit=True):
        product = super().save(commit)
        product.save()
        return product


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'product_list', 'amount', 'pay_type', 'coupon']

    def save(self, commit=True):
        pay = super().save(commit)
        pay.save()
        return pay


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['code', 'value']

    def save(self, commit=True):
        coupon = super().save(commit)
        coupon.save()
        return coupon


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'fullname', 'chat_id']

    def save(self, commit=True):
        user = super().save(commit)
        user.save()
        return user