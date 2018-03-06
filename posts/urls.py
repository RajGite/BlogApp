from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    post_create,
    post_delete,
    post_detail,
    post_list,
    post_update,
    select_category,
)
urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^category/$', select_category, name='category'),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),

]