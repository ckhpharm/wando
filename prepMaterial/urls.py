from django.urls import path
from prepMaterial import views

urlpatterns = [
    path("", views.index, name='index'),
]
