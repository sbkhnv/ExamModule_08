from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm


class ThankView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'thankyou.html')


class UserLoginView(View):
    def get(self, request):
        form = Login()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("index")
        else:

            context = {
                "form": login_form,
            }
            return render(request, "login.html", context)


class UserRegisterView(View):
    def get(self, request):
        form = Register()
        context = {'form': form}
        return render(request, 'register.html', context)


    def post(self, request):
        create_form = Register(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')

        else:
            context = {'form': create_form}
            return render(request, 'register.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class MyProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        # form = UserRegisterForm(instance=user)
        return render(request, 'my-profile.html', {'user': user})


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = Register(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Register(instance=request.user)
    return render(request, 'edit-profile.html', {'form': form})


@login_required(login_url='login')
def profile_delete(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect('login')


class UserInfoView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if pk:
            user = User.objects.get(id=pk)
            form = User(instance=user)
            return render(request, 'user-detail.html', {'form': form, 'user': user})
        else:
            users = User.objects.all()
            return render(request, 'users.html', {'users': users})

    def post(self, request, pk=None):
        user = None
        if pk:
            user = User.objects.get(id=pk)
            form = User(request.POST, instance=user)
        elif user is None:
            form = User(request.POST)
        else:
            return redirect('users')

        if form.is_valid():
            form.save()
            return redirect('users')

        if pk:
            return render(request, 'user-detail.html', {'form': form, 'user': user})
        else:
            return render(request, 'users.html', {'form': form})

@login_required(login_url='login')
def user_delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('users')


class AddUser(LoginRequiredMixin, View):
    def get(self, request):
        form = User()
        return render(request, 'add-user.html', context={'form': form})

    def post(self, request):
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            return render(request, 'add-user.html', status=status.HTTP_400_BAD_REQUEST)


class StaffView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if pk:
            staff = Staff.objects.get(id=pk)
            form = Staff(instance=staff)
            return render(request, 'staff-detail.html', {'form': form, 'staff': staff})
        else:
            staffs = Staff.objects.all()
            blogs = Blog.objects.all()
            return render(request, 'about.html', {'staffs': staffs, 'blogs': blogs})

    def post(self, request, pk=None):
        staff = None
        if pk:
            staff = Staff.objects.get(id=pk)
            form = Staff(request.POST, instance=staff)
        elif staff is None:
            form = Staff(request.POST)
        else:
            return redirect('staffs')

        if form.is_valid():
            form.save()
            return redirect('staffs')

        if pk:
            return render(request, 'staff-detail.html', {'form': form, 'user': staff})
        else:
            return render(request, 'about.html', {'form': form})

@login_required(login_url='login')
def staff_delete(request, pk):
    staff = Staff.objects.get(id=pk)
    staff.delete()
    return redirect('staffs')


class AddStaff(LoginRequiredMixin, View):
    def get(self, request):
        form = Staff()
        return render(request, 'add-staff.html', context={'form': form})

    def post(self, request):
        form = Staff(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffs')
        else:
            return render(request, 'add-staff.html', status=status.HTTP_400_BAD_REQUEST)


class BlogView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if pk:
            blog = Blog.objects.get(id=pk)
            form = Blog(instance=blog)
            return render(request, 'blog-detail.html', {'form': form, 'blog': blog})
        else:
            blogs = Blog.objects.all()
            return render(request, 'blog.html', {'blogs': blogs})

    def post(self, request, pk=None):
        blog = None
        if pk:
            blog = Blog.objects.get(id=pk)
            form = Blog(request.POST, instance=blog)
        elif blog is None:
            form = Blog(request.POST)
        else:
            return redirect('blogs')

        if form.is_valid():
            form.save()
            return redirect('blogs')

        if pk:
            return render(request, 'blog-detail.html', {'form': form, 'blog': blog})
        else:
            return render(request, 'blog.html', {'form': form})

@login_required(login_url='login')
def blog_delete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('blogs')


class AddBlog(LoginRequiredMixin, View):
    def get(self, request):
        form = Blog()
        return render(request, 'add-blog.html', context={'form': form})

    def post(self, request):
        form = Blog(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
        else:
            return render(request, 'add-blog.html', status=status.HTTP_400_BAD_REQUEST)



class ProblemView(LoginRequiredMixin, View):
    def get(self, request, pk=None):
        if pk:
            problem = Problem.objects.get(id=pk)
            form = Problem(instance=problem)
            return render(request, 'problem-detail.html', {'form': form, 'problem': problem})
        else:
            problems = Problem.objects.all()
            return render(request, 'problems.html', {'problems': problems})

    def post(self, request, pk=None):
        problem = None
        if pk:
            problem = Problem.objects.get(id=pk)
            form = Problem(request.POST, instance=problem)
        elif problem is None:
            form = Problem(request.POST)
        else:
            return redirect('problems')

        if form.is_valid():
            form.save()
            return redirect('problems')

        if pk:
            return render(request, 'problem-detail.html', {'form': form, 'problem': problem})
        else:
            return render(request, 'problems.html', {'form': form})

@login_required(login_url='login')
def problem_delete(request, pk):
    problem = Problem.objects.get(id=pk)
    problem.delete()
    return redirect('problems')


class AddProblem(LoginRequiredMixin, View):
    def get(self, request):
        form = Problem()
        return render(request, 'contact.html', context={'form': form})

    def post(self, request):
        form = Problem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            return render(request, 'contact.html', status=status.HTTP_400_BAD_REQUEST)

