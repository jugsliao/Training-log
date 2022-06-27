from django import forms
from .models import Log1, Log2

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
        fields = ['time1', 'time2', 'time3', 'time4', 'time5', 'time6', 'time7', 'time8']
        labels = {'time': ''}

