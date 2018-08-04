from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.models import User
# Create your views here.

class UserDetailView(DetailView):
    qeryset = User.objects.all()
    template_name = 'accounts/user_detail.html'

    def get_object(self):
            return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar"] = True
        return context
    
