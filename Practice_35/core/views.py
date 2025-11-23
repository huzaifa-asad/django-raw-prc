from django.shortcuts import render
from core.models import Student

def home(request):
    students = Student.objects.all()
    for student in students:
        print(f"name: {student.name} age: {student.age} email: {student.email}")
    return render(request, "core/home.html")