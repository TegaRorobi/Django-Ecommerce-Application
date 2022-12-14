from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from main.models import Cart

# Create your views here.
def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        print(response.POST)
        if form.is_valid():
            print('the form is valid and it will be saved')
            form.save()

            created_user = form.instance
            Cart.objects.create(user=created_user)
            return redirect('/login')
        else:
            print('The form is not valid and it will not be saved')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form':form})