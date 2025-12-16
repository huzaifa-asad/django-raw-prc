from django.urls import path
from django.views.generic.base import TemplateView
from core import views

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='core/home.html')),
    
    path('about/', views.AboutTemplateView.as_view()),
    path('contact/', views.ContactTemplateView.as_view()),
    path('profile/<int:id>', views.ProfileTemplateView.as_view())
]
