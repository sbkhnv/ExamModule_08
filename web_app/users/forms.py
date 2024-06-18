from django import forms
from .models import *
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class Login(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']


class User(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user', 'your_photo', 'city', 'street', 'home_number', 'user_number']

    def save(self, commit=True):
        user = super().save(commit)
        user.save()
        return user


class Staff(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'photo', 'work_time', 'phone', 'experience']

    def save(self, commit=True):
        staff = super().save(commit)
        staff.save()
        return staff


class Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text', 'user']

    def save(self, commit=True):
        data = super().save(commit)
        data.save()
        return data


class Problem(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['problem_text', 'user_email']

    def save(self, commit=True):
        data = super().save(commit)
        data.save()
        return data