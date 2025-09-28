from django.urls import path
from student import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.home, name="course"),
    path('home/', cache_page(30)(views.home), name="course"),
    path('index/', views.home, name="course"),
    path('course/', views.course, name="home"),
    path('result/', cache_page(30)(views.result), name="result"),
]
