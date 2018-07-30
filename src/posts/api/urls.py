from django.conf.urls import url
from .views import PostListAPIView, PostCreateAPIView


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/')),
    url(r'^create/$', PostCreateAPIView.as_view(), name='Create'),
    # url(r'^detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='Detail'),
    # url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='Update'),
    # url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='Delete'),
    url(r'^$', PostListAPIView.as_view(), name='List'),
]