from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Dropdown.as_view(), name="page")
]  