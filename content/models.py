from django.db import models
from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os.path import splitext, basename
class PictureStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'location': settings.MEDIA_ROOT,
            'base_url': settings.MEDIA_URL
        })
        super(PictureStorage, self).__init__(*args, **kwargs)


def upload_path(instance, filename):
    filename = basename(filename)
    _, extension = splitext(filename)
    now = timezone.now()
    prefix = 'pictures'
    return '{}/{}/{}{}'.format(
        prefix, now.year, '1', extension)

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
	picturs = models.ImageField(_('Image file'),upload_to=upload_path,storage=PictureStorage(),blank=True,null=True)
	link = models.CharField(max_length=200, blank=True,null=True)
	nameLink = models.CharField(max_length=200, blank=True,null=True)
	publishPost = models.BooleanField(default=True)
	created_date = models.DateTimeField(default=timezone.now, editable=False)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
			