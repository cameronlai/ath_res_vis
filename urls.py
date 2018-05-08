from django.conf.urls import patterns, url

from ath_res_vis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'ajax/load-names/', views.load_names, name='load_names'),
]
