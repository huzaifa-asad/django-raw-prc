from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    all_post = Post.objects.all().order_by('publish_date')
    paginator = Paginator(all_post, per_page=3, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # print('Page Number ', page_number)
    # print('Page Obj ', page_obj)
    return render(request, 'core/home.html', {'page_obj': page_obj})