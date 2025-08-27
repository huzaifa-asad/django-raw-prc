from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.

# Functions based Views(FBV)
def home(request):
    return HttpResponse("Welcome to my Blog!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


# Class-Based Views(CBV)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"