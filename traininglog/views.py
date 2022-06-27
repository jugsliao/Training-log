from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import LogForm1
from .models import Log1

# Create your views here.
def home(request):
    '''render the home page'''
    return render(request, 'traininglog/home.html')

@login_required
def newlog(request):
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
    return render(request, 'traininglog/newlog.html', context)

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
        return HttpResponseRedirect(reverse('traininglog:log', args=[log.id]))

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

