from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def setsession(request):
    request.session['fname'] = 'huzaifa'
    request.session['lname'] = 'asad'
    # request.session.set_expiry(10)  # in seconds
    # request.session.set_expiry(0)  # session expire in browser close
    return render(request, 'student/setsession.html')

def getsession(request):
    # first_name = request.session['fname']
    first_name = request.session.get('fname', 'No')
    last_name = request.session.get('lname', 'User')
    return render(request, 'student/getsession.html', {'first_name': first_name,
                                                    'last_name': last_name})

def delsession(request):
    if 'fname' and 'lname' in request.session:
        del request.session['fname']
        del request.session['lname']
    return render(request, 'student/delsession.html')

def flushsession(request):
    request.session.flush()
    return render(request, 'student/flushsession.html')

def sessionmethodsinview(request):
    keys = request.session.keys()
    print(keys)
    # to show key and value both
    items = request.session.items()
    print(items)
    
    session_cookie_age = request.session.get_session_cookie_age()
    print("session cookie age: ", session_cookie_age)
    
    expire_age = request.session.get_expiry_age()
    print("Expire age: ", expire_age)
    
    expire_date = request.session.get_expiry_date()
    print("Expire age: ", expire_date)
    
    expire_at_browser_close = request.session.get_expire_at_browser_close()
    print("Expire age: ", expire_at_browser_close)
    return render(request, 'student/sessionmethodsinview.html')

def sessionmethodsintemplate(request):
    keys = request.session.keys()
    # to show key and value both
    items = request.session.items()
    return render(request, 'student/sessionmethodsintemplate.html', {'keys': keys, 'items': items})

def sessionclear(request):
    request.session.clear_expired()
    return render(request, 'student/sessionclear.html')

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')