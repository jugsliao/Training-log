from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

# Create your views here.

def registration(request):
    if request.method == 'POST':
        r_form = RegisterForm(request.POST)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if r_form.is_valid():
            r_form.save()
            p_form.save()
            username = r_form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')
    else:
        r_form = RegisterForm()
        p_form = ProfileUpdateForm()

    context = {
        'r_form': r_form,
        'p_form': p_form
    }

    return render(request, 'users/register.html', context)

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('first_app/home')


def logout_view(request):
    logout(request)
    return redirect('first_app/home')

def login_error(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login_error.html')

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if  form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'form': form
#     }

#     return render(request, 'users/profile.html', context)
