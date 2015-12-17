from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /cards/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /cards/3/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    ]
