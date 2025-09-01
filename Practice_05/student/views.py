from django.shortcuts import render
from student.models import Profile


def all_data(req):
    all_students = Profile.objects.all()
    print(all_students)
    return render(req, 'student/all.html', {'students': all_students})
