
from django.urls import path
from . import views

urlpatterns = [

    path("autor/", views.autor, name="autor"),
    path("posteo/", views.posteo, name="posteo"),
    path("categoria/", views.categoria, name="categoria"),  
    path("home/", views.home, name="home")
]
