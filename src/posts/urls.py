from django.conf.urls import url
from .views import PostDetailView, PostListView, PostCreateView

urlpatterns = [
    url(r'^create/$', PostCreateView.as_view(), name='Create'),
    url(r'^detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='Detail'),
    url(r'^list/', PostListView.as_view(), name='List'),
]

