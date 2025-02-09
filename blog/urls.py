from django import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('ajout_post', ajout_post, name='ajout_post'),
    path('post_details', post_details, name='post_details'), 
  
]