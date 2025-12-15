from django.urls import path
from core import views

urlpatterns = [
    path('fun1/', views.myfunview1),
    path('fun2/', views.myfunview2),
    path('homefun/', views.homefunview),
    path('aboutfun/', views.aboutfunview),
    # path('newsfun/', views.newsfunview),
    
    # inject tamplate form url
    path('newsfun2/', views.newsfunview, {'template_name': 'core/news2.html'}),
    # path('contactfun/', views.contactfunview),
    
    
    # Class Views Urls
    path('cl1/', views.MyClassView1.as_view()),
    path('cl2/', views.MyClassView2.as_view()),
    path('cl3/', views.MyClassView3.as_view()),
    path('aboutcls/', views.AboutClassView.as_view(template_name="core/about.html")),
]
