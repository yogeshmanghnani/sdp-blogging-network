from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Profile, LoginLogs

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, created,  **kwargs):
	instance.profile.save()

@receiver(user_logged_in)
def on_login(sender, request, user, **kwargs):
	log = LoginLogs(user=user)
	log.save()
