from django.shortcuts import HttpResponse, render


def my_fun_middleware(get_response):
    print("One Time Initialization Func based")
    
    def my_func(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_func


# def my_fun_middleware(get_response):
#     print("One Time Initialization")
    
#     def my_func(request):
#         print("This is before view")
#         # response = HttpResponse('this is middleware not view')
#         response = render(request, 'middlewares/uc.html')
#         print("This is after view")
#         return response
#     return my_func


# Class Based Middlewares

class myClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization Class based")
        
    def __call__(self, request):
        print("this is before view")
        response = self.get_response(request)
        print("this is after view")
        return response