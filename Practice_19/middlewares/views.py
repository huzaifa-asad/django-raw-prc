from django.shortcuts import render
from django.template.response import TemplateResponse


def home(request):
    print("i am home view")
    return render(request, 'middlewares/home.html')

def my_math(request):
    print("i am my_math view")
    a = 10/2
    return render(request, 'middlewares/math.html', {'a': a})
 
def user_info(request):
    print("i am user_info view")
    context = {'name': 'Huzaifa Asad'}
    return render(request, 'middlewares/user.html', context)
