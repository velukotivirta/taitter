from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"), # Go into views.py and look for the homepage()-function
    path('new_post/', views.post_new, name="new_post"), 
    path('<slug:slug>', views.post_page, name="page"), 
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]

