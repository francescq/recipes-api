from django.test import TestCase
from django.urls import reverse

from core.models import Recipe

from rest_framework import status
from rest_framework.test import APIClient


RECIPES_URL = reverse('recipes:recipe-list')


def detail_url(recipe_id):
    return reverse('recipes:recipe-detail', args=[recipe_id])


def create_fake_recipe(num=0):
    recipe = {
        "name": f'name{num}',
        "description": f'description{num}'
    }

    return Recipe.objects.create(**recipe)


class RecipesApi(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_should_return_recipes_list(self):
        create_fake_recipe(0)
        create_fake_recipe(1)

        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertDictEqual(dict(res.data[0]), {
            'name': 'name0',
            'description': 'description0'
        })
        self.assertDictEqual(dict(res.data[1]), {
            'name': 'name1',
            'description': 'description1'
        })

    def test_should_create_a_recipe(self):
        newRecipe = {
            "name": 'new recipe',
            "description": 'description new recipe'
        }

        res = self.client.post(RECIPES_URL, newRecipe)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(res.data, {
            'id': 3,
            'name': 'new recipe',
            'description': 'description new recipe'
        })

    def test_should_get_the_recipe_detail(self):
        recipeToRetrieve = create_fake_recipe()

        url = detail_url(recipeToRetrieve.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertDictEqual(res.data, {
            'id': 4,
            'name': 'name0',
            'description': 'description0'
        })
