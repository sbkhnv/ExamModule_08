from django.urls import path
from .views import UsersView,FurniView

urlpatterns = [
    path("users/", UsersView.as_view(),name="users"),
    path("furni/",FurniView.as_view(),name="furni")
]