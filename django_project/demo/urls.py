from django.conf.urls import url
from . import views


urlpatterns = [
    url('^get_num', views.get_num)
]