from django.shortcuts import render
from .models import Post, Genre

def post_list(request):

    posts = Post.objects.all()
    genres = Genre.objects.all()
    context = {
        "posts": posts,
        "genres": genres
    }

    return render(request, 'posts/post_list.html', context)

def post(request, id):

    post = Post.objects.get(id = id)

    context = {
        "post": post,
    }

    return render(request, 'posts/post.html', context)