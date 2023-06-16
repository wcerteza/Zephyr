from django.db import models
from django.urls import reverse
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}({self.id}) at {self.created_at}"

    # class Meta:
    #     ordering = ["-date"]


# class Comments(models.Model):
#     title = models.CharField(max_length=90)
#     content = models.TextField(max_length=160)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title}({self.id}) at {created_at}"


# class Attachments(models.Model):
#     url = models.CharField(max_length=200)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=true)

#     def __str__(self):
#         return f"Attachment for post_id: {self.post_id} @{self.url}"


# class Likes(models.Model):
#     title = models.CharField(max_length=90)
#     content = models.TextField(max_length=160)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title}({self.id}) at {created_at}"
