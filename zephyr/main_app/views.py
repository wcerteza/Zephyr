from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PostForm
from django.urls import reverse_lazy


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
    success_url = reverse_lazy("stream")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
