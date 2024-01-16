from django.urls import path
from rest_framework import routers

from education.apps import EducationConfig
from education.views.course import CourseViewSet
from education.views.lesson import (LessonListView, LessonCreateView, LessonDetailView,
                                    LessonUpdateView, LessonDeleteView)


app_name = EducationConfig.name


urlpatterns = [
    path('', LessonListView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('<int:pk>/update/', LessonUpdateView.as_view()),
    path('<int:pk>/delete/', LessonDeleteView.as_view()),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
