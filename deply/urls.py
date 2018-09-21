from django.urls import path, re_path
from django.conf.urls import url

from . import views
from . import views_api



urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path('^api/$', views_api.history, name='history'),
    #url(r'^api1/$', views_api.deply_list),
    #url(r'^api1/(?P<pk>[0-9]+)/$', views_api.deply_detail),
    re_path('api-wanliu/$', views_api.deply_list, name='wanliu'),
    re_path('^api-wanliu/(\d+)/$', views_api.deply_detail, name='wanliu-change'),
    #re_path('^api1/$', views_api.deply_list, name='deply_list'),
    #re_path('^api2/(\d+)/$', views_api.deply_detail, name='deply_detail'),
    #re_path('^api1/(\d+)/$', views_api.deply_detail, name='deply_detail'),
    #url(r'^index/$', views.index,name='index'),
]