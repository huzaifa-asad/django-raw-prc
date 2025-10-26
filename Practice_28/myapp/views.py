from django.shortcuts import render
from myapp.models import Post, Page, Song
from django.contrib.auth.models import User

def home(request):
    return render(request, 'myapp/home.html')

def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email="huzaifa@gmail.com")
    data3 = User.objects.filter(page__pcat='restapi')
    data4 = User.objects.filter(song__sduration=3)
    return render(request, 'myapp/user.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4})

def show_page_data(request):
    return render(request, 'myapp/page.html')

def show_post_data(request):
    data1 = Post.objects.all()
    return render(request, 'myapp/post.html', {'data1': data1})

def show_song_data(request):
    return render(request, 'myapp/song.html')