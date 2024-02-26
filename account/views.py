from django.shortcuts import render, redirect
from .forms import CustomerCreationForm, CustomerLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def register_account(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomerCreationForm()
    return render(request, 'account/create.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                messages.success(request, 'Successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, "wrong username or password!")
                
    else:
        form = CustomerLoginForm()
    return render(request, 'account/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(reverse('login'))