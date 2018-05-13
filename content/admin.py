from django.contrib import admin
from .models import TypePost, Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'created_date', 'publishPost')
	list_filter = ('publishPost', 'created_date')
	search_fields = ('created_date', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(TypePost)