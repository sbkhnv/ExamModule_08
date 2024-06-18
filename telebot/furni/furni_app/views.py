from django.shortcuts import render
from django.views import View
from .models import users,Furni


class UsersView(View):
    def get(self, request):
        users_1 = users.objects.all()
        return render(request,"users.html",{"users":users_1})


class FurniView(View):
    def get(self, request):
        furni_1 = Furni.objects.all()
        return render(request, "furni.html", {"furni": furni_1})

