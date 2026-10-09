from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.task = Task.objects.create(title='Test Task', description='Test Description', completed=False)
        self.list_url = reverse('task-list')

    def test_get_tasks_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tasks_authenticated(self):
        # Авторизуем клиента
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'New API Task', 'description': 'API Desc', 'completed': False}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
