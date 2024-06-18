from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    your_photo = models.ImageField(upload_to='user/')
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    home_number = models.CharField(max_length=50)
    user_number = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_info'
        ordering = ['id']
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.user.first_name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='staff/')
    work_time = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    experience = models.TextField()

    class Meta:
        db_table = 'staff_info'
        ordering = ['id']
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.user.last_name

class Blog(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'
        ordering = ['id']
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.user.first_name


class Problem(models.Model):
    problem_text = models.TextField()
    user_email = models.EmailField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'problems'
        ordering = ['id']
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.user_email