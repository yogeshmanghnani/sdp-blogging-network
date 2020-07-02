from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Complaint

# Create your views here.
class ComplaintCreateView(LoginRequiredMixin, CreateView):
        model = Complaint
        fields = ['title', 'body']

        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)


def complaint_done(request):
        return render(request, 'complaints/done.html')
