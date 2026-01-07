from django.shortcuts import render
from django.views import View
from core.models import Student

class AllStudentView(View):
    def get(self, request):
        all_students = Student.objects.all()
        return render(request, 'core/all_student.html', {'all_students': all_students})