from rest_framework import serializers


from core.models import Recipe


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'description')


class RecipeDetailSerializer(RecipeListSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)
