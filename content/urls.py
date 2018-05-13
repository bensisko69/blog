from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'contact', views.contact, name='contact'),
    url(r'admin', views.admin, name='admin'),
    url(r'login', views.login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)