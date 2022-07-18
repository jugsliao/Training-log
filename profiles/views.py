from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.models import User

from .models import Profile 
from .forms import ProfileForm

# Create your views here.

class ProfilesList(ListView):
     template_name = 'profiles/profiles.html'
     model = Profile 

def myprofile(request):
     return render(request, 'profiles/myprofile.html') 

def createprofile(request):
     if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
     else:
        form = ProfileForm()
     return render(request, 'profiles/createprofile.html', {'form':form})
