from django.urls import path

from . import views

from show import views as show_views  # new


urlpatterns = [
    path('s1', views.xianshihanshu, name='xianshihanshu'),
    path('', show_views.xianshipingtai, name="xianshipingtai"),  # new
]