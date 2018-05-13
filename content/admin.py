from django.contrib import admin
from .models import TypePost, Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'created_date', 'publishPost')

admin.site.register(Post, PostAdmin)
admin.site.register(TypePost)