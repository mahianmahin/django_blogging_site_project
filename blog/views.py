from django import http, shortcuts
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import SignupForm
from .forms import LoginForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import BlogForm
from .models import Blog

# Create your views here.


# ==================== Home view ====================#

def home(request):
    blog = Blog.objects.all()
    return render(request, 'blog/home.html', {'home' : 'active', 'name' : request.user, 'blog' : blog})

# ==================== About view ====================#

def about(request):
    return render(request, 'blog/about.html', {'about' : 'active', 'name' : request.user})

# ==================== Registration view ====================#

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login/')
        else:
            form = SignupForm()
    else:
        return HttpResponseRedirect('/dashboard/')

    return render(request, 'blog/signup.html', {'signup' : 'active', 'form' : form})

# ==================== Login view ====================#

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
    else:
        return HttpResponseRedirect('/dashboard/')
    
    return render(request, 'blog/login.html', {'form' : form, 'login' : 'active'})

# ==================== Logout view ====================#

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("<h3>You are not logged in then why the hell you are trying to log out!!???</h3>")
    

# ==================== Contact view ====================#

def contact(request):
    return render(request, 'blog/contact.html', {'contact' : 'active', 'name' : request.user})


# ==================== Dashboard view ====================#

def dashboard(request):
    if request.user.is_authenticated:
        blog_list = Blog.objects.filter(author = request.user.username)

        return render(request, 'blog/dashboard.html', {'name' : request.user, 'blog_list' : blog_list, 'dashboard' : 'active'})
    else:
        return HttpResponseRedirect('/login/')

# ==================== Create post view ====================#

def create_post(request):
    if request.user.is_superuser:
        status = "True"
    else:
        status = "False"

    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogForm(request.POST, initial={'author' : request.user})
            # Passing a boolean data to this hidden field below for checking superuser access
            form.initial['superuser_status'] = status
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = BlogForm(initial={'author' : request.user.username})
            form.initial['superuser_status'] = status

        return render(request, 'blog/create_post.html', {'name' : request.user, 'form' : form})

    else:
        return HttpResponseRedirect('/login/')

# ==================== Delete post view ====================#

############ Only a superuser can delete his/her own posts from this view func ############

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blog.objects.get(pk=id)
            pi.delete()
            # print (pi)
            # return redirect('/dashboard/')
        # return render(request, 'blog/dashboard.html')
    else:
        return HttpResponseRedirect('/login/')

# ==================== Edit post view ====================#

def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blog.objects.get(pk = id)
            form = BlogForm(request.POST, instance = pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        
        else:
            pi = Blog.objects.get(pk=id)
            form = BlogForm(instance=pi)

        return render(request, 'blog/edit_post.html', {'name' : request.user.username, 'form' : form})
    
    else:
        return HttpResponseRedirect('/login/')