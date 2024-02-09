from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
    posts_list = Post.objects.order_by('-date_created')
    return render(request, 'blog/blog.html', {'posts': posts_list})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})