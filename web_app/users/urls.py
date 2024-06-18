from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserInfoView.as_view(), name='users'),
    path('users/<int:pk>/', UserInfoView.as_view(), name='user_detail'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),
    path('users/add/', AddUser.as_view(), name='user_add'),
    path('staffs/', StaffView.as_view(), name='staffs'),
    path('staffs/<int:pk>/', StaffView.as_view(), name='staff_detail'),
    path('staffs/delete/<int:pk>/', staff_delete, name='staff_delete'),
    path('staffs/add/', AddStaff.as_view(), name='staff_add'),
    path('blogs/',  BlogView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogView.as_view(), name='blog_detail'),
    path('blogs/delete/<int:pk>/', blog_delete, name='blog_delete'),
    path('blogs/add/', AddBlog.as_view(), name='blog_add'),
    path('problems/', ProblemView.as_view(), name='problems'),
    path('problems/<int:pk>/', ProblemView.as_view(), name='problem_detail'),
    path('contact', AddProblem.as_view(), name='contact'),
    path('problems/delete/<int:pk>/', problem_delete, name='problem_delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
    path('myprofile/delete/', profile_delete, name='profile_delete'),
    path('myprofile/edit/', edit_profile, name='edit_profile'),
    path('thank/', ThankView.as_view(), name='thanks')
]