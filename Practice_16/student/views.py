from django.shortcuts import render
from django.views.decorators.cache import cache_page

def home(req):
    return render(req, 'student/home.html')

@cache_page(15)  # for 15 seconds
def course(req):
    return render(req, 'student/course.html')

def result(req):
    return render(req, 'student/result.html')