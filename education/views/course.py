from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from education.models import Course
from education.paginators import CoursePaginator
from education.permissions import IsOwner, IsMember, IsModerator
from education.serializers.course import CourseListSerializer, CourseSerializer
from education.tasks import update_course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsMember]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated, IsModerator | IsMember]
        elif self.action == 'retrieve' or self.action == 'update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]


class CourseUpdateAPIview(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_update(self, serializer):
        description = serializer.save()
        update_course.delay()
