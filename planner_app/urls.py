from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("task/", views.task, name="task"),
    path("task/<int:pk>/", views.task_detail, name="task_detail"),
    path("task/new/", views.task_create, name="task_create"),
    path("task/<int:pk>/edit/", views.task_edit, name="task_edit"),
]
