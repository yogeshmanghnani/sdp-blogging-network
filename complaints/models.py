from django.db import models
from django.utils import timezone
from blogs.models import Comment
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Complaint(models.Model):
        title = models.CharField(max_length=64)
        body = models.CharField(max_length=4096)
        resolved = models.BooleanField(default=False)
        date_posted = models.DateTimeField(default = timezone.now)
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

        def __str__(self):
                return self.title

        def get_absolute_url(self):
                return reverse('complaint_done')

