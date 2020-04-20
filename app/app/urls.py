from django.urls import include, path

urlpatterns = [
    path("ping", include("ping.urls")),
    path('api/', include('recipe.urls')),
]
