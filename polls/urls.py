from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]