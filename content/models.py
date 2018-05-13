from django.db import models
from django import forms
from django.utils import timezone

class TypePost(models.Model):
	typePost = models.CharField(max_length=200)
	activate = models.BooleanField(default=True)
	def __str__(self):
		return self.typePost

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(max_length=5000, blank=True,null=True)
	serialNumberVideo = models.CharField(max_length=30, blank=True,null=True)
	typePost = models.ManyToManyField(TypePost)
	picturs = models.ImageField(blank=True,null=True)
	link = models.CharField(max_length=200, blank=True,null=True)
	nameLink = models.CharField(max_length=200, blank=True,null=True)
	publishPost = models.BooleanField(default=True)
	created_date = models.DateTimeField(default=timezone.now, editable=False)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
			