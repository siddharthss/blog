from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index_view,name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.display_view, name='display'),
    url(r'^create/', views.create_view, name='create'),
    url(r'^add/', views.add_view, name='add'),
    url(r'^delete/(?P<article_id>[0-9]+)/$', views.delete_view, name='delete'),
    url(r'^update/(?P<article_id>[0-9]+)/$', views.update_content_view, name='update_content'),
]
