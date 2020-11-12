from django.urls import path
from .import views

urlpatterns=[
    path("", views.home, name="home"),
    path('formtest/',views.formtest),
    path("starter/", views.starter, name="starter"),
]