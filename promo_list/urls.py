from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^promos/$', views.Promos.as_view(), name='promos'),
    ]
