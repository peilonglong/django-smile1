from django.conf.urls import url

from . import views

app_name = 'books'

urlpatterns = [
    # ex:/books/
    url(r'^$', views.index, name='index'),

    # ex:/books/5/
    url(r'^search_form/$', views.search_form, name='search_form'),

    # ex:/books/5/results/
    url(r'^search/$', views.search, name='search'),

    url(r'^contact_form/$', views.contact_form, name='contact_form'),
    url(r'^contact/$', views.contact, name='contact'),

    # ex:/books/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # ex:/books/5/vote/
    # url(r'^now$', views.current_time, name='current_time'),

    # ex:/polls/5/vote/
    # url(r'^books', views.book_list, name='book_list'),

]
