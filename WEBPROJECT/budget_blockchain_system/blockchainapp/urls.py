from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('account', views.account, name='account'),
    path('transaction', views.transaction, name='transaction'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout')
]