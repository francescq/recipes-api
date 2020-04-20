
from django.test import TestCase

from core.models import Recipe, Ingredient


# {“name”: “casa-tarradellas”}
class IngredientModel(TestCase):
    def setUp(self):
        recipe = Recipe.objects.create(
            name='recipe1',
            description='desc1'
        )

        self.ingredient = Ingredient.objects.create(
            name='ingredient1',
            recipe=recipe
        )

    def test_str_should_return_ingredient_name(self):
        self.assertEqual(str(self.ingredient), 'ingredient1')

    def test_should_contain(self):
        self.assertEqual(self.ingredient.name, "ingredient1")
