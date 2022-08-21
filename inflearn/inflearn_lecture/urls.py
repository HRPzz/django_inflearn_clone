from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결
]