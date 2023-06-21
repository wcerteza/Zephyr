from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Comment(models.Model):
    content = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"added to {self.post}({self.id}) at {self.created_at}"


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(
        User#, default=None, blank=True, related_name="liked_posts"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.title}({self.id}) at {self.created_at} {self.user}"

    @property
    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        ordering = ["-updated_at"]

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.id})


class Attachment(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for post_id: {self.post_id} @{self.url}"


# LIKE_CHOICES = (
#     ("Like", "Like"),
#     ("Unlike", "Unlike"),
# )


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey("Post", on_delete=models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=10)

#     def __str__(self):
#         return f"{self.user} liked {self.post}"
