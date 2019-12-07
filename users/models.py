from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.jpg')

	def __str__(self):
		return f'{self.user.username} Profile'
