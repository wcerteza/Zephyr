from django.urls import path
from . import views

urlpatterns = [
    path("", views.stream, name="stream"),
    path("create/", views.PostCreate.as_view(), name="post_create"),
    path("accounts/signup/", views.signup, name="signup"),
]
