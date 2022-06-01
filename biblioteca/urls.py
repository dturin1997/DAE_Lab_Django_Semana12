#from django.conf.urls import url
from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^prestamos/$', views.prestamo_list),
    re_path(r'^prestamos/(?P<pk>[0-9]+)/$', views.prestamo_detail),
]