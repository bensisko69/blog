from django.contrib.auth import logout, authenticate, login as dj_login
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers
import json
from .models import Post, TypePost, Contact
from .form import ContactForm
from pprint import pprint



def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	types = TypePost.objects.all()
	page = 'home'
	return render(request, 'content/post.html', {'posts': posts, "page": page, 'types':types})

def contact(request):
	page = 'contact'
	formset = ContactForm(request.POST)
	return render(request, 'content/contact.html', {"page":page, 'formset':formset})

def admin(request):
	page = 'admin'
	if (request.user.is_authenticated):
		contacts = Contact.objects.filter(created_date__lte=timezone.now(), treaty=False).order_by('created_date')
		return render(request, 'content/admin.html', {"page":page, 'contacts':contacts})
	return render(request, 'content/admin.html', {"page":page})

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		dj_login(request, user)
		page = 'admin'
		contacts = Contact.objects.filter(created_date__lte=timezone.now(), treaty=False).order_by('created_date')
		return render(request, 'content/admin.html', {"page":page, 'contacts':contacts})
	else:
		page = 'admin'
		return render(request, 'content/admin.html', {"page":page})

def logout_view(request):
	logout(request)
	page = 'admin'
	return render(request, 'content/admin.html', {"page":page})

def like(request):
	response = {}
	if (request.method == 'POST'):
		postId = request.POST.get('id')
		if (postId):
			post = Post.objects.get(id=postId)
			if (post):
				post.like +=1
				post.save()
				response['status'] = 'success'
				response['like'] = post.like
			else:
				response['status'] = 'wrong'
				response['error'] = 'no post'
		else:
			response['status'] = 'wrong'
			response['error'] = 'no post id'
	else:
		response['status'] = 'wrong'
		response['error'] = 'no requete post'
	return HttpResponse(json.dumps(response),content_type="application/json")

def filterPost(request):
	if (request.method == 'POST'):
		response = {}
		typeId = request.POST.get('id')
		if (typeId == 'null'):
			posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
		else:
			posts = Post.objects.filter(typePost=typeId).order_by('created_date')
		response['status'] = 'success'
		response['posts'] = json_serialized_objects = serializers.serialize("json", posts)
	return HttpResponse(json.dumps(response),content_type="application/json")