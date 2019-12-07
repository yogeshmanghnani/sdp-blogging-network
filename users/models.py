from django.db import models
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


