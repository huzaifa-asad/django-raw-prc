from django.contrib import admin
from school.models import Account

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'teacher_name',
                    'email', 'password']