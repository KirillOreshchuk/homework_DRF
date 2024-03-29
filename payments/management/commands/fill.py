import random
from decimal import Decimal
from faker import Faker
from django.core.management import BaseCommand

from education.models import Lesson, Course
from payments.models import Payment
from users.models import User

fake = Faker()


class Command(BaseCommand):
    """
    Команда для сброса и добавления тестовых данных в БД
    """

    def handle(self, *args, **kwargs):

        # Удаляем все объекты классов Payment, Lesson, Course
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        # Создаем 3 пользователя
        users = []
        for i in range(3):
            email = fake.email()
            password = fake.password()
            phone = fake.numerify()
            city = fake.city()
            user = User.objects.create(email=email, password=password, phone=phone, city=city)
            users.append(user)

            # Создаем 2 курса у каждого пользователя по 3 урока в каждом
            courses = []
            lessons = []
            for i in range(2):
                course = Course.objects.create(
                    name=fake.word(),
                    description=fake.text(),
                    owner=user,
                )
                courses.append(course)

                for i in range(3):
                    lesson = Lesson.objects.create(
                        name=fake.sentence(),
                        description=fake.text(),
                        course=course,
                        video_url=fake.url(),
                        owner=user,
                    )
                    lessons.append(lesson)

        # Создаем 20 рандомных платежей
        for i in range(20):
            user = random.choice(users)
            payment_date = fake.date_between(start_date='-30d', end_date='today')
            payment_amount = Decimal(random.uniform(10, 100))
            payment_method = random.choice(['cash', 'transfer'])

            is_course = random.choice([True, False])
            course_or_lesson = random.choice(courses) if is_course else random.choice(lessons)

            Payment.objects.create(
                user=user,
                payment_date=payment_date,
                course=course_or_lesson if is_course else None,
                lesson=course_or_lesson if not is_course else None,
                payment_amount=payment_amount,
                payment_method=payment_method,
            )
