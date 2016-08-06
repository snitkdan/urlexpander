from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^urlexpander/$', views.url_home),
	url(r'^urlexpander/(?P<url_pk>[0-9]+)/$', views.url_detail),
	url(r'^urlexpander/new/$', views.url_add),
	url(r'^urlexpander/(?P<url_pk>[0-9]+)/delete/$', views.url_delete),
]
