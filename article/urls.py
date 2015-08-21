from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.displayview, name='display'),
    url(r'^create/', views.createview, name='create'),
    url(r'^add/', views.addview, name='add'),
    url(r'^delete/(?P<article_id>[0-9]+)/$', views.deleteview, name='delete'),
]
