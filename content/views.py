from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	page = 'home'
	return render(request, 'content/post.html', {'posts': posts, "page": page})

def contact(request):
	page = 'contact'
	return render(request, 'content/contact.html', {"page":page})

def admin(request):
	page = 'admin'
	return render(request, 'content/admin.html', {"page":page})