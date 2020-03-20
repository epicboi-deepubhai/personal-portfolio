from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blog_no = Blog.objects.count
    blogs = Blog.objects.order_by('-upload_date')[:6]
    return render(request, 'blog/blog_home.html', {'blogs': blogs, 'blog_no': blog_no})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})