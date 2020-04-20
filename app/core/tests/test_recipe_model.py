
from django.test import TestCase

from core import models


# {
# 	“id”: 1,
# 	“name”: “Pizza”
# 	“description”: “Put it in the oven”,
# 	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
# }
class RecipeModel(TestCase):
    def setUp(self):
        self.recipe = models.Recipe.objects.create(
            name='recipeName',
            description='recipeDescription',
        )

    def test_str_should_return_recipe_name(self):
        self.assertEqual(str(self.recipe), 'recipeName')

    def test_should_contain_name_an_description(self):
        self.assertEqual(self.recipe.name, 'recipeName')
        self.assertEqual(self.recipe.description, 'recipeDescription')
