from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import widgets
from .models import Blog

# ==================== Signup form ====================#

class SignupForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=(forms.PasswordInput(attrs={'class' : 'form-control text-fields'})))
    password2 = forms.CharField(label='Confirm Password', widget=(forms.PasswordInput(attrs={'class' : 'form-control text-fields'})))
    email = forms.EmailField(required=True, widget=(forms.EmailInput(attrs={'class' : 'form-control text-fields'})))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        labels = {
            'username' : 'Username',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control text-fields'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control text-fields'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control text-fields'}),
        }

# ==================== Login form ====================#

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control text-fields'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control text-fields'})
        }

# ==================== Create post form ====================#

class BlogForm(forms.ModelForm):
    author = forms.CharField(disabled=True, widget = (forms.TextInput(attrs={'class' : 'form-control text-fields'})))
    
    # This field below checks whether the user is a superuser or not.
    
    ''' Description : This is a hidden field and in the view section either 'True' or 'False' is
        passed based on a condition whether the requested user is superuser or not. As it is a 
        hidden field, it will not be visible to the user but it will pass a boolean data to the
        db underneath the hood.
    '''
    superuser_status = forms.CharField(disabled=True, widget = (forms.HiddenInput()))

    class Meta:
        model = Blog
        fields = ['title', 'author', 'blog', 'superuser_status']


        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control text-fields'}),
            # 'author' : forms.TextInput(attrs={'class' : 'form-control text-fields'}),
            'blog' : forms.Textarea(attrs={'class' : 'form-control text-fields'})
        }