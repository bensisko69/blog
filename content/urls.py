from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'contact', views.contact, name='contact'),
    url(r'adminFront', views.admin, name='admin'),
    url(r'login', views.login, name='login'),
    url(r'logout', views.logout_view, name='logout_view'),
    url(r'like', views.like, name='like'),
    url(r'filterPost', views.filterPost, name='filterPost'),
    url(r'treaty', views.treaty, name='treaty')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)