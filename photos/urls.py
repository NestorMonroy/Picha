from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from . import views
app_name = 'photos'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.signup_view, name='register'),
    url(r'^otro/$', views.emailsending, name='otro'),

]
