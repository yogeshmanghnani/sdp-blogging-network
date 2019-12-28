from django.shortcuts import render, get_object_or_404
from .models import Blog_Post, Comment
from users.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponse, Http404
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
	paginate_by = 12
	model = Blog_Post
	template_name = "blogs/home.html"
	context_object_name = "posts"
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Blog Posts"
		context['blog_home'] = 'uk-active'
		return context


class UserPostListView(ListView):
	paginate_by = 12
	model = Blog_Post
	template_name = "blogs/user_posts.html"
	context_object_name = "posts"
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
		author = get_object_or_404(User, username=self.kwargs.get('username'))
		context = super().get_context_data(**kwargs)
		context['title'] = "Blog Posts by " + author.username
		context['author'] = author
		return context

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Blog_Post.objects.filter(author=user)


class PostDetailView(DetailView):
	model = Blog_Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = self.object.title

		#Pass Comment
		current_post = get_object_or_404(Blog_Post, pk=self.kwargs.get('pk'))
		comments = Comment.objects.filter(blog=current_post, reply_to__isnull=True).order_by('-date_posted')
		context['comments'] = comments

		#if like pass context
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



@login_required
def comment(request, pk):
	if request.method == 'POST':
		blog = Blog_Post.objects.get(pk=pk)
		com = Comment()
		com.content = request.POST.get("content").strip()
		com.user = request.user
		com.blog = blog
		if not com.content == "":
			com.save()
			return render(request, 'blogs/elements/comments/comment_card.html', {"comment": com})
		else:
			return HttpResponse()
	else:
		raise Http404("Not Found")




@login_required
def comment_delete(request, pk, comid):
	pass
