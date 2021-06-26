from  django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('/text', views.text, name='text'),
    path('/jstext', views.jstext, name='jstext'),
    path('/files', views.files, name='files'),
]