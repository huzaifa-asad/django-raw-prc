from django.shortcuts import render
from school.models import Student
from django.db.models import Q

# Create your views here.
def home(request):
    # student_data = Student.objects.filter(Q(id=2) & Q(roll=112))
    # student_data = Student.objects.filter(Q(id=2) | Q(roll=113))
    
    # use ~ for NOT 
    # student_data = Student.objects.filter(~Q(id=2))
    
    # student_data = Student.objects.filter(Q(city='karachi'))
    
    student_data = Student.objects.filter(Q(city='Swabi') & Q(marks__gte=98))

    
    context = {
        'students': student_data
    }
    # print('Return: ', student_data)
    return render(request, 'school/home.html', context)
