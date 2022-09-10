from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('upload', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('uploadmaterial' , views.uploadmaterial, name='uploadmaterial')
    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
]