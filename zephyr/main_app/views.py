from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PostForm, CustomUserCreationForm, CommentForm
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
    posts_form = PostForm()
    title = f'{post.user}:"{post.title}"'
    return render(
        request,
        "posts/detail.html",
        {
            "post": post,
            "title": title,
            "posts_form": posts_form,
        },
    )


class PostUpdate(UpdateView):
    model = Post
    fields = ["title", "content"]


class PostDelete(DeleteView):
    model = Post
    success_url = "/"


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            error_message = "Invalid signup, please try again!"
    else:
        form = CustomUserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        form = CommentForm()

    return render(
        request,
        "posts/detail.html",
        {"post": post, "form": form, "comment": comment},
    )
