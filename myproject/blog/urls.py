from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path("post-list/", views.PostListView.as_view(), name="post_list_cbv"),
]
