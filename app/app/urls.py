from django.urls import include, path

urlpatterns = [
    path("ping", include("ping.urls")),
]
