from django.conf.urls import patterns, url
from ath_res_vis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_school_info/$', views.get_school_info, name='get_school_info'),
]
