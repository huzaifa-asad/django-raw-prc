from django.shortcuts import render
from django.contrib import messages
from student.forms import UserForm
# Create your views here.

def home(request):
    # messages.add_message(request, messages.SUCCESS, 'Welcome to Home Page')
    # messages.add_message(request, messages.INFO, 'This is Info Message')
    # messages.add_message(request, messages.WARNING, 'This is Warning Message')
    # messages.add_message(request, messages.ERROR, 'This is Error Message')
    
    
    # In Other way
    messages.success(request, 'Welcome to Home Page')
    messages.info(request, 'This is Info Message')
    messages.warning(request, 'This is Warning Message')
    messages.error(request, 'This is Error Message')
    
    return render(request, 'student/home.html')


def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Registration Successfull..!')
        else:
            messages.error(request, 'Registration Failed!')
    else:
        form = UserForm()
    return render(request, 'student/registaration.html', {'form': form})