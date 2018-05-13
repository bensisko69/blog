from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth import logout, authenticate, login as dj_login
from pprint import pprint

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

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		dj_login(request, user)
		page = 'admin ok'
		return render(request, 'content/admin.html', {"page":page})
	else:
		page = 'admin nok'
		return render(request, 'content/admin.html', {"page":page})

def logout_view(request):
	logout(request)
	page = 'admin nok'
	return render(request, 'content/admin.html', {"page":page})