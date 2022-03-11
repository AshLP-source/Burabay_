from django.urls import path
from django.views.generic import ListView
from . import views

urlpatterns = [
    path('', views.home, name='main_page'),
    path('blog/', views.blog, name='blog_page'),
    path('rooms/', views.rooms, name='rooms_page'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
    path('single-blog/', views.single_blog, name='single_blog_page'),

]
