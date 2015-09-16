from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name="index"),
        url(r'^(?P<pk>[0-9]+)/$', views.detail, name="detail"),
        url(r'^ask/$', views.ask, name="ask"),
        url(r'^add_question/$', views.add_question, name="add_question"),
        ]
