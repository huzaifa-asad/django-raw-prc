from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView

# Create your views here.
class PostView(View):
    def get(self, request):
        all_post = Post.objects.all().order_by('id')
        paginator = Paginator(all_post, per_page=3 )
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'core/paginator.html', {'page_obj': page_obj})
    

class PostListView(ListView):
    model = Post
    template_name = 'core/posts.html'
    ordering=['id']
    paginate_orphans=2
    paginate_by=3