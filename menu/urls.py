from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.createmenu, name='create'),
    path('edit/<int:pk>/', views.updatemenu, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('e', views.error5, name='error500'),
]

