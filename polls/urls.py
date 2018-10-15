from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    # ex:/polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex:/polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex:/polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex:/polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # ex:/polls/5/vote/
    url(r'^now$', views.current_time, name='current_time'),

    # ex:/polls/5/vote/
    url(r'^book$', views.book_list, name='book_list'),

    # url(r'^bands/$', views.band_listing, name='band-list'),
    # url(r'^bands/(\d+)/$', views.band_detail, name='band-detail'),
    # url(r'^bands/search/$', views.band_search, name='band-search'),

]
