# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from .views import match

urlpatterns = patterns(
    '',
    (r'^match/(?P<match_pk>\d+)/$', match, {}, 'match'),
)
