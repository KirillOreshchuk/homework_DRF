from rest_framework.viewsets import ModelViewSet

from education.models import Course
from education.serializers.course import CourseListSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
