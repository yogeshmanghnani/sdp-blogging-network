from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Blog_Post(models.Model):
	title = models.CharField(max_length=64)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_blogs")
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})
