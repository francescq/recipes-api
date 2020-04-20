from django.urls import path
from ping import views

urlpatterns = [
    path("", views.home, name="ping"),
]
