from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['age'].widget.attrs.update({'class':'form-control',})
            self.fields['rate'].widget.attrs.update({'class':'form-control',})       
            self.fields['description'].widget.attrs.update({'class':"form-control"})

    class Meta:
        model = Profile 
        fields = '__all__'
        exclude = ['user']