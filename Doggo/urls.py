from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /Doggo/details
    url(r'^$', views.home, name='home'),
    url(r'^P<Kandydat_id>[0-9]+/$', views.details, name='details'),
    url(r'^P<Kandydat_id>[0-9]+/results/$', views.results, name='results'),
]
