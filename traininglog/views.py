from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import LogForm1, LogForm2, GoalForm
from .models import Log1, Log2, User, Goal

# Create your views here.
def home(request):
    '''render the home page'''
    '''
    training pace = weeks left * 4seconds + target training pace
    
    '''
    # Get recent workouts for logged in user:
    goal = Goal.objects.filter(user=request.user)

    # Gather any page data:
    data = {
        'goal': goal
    }

    # Load dashboard with data:
    return render(request, 'traininglog/home.html', data)

def chooselog(request):
    return render(request, 'traininglog/chooselog.html')

class newlog1View(LoginRequiredMixin, generic.CreateView):
    model = Log1
    fields = ['time1', 'time2', 'time3', 'time4', 'time5', 'time6']
    template_name = 'traininglog/newlog1.html'
    
    def get_success_url(self):
        return reverse('traininglog:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def editlog(request, log_id):
    '''editing an answer'''
    log = Log1.objects.get(id=log_id)

    if request.method != 'POST':
        #when first start editing, pre-fill form with the current answer
        form = LogForm1(instance=log)
    else:
        #POST data submitted, proccesing date_added
        form = LogForm1(instance=log, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('traininglog:log', args=[log.id]))

    context = {'log': log, 'form': form}
    return render(request, 'traininglog/editlog.html', context)

@login_required
def deletelog(request, log_id):
    '''deleting an answer'''
    log = Log1.objects.get(id=log_id)

    if request.method == 'POST':
        log.delete()
        return HttpResponseRedirect(reverse('traininglog:logs'))

    context = {'log':log}
    return render(request, 'traininglog/deletelog.html', context)

class LogsView(generic.ListView):
    template_name = 'traininglog/logs.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return Log1.objects.filter(user=self.request.user).order_by('-pub_date') 

def log(request, log_id):
    '''show the log on that date'''
    log = Log1.objects.get(id=log_id)
    context = {'log': log}
    return render(request, 'traininglog/log.html', context)

@login_required
def goal(request):
    if request.method == 'POST':
        form = GoalForm(data=request.POST)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("traininglog:home"))

    else:
        form = GoalForm()

    context = {
        'form': form
    }

    return render(request, 'traininglog/goal.html', context)

class newGoalView(LoginRequiredMixin, generic.CreateView):
    model = Goal
    fields = ['goal_time', 'goal_date']
    template_name = 'traininglog/goal.html'
    
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

   