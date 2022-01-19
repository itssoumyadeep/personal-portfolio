from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#import random
# Create your views here.
from .models import Blog

def blog_home(request):
    blogs = Blog.objects.all()
    return render(request,'blog/home.html',{'blogs':blogs})

def detail_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail_blog.html',{'blog':blog})
