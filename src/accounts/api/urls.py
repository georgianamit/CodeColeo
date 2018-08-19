from django.conf.urls import url
from posts.api.views import PostListAPIView, PostCreateAPIView, ShareAPIView


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/post/$', PostListAPIView.as_view(), name='List'),
]