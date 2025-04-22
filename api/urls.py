from django.urls import path
from . import views
from django.conf.urls import handler500, handler404
urlpatterns = [
    path('', views.getData),
    path('parent', views.getParent),
]
