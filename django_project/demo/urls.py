from django.conf.urls import url
from . import views


urlpatterns = [
    # url('^get_num', views.get_num),
    # url('^get_multi_num', views.get_num_nulti),
    url('^get_multi_res', views.your_view),
]