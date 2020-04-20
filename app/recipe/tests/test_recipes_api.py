from django.urls import reverse

from core.models import Recipe

from rest_framework import status
from rest_framework.test import APITestCase


RECIPES_URL = reverse('recipes:recipe-list')


def detail_url(recipe_id):
    return reverse('recipes:recipe-detail', args=[recipe_id])


def create_fake_recipe(num=0):
    recipe = {
        "name": f'name{num}',
        "description": f'description{num}',
    }

    return Recipe.objects.create(**recipe)


class RecipesApi(APITestCase):

    def test_should_return_recipes_list(self):
        create_fake_recipe(0)
        create_fake_recipe(1)

        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['name'], 'name0')
        self.assertEqual(res.data[1]['name'], 'name1')

    def test_should_filter_recipe_by_name(self):
        create_fake_recipe(0)
        create_fake_recipe(1)

        res = self.client.get(f'{RECIPES_URL}?name=name1')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], 'name1')

    def test_should_create_a_recipe(self):
        newRecipe = {
            "name": 'new recipe',
            "description": 'description new recipe',
            "ingredients": [
                {"name": "ingredient1"},
                {"name": "ingredient2"},
                {"name": "ingredient3"}
            ]
        }

        res = self.client.post(RECIPES_URL, newRecipe, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data["name"], 'new recipe')
        self.assertEqual(res.data["description"], 'description new recipe')

    def test_should_get_the_recipe_detail(self):
        recipeToRetrieve = create_fake_recipe()

        url = detail_url(recipeToRetrieve.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["name"], 'name0')
        self.assertEqual(res.data["description"], 'description0')

    def test_should_return_404(self):
        notExistingId = 999
        url = detail_url(notExistingId)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_full_recipe(self):
        recipeToUpdate = create_fake_recipe()
        payload = {
            "name": "Name Updated",
            "description": "desc update",
            "ingredients": [{"name": "ing1Updated"}]
        }

        res = self.client.put(detail_url(recipeToUpdate.id),
                              payload,
                              format="json"
                              )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], 'Name Updated')
        self.assertEqual(res.data['description'], 'desc update')
        self.assertEqual(res.data['ingredients'][0]['name'], "ing1Updated")

    def test_update_partial_recipe(self):
        recipeToUpdate = create_fake_recipe()
        payload = {
            "name": "Name patched",
        }

        res = self.client.patch(detail_url(recipeToUpdate.id), payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], "Name patched")
        self.assertEqual(res.data['description'], "description0")

    def test_should_delete_the_recipe(self):
        recipeToDelete = create_fake_recipe()

        url = detail_url(recipeToDelete.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Recipe.objects.filter(id=recipeToDelete.id).exists())
