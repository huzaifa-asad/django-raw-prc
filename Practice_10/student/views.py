from django.shortcuts import render, redirect
from student.forms import ProfileForm
from student.models import Profile


def home(request):
    candidates = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'student/home.html', {'form': form, 'candidates': candidates})


def candidate_detail(request, id):
    candidate = Profile.objects.get(id=id)
    return render(request, 'student/candidates.html', {'candidate': candidate})