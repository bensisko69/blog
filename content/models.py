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
    return '{}/{}/{}{}'.format(
        'pictures', now.year, filename.replace('.','_'), extension)

class TypePost(models.Model):
	typePost = models.CharField(max_length=200)
	activate = models.BooleanField(default=True)
	def __str__(self):
		return self.typePost

class Post(models.Model):
	class Meta:
	 	verbose_name = "Post"

	title = models.CharField(max_length=200, verbose_name="Titre")
	text = models.TextField(max_length=5000, blank=True,null=True)
	serialNumberVideo = models.CharField(max_length=30, blank=True,null=True, verbose_name="ID de la vidéo")
	typePost = models.ManyToManyField(TypePost, verbose_name="Catégorie")
	picturs = models.ImageField(_('Image file'),upload_to=upload_path,storage=PictureStorage(),blank=True,null=True)
	link = models.CharField(max_length=200, blank=True,null=True, verbose_name="Lien")
	nameLink = models.CharField(max_length=200, blank=True,null=True, verbose_name="Nom du lien à afficher")
	publishPost = models.BooleanField(default=True, verbose_name="Mettre en ligne")
	created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Créé le")
	like = models.IntegerField(default=0, verbose_name="Nombre de like", editable=False)

	def __str__(self):
		return self.title
			
class Contact(models.Model):
	firstname = models.CharField(max_length=200, verbose_name="Prénom", blank=True,null=True)
	lastname = models.CharField(max_length=200, verbose_name="Nom", blank=True,null=True)
	email = models.EmailField(max_length=200, verbose_name="Email")
	text = models.TextField(max_length=5000, verbose_name="Commentaire")
	created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Créé le")
	treaty = models.BooleanField(default=False, verbose_name="Traité")

	def __str__(self):
		return self.email
		