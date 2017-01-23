from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^new/', views.Index.as_view(), name='new'),
    url(r'^$', views.Banner.as_view(), name='index'),
]
