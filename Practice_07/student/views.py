from django.shortcuts import render
from student.forms import Registration
from django.http import HttpResponseRedirect

def register(req):
    if req.method == 'POST':
        form = Registration(req.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name:', name)
            print('Email:', email)
            print('Password:', password)
            # to save from resubmission form
            return HttpResponseRedirect('/student/success/')
    else:
        form = Registration()
    return render(req, 'student/register.html', {'form': form})


def reg_success(req):
    return render(req, 'student/success.html')