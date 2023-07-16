from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCace(APITestCase):

    def setUp(self):
        self.user = User(phone='123456789')
        self.user.set_password('123zxc456')
        self.user.save()
        response = self.client.post("/users/api/token", {"phone": "123456789", "password": "123zxc456"})

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_user(self):
        response = self.client.post("/register/", {"phone": "123456789", "password": "123zxc456"})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # def test_list_user(self):
    #     response = self.client.get('/users/')
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     self.assertEquals(response.json(), [{"phone": "123456789", "password": "123zxc456"}])
    #
    # def test_update_user(self):
    #     response = self.client.put("/users/1/", {"phone": "123456789", "password": "123zxc456"})
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     self.assertEquals(response.json(), {"phone": "123456789", "password": "123zxc456"})
    #
    # def test_detail_user(self):
    #     response = self.client.get("/users/1")
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     self.assertEquals(response.json(), {"phone": "123456789", "password": "123zxc456"})
    #
    # def test_delete_user(self):
    #     response = self.client.delete("users/1/")
    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
