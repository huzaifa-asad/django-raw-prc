from django.contrib import admin
from student.models import Profile, Results

# Register your models here.
admin.site.register(Profile)


# Create modelAdmin class for Results
@admin.register(Results) #short form of site register
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_class', 'marks')
# admin.site.register(Results, ResultsAdmin)
