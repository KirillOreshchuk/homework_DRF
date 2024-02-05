from django.urls import path
from rest_framework import routers

from education.apps import EducationConfig
from education.views.course import CourseViewSet, CourseUpdateAPIview
from education.views.lesson import (LessonListView, LessonCreateView, LessonDetailView,
                                    LessonUpdateView, LessonDeleteView)


app_name = EducationConfig.name


urlpatterns = [
    path('', LessonListView.as_view(), name='lesson-list'),
    path('create/', LessonCreateView.as_view(), name='lesson-create'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson-delete'),

    path('courses/update/<int:pk>/', CourseUpdateAPIview.as_view(), name='course-update'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
