from django.shortcuts import redirect, reverse
from django.contrib import admin
#from django.core.urlresolvers import reverse
from .models import ObjectViewed

class ObjectViewedAdmin(admin.ModelAdmin):
	list_display = ('user', 'content_object', 'timestamp', 'ip_addr')
	list_editable = ()
	search_fields = ['user__username']
	exclude = ["id", "content_type", "object_id"] 
	readonly_fields = [f.name for f in ObjectViewed._meta.fields if f.name not in ("id", "content_type", "object_id")]
	list_display_links = None

	def change_view(self, request, object_id, form_url='', extra_context=None):
		opts = self.model._meta
		url = reverse('admin:{app}_{model}_changelist'.format(app=opts.app_label,model=opts.model_name,))	
		return redirect(url) 

admin.site.register(ObjectViewed, ObjectViewedAdmin)
