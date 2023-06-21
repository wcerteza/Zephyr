from django.contrib import admin
from .models import Post, Comment, Attachment#, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Attachment)
#admin.site.register(Like)
