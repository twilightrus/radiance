from django.contrib import admin

from blog.models import Article, Comment, Like


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
