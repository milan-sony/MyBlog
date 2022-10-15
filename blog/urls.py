from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    # path('signup/', views.usersignuppage, name='usersignuppage'),
    # path('login/', views.userloginpage, name='userloginpage'),
]