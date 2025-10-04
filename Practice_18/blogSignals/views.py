from django.shortcuts import HttpResponse
from blogSignals import signals
# Create your views here.

def home(request):
    a = 10/0
    return HttpResponse('Hello')

def custom_signal(request):
    signals.notification.send(sender=None, request=request, user=["Huzaifa", "Asad"])
    return HttpResponse('This is Custom Signal')