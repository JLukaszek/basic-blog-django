from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date']
    ordering = ['-publish_date']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)