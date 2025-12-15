from django.shortcuts import render, HttpResponse
from django.views import View

def myfunview1(request):
    return HttpResponse("Hello Function based View")

class MyClassView1(View):
    def get(self, request):
        return HttpResponse("Hello Class Based View")

def myfunview2(request):
    return HttpResponse("<h1>Function Based View</h1>")

class MyClassView2(View):
    def get(self, request):
        return HttpResponse("<h1>Function Based View</h1>")

def homefunview(request):
    return render(request, "core/home.html")

class MyClassView3(View):
    name = 'Huzaifa'
    def get(self, request):
        return render(request, "core/home.html", {'name': self.name})

def aboutfunview(request):
    context = {'msg': 'Welcome to GeekyShows Function Based View'}
    return render(request, 'core/about.html', context)

class AboutClassView(View):
    template_name = ''
    def get(self, request):
        context = {'msg': 'Welcome to Huzaifa Asad github Profile'}
        return render(request, self.template_name, context)


def newsfunview(request, template_name):
    template_name = template_name
    context = {'info': 'Subscribe to our Channel'}
    return render(request, template_name, context)

# def contactfunview(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             return HttpResponse('Thanks Form Submitted!')
#         else:
#             form = ContactForm()
#         return render(request, 'core/contact.html', {'form': form})
    
   
    