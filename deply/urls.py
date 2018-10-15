from django.urls import path, re_path
from django.conf.urls import url

from . import views
from . import views_api



urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path('^api/$', views_api.history, name='history'),
    re_path('api-wanliu/$', views_api.deply_list, name='wanliu'),
    re_path('^api-wanliu/(\d+)/$', views_api.deply_detail, name='wanliu-change'),
]