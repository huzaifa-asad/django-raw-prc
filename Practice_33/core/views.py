from django.shortcuts import render
from asgiref.sync import sync_to_async, async_to_sync
from core.models import Student
from django.http import JsonResponse

## Syncronous function
def my_sync_function(x):
    return x * 2

async def my_async_function():
    result = await sync_to_async(my_sync_function)(5)
    print(result)
       
## Asynchronous function
async def my_async_function2(x):
    return x * 2

def my_sync_function():
    result = async_to_sync(my_async_function2)(5)
    print(result)
    
def get_student_data():
    return list(Student.objects.filter(age__gte=20).values())

async def student_data(request):
    student_data = await sync_to_async(get_student_data)()
    return JsonResponse({'data': student_data})