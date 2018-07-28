from django.conf.urls import url
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    url(r'^create/$', PostCreateView.as_view(), name='Create'),
    url(r'^detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='Detail'),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='Update'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='Delete'),
    url(r'^list/', PostListView.as_view(), name='List'),
]

