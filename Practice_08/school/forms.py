from django import forms
from school.models import Account

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['student_name', 'email', 'password']
        
# Inherit Student form
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name', 'email', 'password']