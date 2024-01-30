from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.models import Course, Lesson
from subscription.models import Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='user@test.com', password='password_test')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='course_test',
            owner=self.user
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course
        )

    def test_sub_create(self):
        """Тест создания подписки"""

        data = {
            'user': self.user.pk,
            'course': self.course.pk,
        }

        response = self.client.post(
            reverse('subscription:subscription-create'),
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_sub_delete(self):

        response = self.client.delete(
            reverse('subscription:subscription-delete', kwargs={'pk': self.subscription.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
