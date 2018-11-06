from django.urls import path
from . import views

urlpatterns = [
    #Show all posts.
    path('', views.post_list, name='post_list'),
    #Individual page for the post.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #Create a new post.
    path('post/new/', views.post_new, name='post_new'),
    #Edit page for a post.
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #Page of unpublished posts.
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    #Publish a post.
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #Remove a post.
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    #Page for post comments.
    path('post/(<pk>)/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #Approving comments.
    path('comment/(<int:pk>)/approve', views.comment_approve,  name='comment_approve'),
    #Removing any comments.
    path('comment/(<int:pk>)/remove', views.comment_remove,  name='comment_remove'),
    ]
    
