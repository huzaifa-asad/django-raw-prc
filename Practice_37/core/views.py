from django.shortcuts import render, HttpResponse


def myfunview1(request):
    return HttpResponse("Hello Function based View")

def myfunview2(request):
    return HttpResponse("<h1>Function Based View</h1>")

def homefunview(request):
    return render(request, "core/home.html")

def aboutfunview(request):
    context = {'msg': 'Welcome to GeekyShows Function Based View'}
    return render(request, 'core/about.html', context)
