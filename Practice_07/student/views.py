from django.shortcuts import render
from student.forms import Registration

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
    else:
        form = Registration()
    return render(req, 'student/register.html', {'form': form})
