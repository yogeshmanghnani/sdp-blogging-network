from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),
	path('about/', views.about, name="blog_about"),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
	path('post/<int:pk>/update', views.PostUpdateView.as_view(), name="post_update"),
	path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="post_delete"),
	path('post/<int:pk>/like', views.like, name="post_like"),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
]
