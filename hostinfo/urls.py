from django.urls import path, re_path

from . import views
from django.conf.urls import url
#from django.contrib import admin
#from views import *



urlpatterns = [
    #path('', views.index, name='index'),
    re_path('^index/$', views.index, name='index'),
    #url(r'^index/$', views.index,name='index'),
]