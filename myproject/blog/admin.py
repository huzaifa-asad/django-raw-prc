from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "email", "enrolled_date")
    search_fields = ("name", "email")
    list_filter = ("age", "id")

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "created_at")

admin.site.register(Student, StudentAdmin)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(PostDetail)
admin.site.register(Tag)