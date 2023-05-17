from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_list, name = "home_list"),
    path("pet_list/", views.pet_list, name = "pet_list"),
    path("pet_list/<int:pk>", views.pet_list_info, name = "pet_list_info"),
    path("comment_remove/<int:pk>", views.comment_remove, name = "comment_remove"),
    path("show_pet_video/<int:pk>", views.show_pet_video, name = "show_pet_video"),
    path("login/", views.login, name = "login"),
    path("logout/", views.logout, name = "logout"),
    path("join/", views.join, name = "join"),
]