from django.conf.urls import url
from .views import PostDetailView, PostListView

urlpatterns = [
    url(r'^detail/', PostDetailView.as_view(), name='PostDetail'),
    url(r'^list/', PostListView.as_view(), name='PostList'),
]

