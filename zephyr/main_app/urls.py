from django.urls import path
from . import views

urlpatterns = [
    # Stream
    path("", views.stream, name="stream"),
    path("about/", views.about, name="about"),
    # Posts
    path("create/", views.PostCreate.as_view(), name="post_create"),
    path("posts/<int:post_id>/", views.posts_detail, name="detail"),
    path("posts/<int:pk>/update/", views.PostUpdate.as_view(), name="posts_update"),
    path("posts/<int:pk>/delete/", views.PostDelete.as_view(), name="posts_delete"),
    # Account
    path("accounts/signup/", views.signup, name="signup"),
    # Comment
    path(
        "posts/<int:post_id>/comment_create/",
        views.comment_create,
        name="comment_create",
    ),
    # Attachments
    path(
        "posts/<int:post_id/add_attachment",
        views.post_add_attachment,
        name="post_add_attachment",
    ),
    path("like/", views.like_post, name="like_post"),
    path("profile/", views.user_profile, name="profile"),
]
