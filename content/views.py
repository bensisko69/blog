from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'content/post.html', {'posts': posts})

def contact(request):
	return render(request, 'content/contact.html')