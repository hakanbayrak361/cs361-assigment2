from django.conf.urls import url

from .views import show_blog,get_blog

urlpatterns = [
    url(r'^blog/entries/$', show_blog),
    url(r'^blog/entries/(?P<todo_id>[0-9]+)', get_blog)
]
