from django.urls import path,include
from . import views
from .views import index
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url

urlpatterns=[

    path('', views.index,name='index file'),
    path('accounts/', include('django.contrib.auth.urls')),

]