from django.shortcuts import render
from student2.forms import DemoForm

def demo_form(req):
    form = DemoForm()
    return render(req, 'student2/demoform.html', {'form': form})
