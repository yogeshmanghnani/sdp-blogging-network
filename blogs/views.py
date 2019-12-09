from django.shortcuts import render
from .models import Blog_Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	posts = Blog_Post.objects.all()
	context = {
			'posts': posts,
			'title' : "Blog Posts",
			'blog_home': 'uk-active'
			}
	return render(request, 'blogs/home.html', context)



class PostListView(ListView):
	model = Blog_Post
	template_name = "blogs/home.html"
	context_object_name = "posts"
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Blog Posts"
		context['blog_home'] = 'uk-active'
		return context


class PostDetailView(DetailView):
	model = Blog_Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.object.title
		if self.request.user in self.object.likes.all():
			context['liked'] = "uk-text-danger"
		return context

	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Blog_Post
	fields = ['title', 'content']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Create New Post"
		context['post_create'] = 'uk-active'
		return context

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Blog_Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		return self.get_object().author == self.request.user

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Update your post"
		context['post_create'] = 'uk-active'
		return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Blog_Post
	success_url = '/'

	def test_func(self):
		return self.get_object().author == self.request.user


def about(request):
	context = {
			'blog_about': 'uk-active',
			'title': 'About'
			}
	return render(request, 'blogs/about.html', context)


@login_required
def like(request, pk):
	if request.method == 'POST':
		response = {}
		blog = Blog_Post.objects.get(pk=pk)
		if request.user in blog.likes.all():
			blog.likes.remove(request.user)
			response['liked'] = False
		else:
			blog.likes.add(request.user)
			response['liked'] = True
		response['numOfLikes'] = blog.likes.count()
		return JsonResponse(response)
	else:
		raise Http404("Not Found")
