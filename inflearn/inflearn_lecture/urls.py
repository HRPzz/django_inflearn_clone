from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]