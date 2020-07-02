from .signals import object_viewed_signal

class ObjectViewedMixin(object):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		request = self.request
		instance = context.get('object')
		if instance:
			object_viewed_signal.send(instance.__class__, instance=instance, request=request)
		elif kwargs.get('object_viewed'):
			instance = kwargs.get('object_viewed')
			object_viewed_signal.send(instance.__class__, instance=instance, request=request)
		return context

