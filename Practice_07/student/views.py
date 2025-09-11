from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect
from student.models import Profile

def register(req):
    if req.method == 'POST':
        form = Registration(req.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            nm = form.cleaned_data['name']
            em= form.cleaned_data['email']
            pw = form.cleaned_data['password']
            print('Name:', nm)
            print('Email:', em)
            print('Password:', pw)
            
            # Save Data into Database
            user = Profile(name = nm, email=em, password=pw)
            user.save()
            
            # Update Data into Database
            # user = Profile(id=1, name=nm, email=em, password=pw)
            # user.save()
            
            # to save from resubmission form
            return HttpResponseRedirect('/student/success/')
    else:
        form = Registration()
    return render(req, 'student/register.html', {'form': form})


def reg_success(req):
    return render(req, 'student/success.html')