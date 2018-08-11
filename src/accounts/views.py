from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

class UserDetailView(DetailView):
    qeryset = User.objects.all()
    template_name = 'accounts/user_detail.html'

    def get_object(self):
            return get_object_or_404(User, username__iexact=self.kwargs.get("username"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        following = UserProfile.objects.is_following(self.request.user,self.get_object())
        context["sidebar"] = False
        context["following"] = following
        return context
    


class UserFollowView(View):

    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)
    
