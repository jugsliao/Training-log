from django import forms
from .models import Log, Goal
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth import login, authenticate

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type = 'date'

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_description', 'goal_daily', 'goal_date']
        widgets = {
            "goal_date": DateInput,
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':"form-control", 'aria-describedby':"emailHelp", 'placeholder':"Enter email"})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class':'form-control',})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class':'form-control',})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'class':'form-control',})
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 
        ]