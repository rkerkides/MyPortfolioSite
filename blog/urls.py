from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]


