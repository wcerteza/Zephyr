from django.shortcuts import render
from .models import Post


def stream(request):
    posts = Post.objects.all()
    return render(request, "stream.html", {"posts": posts})
