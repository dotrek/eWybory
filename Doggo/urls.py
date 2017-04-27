from django.conf.urls import url

from . import views

app_name = 'Doggo'
urlpatterns = [
    # ex: /Doggo/details
    url(r'^$', views.home, name='home'),
    url(r'^(?P<wybory_id>[0-9]+)/$', views.detail_wybory, name='detail_wybory'),
    url(r'^(?P<kandydat_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<kandydat_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<kandydat_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
