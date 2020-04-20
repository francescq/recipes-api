from rest_framework import viewsets

from core.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        nameFilter = self.request.query_params.get('name')
        queryset = self.queryset

        if nameFilter:
            queryset = queryset.filter(name__icontains=nameFilter)

        return queryset.filter()
