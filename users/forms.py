from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # age = forms.IntegerField()
    # sex = forms.ChoiceField(choices=(('male', 'Male'), ('female','Female ')))
    # description = forms.CharField(widget=forms.Textarea)
    # rate = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':"form-control", 'aria-describedby':"emailHelp", 'placeholder':"Enter email"})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class':'form-control',})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class':'form-control',})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'class':'form-control',})
    #     self.fields['age'].widget.attrs.update({'class':'form-control',})
    #     self.fields['sex'].widget.attrs.update({'class':"form-control"})
    #     self.fields['rate'].widget.attrs.update({'class':'form-control',})       
    #     self.fields['description'].widget.attrs.update({'class':"form-control"})
        

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 
        # 'age', 'sex',
        # 'rate', 'description'
        ]