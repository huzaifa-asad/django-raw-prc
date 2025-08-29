from django.shortcuts import render
# Create your views here.

def learn_django(req):
    name = "Django"
    duration = "6 months"
    seats = 50
    
    course_details = {"nm": name, "du": duration, "st": seats}
    return render(req, 'course/django.html', course_details)

def learn_fastapi(req):
    student = {"names": ["huzaifa", "talha", "hamza", "ayal", "haram"]}
    return render(req, 'course/fastapi.html', context=student)