from django.conf.urls import url
from .views import PostListAPIView, PostCreateAPIView, ShareAPIView, LikeToggleAPIView, PostDetailAPIView


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/')),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    # url(r'^search/$', SearchAPIView.as_view(), name='api-search'),
    url(r'^share/(?P<pk>\d+)/$', ShareAPIView.as_view(), name='share'),
    url(r'^like/(?P<pk>\d+)/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^detail/(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='Detail'),
    # url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='Update'),
    # url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='Delete'),
    url(r'^$', PostListAPIView.as_view(), name='List'),
]