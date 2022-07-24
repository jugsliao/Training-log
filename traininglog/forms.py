from django import forms
from .models import Log1, Log2
from .models import Workout
from django.contrib.admin import widgets
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# for 6x400m
class LogForm1(forms.ModelForm):
    class Meta:
        model = Log1
        fields = ['time1', 'time2', 'time3', 'time4', 'time5', 'time6']
        labels = {'time': ''}
        
# for 3x800m
class LogForm2(forms.ModelForm):
    class Meta:
        model = Log2
        fields = ['time1', 'time2', 'time3']
        labels = {'time': ''}


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['goal', 'goal_date']
        widgets = {
            "goal_date": AdminDateWidget(),
        }

