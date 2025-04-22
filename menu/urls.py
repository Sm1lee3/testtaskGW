from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('e', views.error5, name='error500'),
]

