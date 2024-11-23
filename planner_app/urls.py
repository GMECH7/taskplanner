from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.custom_register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("task/", views.task, name="task"),
    path("task/<int:pk>/", views.task_detail, name="task_detail"),
    path("task/new/", views.task_create, name="task_create"),
    path("task/<int:pk>/edit/", views.task_edit, name="task_edit"),
    path("task/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("category/", views.category, name="category"),
    path("category/<int:pk>/", views.category_detail, name="category_detail"),
    path("category/new/", views.category_create, name="category_create"),
    path("category/<int:pk>/edit/", views.task_edit, name="category_edit"),
    path("category/<int:pk>/delete/", views.category_delete, name="category_delete"),
]
