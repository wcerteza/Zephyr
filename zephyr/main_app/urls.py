from django.urls import path
from . import views

urlpatterns = [
    # Stream
    path("", views.stream, name="stream"),
    # Posts
    path("create/", views.PostCreate.as_view(), name="post_create"),
    path("posts/<int:post_id>/", views.posts_detail, name="detail"),
    path("posts/<int:pk>/update/", views.PostUpdate.as_view(), name="posts_update"),
    path("posts/<int:pk>/delete/", views.PostDelete.as_view(), name="posts_delete"),
    # Account
    path("accounts/signup/", views.signup, name="signup"),
]
