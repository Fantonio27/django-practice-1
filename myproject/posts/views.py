from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-date')
    # posts = list(Post.objects.values())

    # return JsonResponse({'posts': posts})
    return render(request, 'posts/posts_list.html', {'posts' : posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post' : post})
