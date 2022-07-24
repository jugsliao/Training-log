from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LogForm1, LogForm2
from .models import Log1, Log2, User, Workout
from .forms import WorkoutForm

# Create your views here.
def home(request):
    '''render the home page'''
    '''
    training pace = weeks left * 4seconds + target training pace
    
    '''
    # Get recent workouts for logged in user:
    workouts = Workout.objects.filter(user__id=request.user.id)

    # Gather any page data:
    data = {
        'workouts': workouts
    }

    # Load dashboard with data:
    return render(request, 'traininglog/home.html', data)

def chooselog(request):
    return render(request, 'traininglog/chooselog.html')

@login_required
def newlog1(request):
    '''adding a new question'''
    if request.method != 'POST':
        #if no data is submitted, create a blank for
        form = LogForm1()
    else:
        # POST data is submitted; process date_added
        form = LogForm1(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("traininglog:home"))

    context = {'form': form}
    return render(request, 'traininglog/newlog1.html', context)

# @login_required
# def newlog2(request):
#     '''adding a new question'''
#     if request.method != 'POST':
#         #if no data is submitted, create a blank for
#         form = LogForm2()
#     else:
#         # POST data is submitted; process date_added
#         form = LogForm2(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("traininglog:home"))

#     context = {'form': form}
#     return render(request, 'traininglog/newlog2.html', context)

# @login_required
# def newlog3(request):
#     '''adding a new question'''
#     if request.method != 'POST':
#         #if no data is submitted, create a blank for
#         form = LogForm1()
#     else:
#         # POST data is submitted; process date_added
#         form = LogForm1(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("traininglog:home"))

#     context = {'form': form}
#     return render(request, 'traininglog/newlog.html', context)

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
        return Log1.objects.order_by('-pub_date') 

def log(request, log_id):
    '''show the log on that date'''
    log = Log1.objects.get(id=log_id)
    context = {'log': log}
    return render(request, 'traininglog/log.html', context)

@login_required
def new_workout(request):
    if request.method == 'POST':
        # form = ProfileUpdateForm(request.POST,
        #                            request.FILES,
        #                            instance=request.user.profile)
        form = WorkoutForm(data=request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return HttpResponseRedirect(reverse("traininglog:home"))

    else:
        form = WorkoutForm()

    context = {
        'form': form
    }

    return render(request, 'traininlog/new_workout.html', context)

   