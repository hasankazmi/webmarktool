from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('signin/', views.Signin, name='signin'),
    path('signout/', views.Signout, name='signout')
]