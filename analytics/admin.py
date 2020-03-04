import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import redirect, reverse
from django.db import models
from django.contrib import admin
from .models import ObjectViewed, BlogViewed, UserViewed


class ViewOnlyAdmin(admin.ModelAdmin):
	list_display_links = None
	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return False


class ObjectViewedAdmin(ViewOnlyAdmin):
	list_display = ('user', 'content_object', 'timestamp', 'ip_addr')
	search_fields = ['user__username']
	list_display_links = None




class BlogViewedAdmin(ViewOnlyAdmin):
	list_filter = ('author',)
	list_display = ('title', 'author', 'date_posted', 'number_of_views', 'number_of_likes')
	search_fields = ['author__username', 'title']
	date_hierarchy = 'date_posted'

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		qs = qs.annotate(
				_view_count = models.Count("views", distinct = True),
				_like_count = models.Count("likes", distinct = True)
				)
		return qs

	def number_of_views(self, obj):
		return obj._view_count

	def number_of_likes(self, obj):
		return obj._like_count

	def changelist_view(self, request, extra_context=None):
		cdata = self.chart_data()
		as_json = json.dumps(cdata, cls = DjangoJSONEncoder)
		extra_context = extra_context or {"chart_data": as_json}
		view = super().changelist_view(request, extra_context)
		return view
	
	def chart_data(self):
		return BlogViewed.objects.distinct().aggregate(
			_view_count = models.Count("views", distinct=True),
			_like_count = models.Count("likes", distinct=True),
		)
		

	number_of_views.admin_order_field = '_view_count'
	number_of_likes.admin_order_field = '_like_count'


class UserViewedAdmin(ViewOnlyAdmin):
	list_display = ('username', 'number_of_reads', 'number_of_likes', 'number_of_comments')
	search_fields = ['username']
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		qs = qs.annotate(_view_count = models.Count("blog_post__views"), _like_count = models.Count("blog_post__likes"), _comment_count = models.Count("blog_post__comments"))
		return qs

	def number_of_reads(self, obj):
		return obj._view_count

	def number_of_likes(self, obj):
		return obj._like_count

	def number_of_comments(self, obj):
		return obj._comment_count

	number_of_reads.admin_order_field = '_view_count'
	number_of_likes.admin_order_field = '_like_count'
	number_of_comments.admin_order_field = '_comment_count'





admin.site.register(UserViewed, UserViewedAdmin)
admin.site.register(ObjectViewed, ObjectViewedAdmin)
admin.site.register(BlogViewed, BlogViewedAdmin)
