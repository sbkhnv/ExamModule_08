from django.contrib import admin
from .models import Payment, Product, Category, Price, User

admin.site.register([Payment, Product, Category,Price, User])