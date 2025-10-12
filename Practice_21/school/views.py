from django.shortcuts import render
from school.models import Student

# Create your views here.
def home(request):
    student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.get(name="huzaifazz")
    
    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').first()
    
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.latest('pass_date', 'id')
    # student_data = Student.objects.earliest('pass_date')
    
    # student_data = Student.objects.all()
    # print(student_data.exists())
    # one_data = Student.objects.get(pk=2)
    # print(student_data.filter(pk=one_data.pk).exists())
    
    # student_data = Student.objects.create(name='khan', roll=111, city='shewa',
    #                                       marks=2232, pass_date='2020-5-2')
    
    # student_data, created = Student.objects.get_or_create(name='farasha', roll=115, city='shewa',
    #                                       marks=3212, pass_date='2021-6-2')
    # print(created)
    
    # student_data = Student.objects.filter(id=4).update(name='Huzaifa Asad', marks=2211)
    # student_data = Student.objects.filter(id=5).update_or_create(name='Asad', marks=2211, roll=44, city='lahore', pass_date='2021-6-2')   
    
    # student_data = Student.objects.get(pk=6).delete()
    # student_data = Student.objects.filter(marks=2100).delete()
    # student_data = Student.objects.all().delete()
    
    print(Student.objects.all().count())
    
    print('Return: ', student_data)
    return render(request, 'school/home.html', {'student': student_data})
