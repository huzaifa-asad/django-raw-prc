from django.shortcuts import render
from django.views.generic.base import TemplateView

class AboutTemplateView(TemplateView):
    template_name = 'core/about.html'
    

class ContactTemplateView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Huzaifa'
        context['roll'] = 103
        
        return context
    

class ProfileTemplateView(TemplateView):
    template_name = 'core/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Huzaifa Asad'
        
        return context