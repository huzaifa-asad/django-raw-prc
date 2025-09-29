from django.shortcuts import render
from django.core.cache import cache

def course(req):
    # mv = cache.get('movie', 'has_expired')
    # if mv == 'has_expired':
    #     cache.set('movie', 'Silicon',  60)
    #     mv = cache.get('movie')
    
    # OR
    
    mv = cache.get_or_set('movie', 'The Harry', 15)
    mv1 = cache.get_or_set('movie', 'The Harry', 25, version=2)
    print(mv1)   
    return render(req, 'student/courses.html', {'mv': mv})


# To show some data for some specified time
# def course(req):
#     data = {'name': 'Huzaifa Asad', 'roll': 103}
#     cache.set_many(data, 30)
#     stu = cache.get_many(data)
#     return render(req, 'student/courses.html', {'stu': stu})

# to remove specific cache
# def course(req):
#     cache.delete('movie', version=2)
#     return render(req, 'student/courses.html')