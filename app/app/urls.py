from django.urls import include, path

urlpatterns = [
    path("ping", include("ping.urls")),
    path('api/recipe/', include('recipe.urls')),
]
