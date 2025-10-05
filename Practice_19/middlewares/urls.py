from django.urls import path
from middlewares import views

urlpatterns = [
    path('home/', views.home),
    path('math/', views.my_math),
    path('user/', views.user_info),
]
