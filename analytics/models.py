from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from .signals import object_viewed_signal
from .utils import get_client_ip
# Create your models here.

User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
        user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
        ip_addr = models.CharField(max_length=220, blank=True, null=True)
        content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
        object_id = models.PositiveIntegerField()
        content_object = GenericForeignKey('content_type', 'object_id')
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return "%s viewed on %s by %s"%(self.content_object, self.timestamp, self.user)

        class Meta:
                ordering = ['-timestamp']
                verbose_name = 'Object Viewed'
                verbose_name_plural = "Objects Viewed"


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
        ctype = ContentType.objects.get_for_model(sender)
        if request.user.is_anonymous :
                user = None
        else:
                user = request.user
        new_view = ObjectViewed.objects.create(
                        user = user,
                        ip_addr = get_client_ip(request),
                        content_type = ctype,
                        object_id = instance.id
                        )
object_viewed_signal.connect(object_viewed_receiver)




#PROXY Models
class BlogViewedManager(models.Manager):
        def get_queryset(self):
                return super().get_queryset().distinct()



from blogs.models import Blog_Post
class BlogViewed(Blog_Post):

        objects = BlogViewedManager()

        class Meta:
                proxy = True
                verbose_name = "Blog Viewed"
                verbose_name_plural = "Blogs Viewed"




## Second Proxy model User
from users.models import User
class UserViewed(User):
        class Meta:
                proxy = True
                verbose_name = "User Blog Viewed"
                verbose_name_plural = "User Blogs Viewed"


from users.models import LoginLogs
class UserLoggedInLog(LoginLogs):
        class Meta:
                proxy = True
                verbose_name = "Login Log"
                verbose_name_plural = "Login Logs"
