from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'data': 'Hey there! I am Huzaifa Django Developer, Welcome to the Student Home Page.'}
    return render(request, 'student/home.html', context)