from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PostForm


def stream(request):
    posts = Post.objects.all()
    posts_form = PostForm()
    return render(
        request,
        "stream.html",
        {
            "posts": posts,
            "title": "Welcome To The Stream | Zephyr",
            "posts_form": posts_form,
        },
    )


class PostCreate(CreateView):
    model = Post
    fields = ["title", "content"]
