from django import forms
from .models import Log1

# for 6x400m
class LogForm1(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)      
#             self.fields['time1'].widget.attrs.update({'class':"form-control"})
#             self.fields['time2'].widget.attrs.update({'class':"form-control"})
#             self.fields['time3'].widget.attrs.update({'class':"form-control"})
#             self.fields['time4'].widget.attrs.update({'class':"form-control"})
#             self.fields['time5'].widget.attrs.update({'class':"form-control"})
#             self.fields['time6'].widget.attrs.update({'class':"form-control"})
    class Meta:
        model = Log1
        fields = ['time1', 'time2', 'time3', 'time4', 'time5', 'time6']
        labels = {'time': ''}
        # exclude = ['user', 'pub_date']

