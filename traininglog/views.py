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

# def question(request, question_id):
#     '''show a single question with its topic and explaination'''
#     question = Log.objects.get(id=question_id)
#     answer = question.answer_set.order_by('-date_added') 
#     context = {'question': question, 'answer': answer}
#     return render(request, 'first_app/question.html', context)

# @login_required
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
            return HttpResponseRedirect(reverse('traininglog:home'))

    context = {'form': form}
    return render(request, 'traininglog/newlog.html', context)

# class LogsView(generic.ListView):
#     template_name = 'first_app/questionhub.html'
#     context_object_name = 'questions'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Log1.objects.order_by('-date_added')

