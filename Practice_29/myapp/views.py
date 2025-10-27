from django.shortcuts import render

def home(request):
    # context = {'cart_items': 2}
    return render(request, 'myapp/home.html')

def product(request):
    # context = {'cart_items': 4}
    return render(request, 'myapp/product.html')

def contact(request):
    # context = {'cart_items': 6}
    return render(request, 'myapp/contact.html')

