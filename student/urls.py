from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),  #homepage
    url(r'^(?P<zID>z[0-9]{7})$', views.detail, name = 'detail'),
]