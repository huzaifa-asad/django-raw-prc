from django.shortcuts import render
from datetime import timedelta, datetime, timezone

# Create your views here.

def setcookie(request):
    response = render(request, 'student/set_cookie.html')
    # response.set_cookie('pay_id', 'ppp123', max_age=3600)
    response.set_cookie('pay_id', 'ppp123', expires=datetime.now(timezone.utc) + timedelta(days=3))
    return response


def getcookie(request):
    # pay_id = request.COOKIES['pay_id']
    pay_id = request.COOKIES.get('pay_id')   # For default value
    return render(request, 'student/get_cookie.html', {'pay_id': pay_id})


def delcookie(request):
    response = render(request, 'student/delete_cookie.html')
    response.delete_cookie('pay_id')
    return response

def setsignedcookie(request):
    response = render(request, 'student/set_signed_cookie.html')
    response.set_signed_cookie('token', 't443322', salt='tk')
    return response


def getsignedcookie(request):
    token = request.get_signed_cookie('token', default='guest_token123', salt='tk')
    return render(request, 'student/get_signed_cookie.html', {'token': token})