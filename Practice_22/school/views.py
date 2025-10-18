from django.shortcuts import render
from school.models import Student
from datetime import date, time

# Create your views here.
def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(name="Talha")
    # student_data = Student.objects.filter(name__exact="Talha")
    
    # if not case sensitive use i means insensitive
    # student_data = Student.objects.filter(name__iexact="Talha")
    # student_data = Student.objects.filter(name__contains="a")
    # student_data = Student.objects.filter(name__icontains="S")
    
    # student_data = Student.objects.filter(id__in=[1, 4, 3])
    
    # Greater than
    # student_data = Student.objects.filter(marks__gt=60)
    # Greater than or Equal to
    # student_data = Student.objects.filter(marks__gte=74)
    # Less than 
    # student_data = Student.objects.filter(marks__lt=74)
    # Less than or Equal to
    # student_data = Student.objects.filter(marks__lte=74)
    
    # student_data = Student.objects.filter(name__startswith="h")
    # student_data = Student.objects.filter(name__istartswith="h")
    # student_data = Student.objects.filter(name__endswith="a")
    
    # Range between two dates
    # student_data = Student.objects.filter(pass_date__range=("2024-10-1", "2025-10-12"))
    
    # student_data = Student.objects.filter(admission_date__year=2024)
    student_data = Student.objects.filter(admission_date__time__gt=time(11, 00))
    print('Return: ', student_data)
    return render(request, 'school/home.html', {'students': student_data})
