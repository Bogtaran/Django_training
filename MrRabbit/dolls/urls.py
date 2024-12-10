from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes, name='clothes'),
    path('footwear/', views.footwear, name='footwear'),
    path('photo/', views.photo, name='photo'),
    path('login/', views.login, name='login'),
    path('post_clothes/<int:post_id>/', views.show_post_clothes, name='post_clothes'),
    path('post_footwear/<int:post_id>/', views.show_post_footwear, name='post_footwear'),
    path('selection_clothes/<str:cloth_type>/', views.show_selection_clothes, name='selection_clothes'),
    path('selection_footwear/<str:foot_type>/', views.show_selection_footwear, name='selection_footwear'),
    ]



