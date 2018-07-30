from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='delete'),
    url(r'^list/', PostListView.as_view(), name='list'),
]

