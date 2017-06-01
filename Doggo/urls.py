from django.conf.urls import url

from . import views

app_name = 'Doggo'
urlpatterns = [
    # ex: /Doggo/details
    url(r'^$', views.introView, name='intro'),
    url(r'^wybory/(?P<wybory_id>[0-9]+)/$', views.detail_wybory, name='detail_wybory'),
    url(r'^kandydat/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<wybory_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^wybory/(?P<wybory_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^tworcy$', views.creatorsview, name='creators'),
    url(r'^upcoming$', views.UpcomingView.as_view(), name='upcoming'),
    url(r'^previous$', views.PreviousView.as_view(), name='previous'),
    url(r'^home', views.HomeView.as_view(), name='home')
]
