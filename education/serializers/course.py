from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from education.models import Course, Lesson
from education.serializers.lesson import LessonSerializer
from subscription.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        request = self.context.get('request')
        if request:
            return Subscription.objects.filter(user=request.user, course=course).exists()
        return False

    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons_count', 'subscription', 'lessons', 'owner', )
