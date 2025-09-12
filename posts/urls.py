# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_feed, name='home_feed'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
]
