from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from analytics.models import ObjectViewed
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class Blog_Post(models.Model):
	title = models.CharField(max_length=1024)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_blogs")
	content = RichTextUploadingField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	category = models.ForeignKey('blogs.Category', null=True, blank=True, related_name="blogs", on_delete=models.PROTECT)
	views = GenericRelation(ObjectViewed, content_type_field = 'content_type', object_id_field = 'object_id')

	def recommend(self):
		return Blog_Post.objects.all()[:4]

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})



class Comment(models.Model):
	content = models.CharField(max_length=512)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default = timezone.now)
	blog = models.ForeignKey(Blog_Post, on_delete=models.CASCADE, related_name='comments')
	reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

	def __str__(self):
		return f'Comment by {self.user} on {self.date_posted}'


class Category(models.Model):
	title = models.CharField(max_length=1024, unique=True)
	desc = models.CharField(max_length=2048)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

	def __str__(self):
		return self.title
