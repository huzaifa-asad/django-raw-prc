from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def setsession(request):
    return render(request, 'student/setsession.html')

def getsession(request):
    return render(request, 'student/getsession.html')

def delsession(request):
    return render(request, 'student/delsession.html')

def flushsession(request):
    return render(request, 'student/flushsession.html')

def sessionmethodsinview(request):
    return render(request, 'student/ssessionmethodsinview.html')

def sessionmethodsintemplate(request):
    return render(request, 'student/sessionmethodsintemplate.html')

def sessionclear(request):
    return render(request, 'student/sessionclear.html')

def settestcookie(request):
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    return render(request, 'student/deltestcookie.html')