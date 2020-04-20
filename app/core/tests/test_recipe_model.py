
from django.test import TestCase

from core.models import Recipe


# {
# 	“id”: 1,
# 	“name”: “Pizza”
# 	“description”: “Put it in the oven”,
# 	“ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
# }
class RecipeModel(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name='recipeName',
            description='recipeDescription',
        )

    def test_str_should_return_recipe_name(self):
        self.assertEqual(str(self.recipe), 'recipeName')

    def test_should_contain(self):
        self.assertEqual(self.recipe.name, 'recipeName')
