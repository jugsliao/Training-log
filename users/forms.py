from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

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
