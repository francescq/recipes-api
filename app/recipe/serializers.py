from rest_framework import serializers
from core.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'ingredients')
        read_only_fields = ('id',)

    def __create_ingredients(self, ingredients, recipe):
        # print(f'serialize.__create_ingredients={ingredients} {recipe}')
        for ingredient in ingredients:
            Ingredient.objects.create(
                name=ingredient['name'],
                recipe=recipe
            )

    def create(self, validated_data):
        # print(f'serialize.create validated_data={validated_data}')
        ingredients = validated_data.pop('ingredients')

        recipe = Recipe.objects.create(
            name=validated_data['name'],
            description=validated_data['description']
        )

        self.__create_ingredients(ingredients, recipe)
        return recipe

    def update(self, recipe, validated_data):
        # print(f'serialize.update validated_data={validated_data}')
        hasIngredients = validated_data.get('ingredients')
        if hasIngredients is not None:
            ingredients = validated_data.pop('ingredients')
        # print(f'ingredients {ingredients}---')

        recipe = super().update(recipe, validated_data)
        recipe.save()

        if hasIngredients:
            recipe.ingredients.all().delete()
            self.__create_ingredients(ingredients, recipe)

        return recipe
