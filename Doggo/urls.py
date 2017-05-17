from django.conf.urls import url

from . import views

app_name = 'Doggo'
urlpatterns = [
    # ex: /Doggo/details
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^wybory/(?P<wybory_id>[0-9]+)/$', views.detail_wybory, name='detail_wybory'),
    url(r'^kandydat/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^kandydat/(?P<kandydat_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
