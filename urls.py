# coding=utf-8
from django.conf.urls import patterns, url
from duck_utils.adminx import PreviewHtmlModelView


urlpatterns = patterns(
    '',
    url(r'^preview_html/(?P<pk>\w+)/$',
        PreviewHtmlModelView.as_view(),
        name='preview_html'),

    )

