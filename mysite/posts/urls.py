from django.urls import path
from .views import post_list, post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<id>', post, name='post')
]
