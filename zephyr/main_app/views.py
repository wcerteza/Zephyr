from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/detail.html", {"post": post})


class PostUpdate(UpdateView):
    model = Post
    fields = ["title", "content"]

class PostDelete(DeleteView):
    model = Post
    success_url = "/"

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            error_message = "invalid signup, try again!"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
