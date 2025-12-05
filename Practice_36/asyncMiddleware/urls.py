from django.contrib import admin
from django.urls import path
from core.views import async_view, sync_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('async_view/', async_view, name='async_view'),
    path('sync_view/', sync_view, name='sync_view'),
]
