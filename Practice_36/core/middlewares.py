from asgiref.sync import iscoroutinefunction, markcoroutinefunction
from django.utils.decorators import sync_and_async_middleware, sync_only_middleware, async_only_middleware

@sync_and_async_middleware
def my_fun_middleware(get_response):
    print("One-time initialization")
    if iscoroutinefunction(get_response):
        async def middleware(request):
            print(f"Before view (Async): {request.path}")
            # Call Next Middleware or Final View
            response = await get_response(request)
            print(f"After view (Async): {request.path}")
            return response
    else:
        def middleware(request):
            print(f"Before view (Sync): {request.path}")
            # Call Next Middleware or Final View
            response = get_response(request)
            print(f"After view (Sync): {request.path}")
            return response
        
    return middleware