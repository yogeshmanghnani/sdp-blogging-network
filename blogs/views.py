from django.shortcuts import render
from .models import Blog_Post
# Create your views here.

def home(request):
	posts = Blog_Post.objects.all()
	context = {
			'posts': posts,
			'title' : "Blog Posts",
			'blog_home': 'uk-active'
			}

	return render(request, 'blogs/home.html', context)


def about(request):
	context = {
			'blog_about': 'uk-active'
			}
	return render(request, 'blogs/about.html', context)
