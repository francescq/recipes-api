
from django.test import TestCase

from core import models


def _create_fake_recipe(self):
    return models.Recipe.objects.create(
        name='recipeName',
        description='recipeDescription',
    )


# {
# 	“id”: 1,
# 	“name”: “Pizza”
# 	“description”: “Put it in the oven”,
# 	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
# }
class RecipeModel(TestCase):
    def setUp(self):
        self.recipe = _create_fake_recipe(self)

    def test_str_should_return_recipe_name(self):
        self.assertEqual(str(self.recipe), 'recipeName')

    def test_should_contain(self):
        self.assertEqual(self.recipe.id, 1)
        self.assertEqual(self.recipe.name, 'recipeName')
        self.assertEqual(self.recipe.description, 'recipeDescription')
