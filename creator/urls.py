from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.create_acc_view, name='create_acc'),
    url(r'^add/$', views.add_creator_view, name='add_acc'),
    url(r'^login/$', views.check_login_user, name='check_login'),
    url(r'logout/$',views.logout_acc_view,name='logout_acc')
]
