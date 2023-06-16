from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=90)
    content = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}({self.id}) at {created_at}"
