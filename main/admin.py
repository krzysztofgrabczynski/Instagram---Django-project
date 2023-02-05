from django.contrib import admin
from .models import UserProfile, Post, Comment, Follow, Like


admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)


