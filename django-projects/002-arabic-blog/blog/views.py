from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    context = {}
    context['title'] = 'الصفحة الرئيسية'
    context['posts'] = Post.objects.all()
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    context['posts'] = Post.objects.all()
    context['title'] = 'من أنا'

    return render(request, 'blog/about.html', context)

# def detail(request, post_id):
def detail(request, title):
    context = {}
    # context['post'] = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(pk=post_id)
    post = Post.objects.get(title=title)
    context['post'] = post
    context['title'] = post


    return render(request, 'blog/detail.html', context)