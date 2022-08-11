from django.contrib import admin
from post.models import *
# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'slug']
    # list_display_links = ['id', 'name', 'slug']

admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','category', 'date', 'slug']

admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Comment, CommentAdmin)
