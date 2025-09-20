from django.contrib import admin
from student.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    search_fields = ('name', 'email')
    list_filter = ('id', 'name')