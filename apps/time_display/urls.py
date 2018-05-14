from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),### this is going to call the index function under views.py
    url(r'^time_display$', views.index, name='index')
]