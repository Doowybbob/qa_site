from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name="index"),
        url(r'^(?P<pk>[0-9]+)/$', views.detail, name="detail"),
        url(r'^(?P<pk>[0-9]+)/up/$', views.voteUp, name="up"),
        url(r'^(?P<pk>[0-9]+)/down/$', views.voteDown, name="down"),
        url(r'^answer/(?P<pk>[0-9]+)/up/$', views.answerVoteUp, name="aUp"),
        url(r'^answer/(?P<pk>[0-9]+)/down/$', views.answerVoteDown, name="aDown"),
        url(r'^ask/$', views.ask, name="ask"),
        url(r'^tag/(?P<pk>[0-9]+)/$', views.by_tag, name="tag"),
        ]
