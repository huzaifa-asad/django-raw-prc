from django.shortcuts import render


def home(request):
    return render(request, 'student/home.html')

# def profile(request, my_id):
#     studnet = {'id': my_id}
#     return render(request, 'student/profile.html', studnet)

# def profile(request, my_class, my_id):
#     studnet = {'class': my_class, 'id': my_id}
#     return render(request, 'student/profile.html', studnet)


def profile(request, year):
    studnet = {'year': year}
    return render(request, 'student/profile.html', studnet)
