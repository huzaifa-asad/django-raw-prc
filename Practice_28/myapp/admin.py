from django.contrib import admin
from .models import Post, Page, Song

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['pname', 'pcat', 'ppublished', 'user']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'ptcat', 'ptpublished', 'user']
    
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['sname', 'sduration', 'written_by']