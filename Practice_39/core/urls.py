from django.urls import path
from core import views

urlpatterns = [
    path('', views.AllStudentView.as_view(), name='all_student'),
]
