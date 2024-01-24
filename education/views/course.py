from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from education.models import Course
from education.permissions import IsOwner, IsMember, IsModerator
from education.serializers.course import CourseListSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsMember]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated, IsModerator | IsMember]
        elif self.action == 'retrieve' or self.action == 'update':
            permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in permission_classes]

