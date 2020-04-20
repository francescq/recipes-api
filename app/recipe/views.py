from rest_framework import viewsets
from core.models import Recipe


from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeListSerializer
        else:
            return serializers.RecipeDetailSerializer

        return self.serializer_class
