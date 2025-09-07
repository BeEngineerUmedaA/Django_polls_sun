from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("hobby/", views.hobby, name="hobby"),
    path("greet/<str:name>/", views.greet, name="greet"),

]


