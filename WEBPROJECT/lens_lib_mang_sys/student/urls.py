from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from django.urls import include, re_path
from django.views.static import serve

urlpatterns = [
    path('', views.login, name='login'),
    path('account', views.account, name='account'),
    path('logout', views.logout, name='logout'),
    path('content', views.content, name='content')
    # url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    
]
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

