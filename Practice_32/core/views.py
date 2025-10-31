from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('Hello Home Page')


async def home(request):
    return HttpResponse('Hello Home Page')
