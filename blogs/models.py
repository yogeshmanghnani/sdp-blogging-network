from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Blog_Post(models.Model):
	title = models.CharField(max_length=64)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
