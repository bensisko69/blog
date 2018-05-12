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
	text = models.TextField(max_length=5000)
	authors = models.ManyToManyField(TypePost)
	picturs = models.ImageField()
	publish = models.BooleanField(default=True)
	created_date = models.DateTimeField(default=timezone.now)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
			