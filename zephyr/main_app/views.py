import os
import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Post, Comment, Attachment, Like
from django.contrib.auth.models import User
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
    users = User.objects.all()
    return render(
        request,
        "stream.html",
        {
            "posts": posts,
            "user": users,
            "title": "Welcome To The Stream | Zephyr",
            "posts_form": posts_form,
        },
    )


def about(request):
    return render(request, "about.html", {"title": "Decentralized Wonderland"})


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
            print(user)
            return redirect("/")
        else:
            error_message = "Invalid signup, please try again!"
    else:
        form = CustomUserCreationForm()
    context = {"form": form, "error_message": error_message}
    print(user)
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


def post_add_attachment(request, post_id):
    attachment_file = request.FILES.get("photo-file", None)
    if attachment_file:
        s3 = boto3.client("s3")
        key = (
            uuid.uuid4().hex[:6]
            + attachment_file_file.name[attachment_file_file.name.rfind(".") :]
        )
        try:
            bucket = os.environ["S3_BUCKET"]
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Attachment.objects.create(url=url, post_id=[post_id])
        except Exception as e:
            print("An error occurred uploading file to S3")
            print(e)
    return redirect("detail", post_id=post_id)


def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == "Like":
                like.value = "Unlike"
            else:
                like.value = "Like"

        like.save()
    return redirect("/")


def user_profile(request, user_id):
    posts = Post.objects.filter(user=request.user)
    user = User.objects.get(id=user_id)
    return render(request, "user/user_profile.html", {"posts": posts, "user": user})


@login_required
def my_profile(request):
    print(request.user)
    posts = Post.objects.filter(user=request.user)
    return render(request, "user/my_profile.html", {"posts": posts})
