from django import forms
from testapp.models import BasicInfo,Opprtunity
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

class OpprtunityForm(forms.ModelForm):
    class Meta:
        model=Opprtunity
        fields='__all__'
class BasicInfoForm(forms.ModelForm):
    class Meta:
        model=BasicInfo
        fields='__all__'
