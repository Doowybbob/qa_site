from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.index, name="index"),
        url(r'^ask/$', views.ask, name="ask"),
        url(r'^add_question/$', views.add_question, name="add_question"),
        ]
