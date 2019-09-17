from django.shortcuts import render,redirect
from testapp.models import BasicInfo,Opprtunity
from testapp.forms import BasicInfoForm,OpprtunityForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from testapp.forms import UserForm

def home_view(request):
    return render(request,'testapp/home.html')


def signup_view(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm()
        if form.is_valid():
            user=form.save()
            user.set_password(user.set_password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
def logout_view(request):
    return render(request,'testapp/logout.html')

def career_view(request):
    opp=Opprtunity.objects.all()
    return render(request,'testapp/career.html',{'opp':opp})
@login_required
def apply_view(request):
    form=BasicInfoForm()
    if request.method=='POST':
        form=BasicInfoForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/apply.html',{'form':form})
def submit_view(request):
    return render(request,'testapp/submit.html')
