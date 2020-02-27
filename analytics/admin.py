from django.shortcuts import redirect, reverse
from django.db import models
from django.contrib import admin
from .models import ObjectViewed, BlogViewed


class ViewOnlyAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

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

	number_of_views.admin_order_field = '_view_count'
	number_of_likes.admin_order_field = '_like_count'



admin.site.register(ObjectViewed, ObjectViewedAdmin)
admin.site.register(BlogViewed, BlogViewedAdmin)
