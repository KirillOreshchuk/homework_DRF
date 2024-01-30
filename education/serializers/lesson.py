from rest_framework import serializers

from education.models import Lesson
from education.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [UrlValidator(video_url='video_url')]

    class Meta:
        model = Lesson
        fields = '__all__'
