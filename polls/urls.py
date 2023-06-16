from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.viewlist, name='view_list'),
    path('', views.index, name='index'),
]
