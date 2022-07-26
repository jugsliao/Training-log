from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.conf import settings

from .forms import LogForm, GoalForm
from .models import Log, Goal

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'traininglog/register.html', context)

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
        return render(request, 'login_error.html')

# # Create your views here.
def home(request):
    '''render the home page'''
    '''
    training pace = weeks left * 4seconds + target training pace
    
    '''
    # goal = Goal.objects.filter(user=request.user)

    data = {
        # 'goal': goal
    }

    return render(request, 'traininglog/home.html', data)

class newlogView(LoginRequiredMixin, generic.CreateView):
    model = Log
    fields = ['title', 'description']
    template_name = 'traininglog/newlog.html'
    
    def get_success_url(self):
        return reverse('traininglog:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def editlog(request, log_id):
    '''editing an answer'''
    log = Log.objects.get(id=log_id)

    if request.method != 'POST':
        #when first start editing, pre-fill form with the current answer
        form = LogForm(instance=log)
    else:
        #POST data submitted, proccesing date_added
        form = LogForm(instance=log, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('traininglog:log', args=[log.id]))

    context = {'log': log, 'form': form}
    return render(request, 'traininglog/editlog.html', context)

@login_required
def deletelog(request, log_id):
    '''deleting an answer'''
    log = Log.objects.get(id=log_id)

    if request.method == 'POST':
        log.delete()
        return HttpResponseRedirect(reverse('traininglog:logs'))

    context = {'log':log}
    return render(request, 'traininglog/deletelog.html', context)

class LogsView(generic.ListView):
    template_name = 'traininglog/logs.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return Log.objects.filter(user=self.request.user).order_by('-pub_date') 

def log(request, log_id):
    '''show the log on that date'''
    log = Log.objects.get(id=log_id)
    context = {'log': log}
    return render(request, 'traininglog/log.html', context)

@login_required
def newgoal(request):
    if request.method != 'POST':
        form = GoalForm()
    else:
        form = GoalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("traininglog:home"))

    context = {'form': form}

    return render(request, 'traininglog/newgoal.html', context)

class newGoalView(LoginRequiredMixin, generic.CreateView):
    model = Goal
    fields = ['goal_description', 'goal_daily', 'goal_date']
    template_name = 'traininglog/newgoal.html'
    
    def get_success_url(self):
        return reverse('traininglog:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalsView(generic.ListView):
    template_name = 'traininglog/goals.html'
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

def goal(request, goal_id):
    '''show the log on that date'''
    goal = Goal.objects.get(id=goal_id)
    context = {'goal': goal}
    return render(request, 'traininglog/goal.html', context)

   