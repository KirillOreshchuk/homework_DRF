from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='user@test.com', password='password_test')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='course test',
            description='course description test',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='name test',
            description='lesson description test',
            course=self.course,
            video_url='http://www.youtube.com/url_test',
            owner=self.user
        )

    def test_list(self):
        """Тестирование вывода всех уроков"""

        response = self.client.get(
            reverse('education:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.lesson.pk,
                            'name': self.lesson.name,
                            'description': self.lesson.description,
                            'preview': None,
                            'video_url': self.lesson.video_url,
                            'course': self.course.pk,
                            'owner': self.user.pk
                        }
                    ]
            }

        )

    def test_retrieve(self):
        """Тестирование вывода одного урока"""

        response = self.client.get(
            reverse('education:lesson-detail', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.pk,
                'name': self.lesson.name,
                'description': self.lesson.description,
                'preview': None,
                'video_url': self.lesson.video_url,
                'course': self.course.pk,
                'owner': self.user.pk
            }
        )

    def test_create(self):
        """Тестирование создания урока"""
        data = {
            'name': 'lesson test',
            'description': 'description test',
            'course': self.course.pk,
            'video_url': 'http://www.youtube.com/video_url_test'
        }

        response = self.client.post(
            reverse('education:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'name': 'lesson test',
                'description': 'description test',
                'preview': None,
                'video_url': 'http://www.youtube.com/video_url_test',
                'course': self.course.pk,
                'owner': self.user.pk
            }

        )

    def test_update(self):
        """Тестирование редактирования урока"""

        response = self.client.patch(
            reverse('education:lesson-update', kwargs={'pk': self.lesson.pk}),
            data={'name': 'name test 2'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.pk,
                'name': 'name test 2',
                'description': self.lesson.description,
                'preview': None,
                'video_url': self.lesson.video_url,
                'course': self.course.pk,
                'owner': self.user.pk
            }

        )

    def test_delete(self):
        """Тестирование удаления урока"""
        response = self.client.delete(
            reverse('education:lesson-delete', kwargs={'pk': self.lesson.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

