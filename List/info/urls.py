from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path("", views.index, name="index"),
    path("addSchool", views.addSchool, name = "addSchool"),
    path("deleteSchools", views.deleteSchools, name="deleteSchools"),
]
