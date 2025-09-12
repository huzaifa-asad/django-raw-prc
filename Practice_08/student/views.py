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
            
            # Save data into database
            data = Profile(name=nm, email=em, password=pw)
            data.save()
            
            # to save from resubmission form
            return HttpResponseRedirect('/student/register/')
    else:
        form = Registration()
    return render(req, 'student/register.html', {'form': form})
