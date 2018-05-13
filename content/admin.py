from django.contrib import admin
from .models import TypePost, Post, Contact

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'created_date', 'like', 'publishPost')
	list_filter = ('publishPost', 'created_date')
	list_editable = ["publishPost"]

class ContactAdmin(admin.ModelAdmin):
	list_display = ('lastname', 'firstname', 'created_date', 'treaty')
	list_filter = ('treaty', 'created_date')
	list_editable = ["treaty"]
		

admin.site.register(Post, PostAdmin)
admin.site.register(TypePost)
admin.site.register(Contact, ContactAdmin)