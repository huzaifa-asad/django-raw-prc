from django.urls import path, register_converter
from student.views import home, profile
from student.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', home, name='home'),
    # path('profile/<my_id>/', profile, name='profile'),
    # path('profile/<int:my_id>/', profile, name='profile'),
    # path('profile/<str:my_id>/', profile, name='profile'),
    # path('profile/<slug:my_id>/', profile, name='profile'),
    # path('profile/<uuid:my_id>/', profile, name='profile'),
    # path('profile/<path:my_id>/', profile, name='profile'),
    
    # to select multiple types
    # path('profile/<str:my_class>/<int:my_id>/', profile, name='profile'),
    
    # created custom converter
    path('profile/<yyyy:year>', profile, name='profile'),
]
