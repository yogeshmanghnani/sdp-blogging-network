from django.db import models
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	email = models.EmailField(unique=True, null=True)

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 and img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
