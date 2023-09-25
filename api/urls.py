from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import CourseViewSet, RatingViewSet, UserViewSet,UniversityViewSet,PorfessorViewSet,StudentViewSet,CommentViewSet,RecourseViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)
router.register('universities', UniversityViewSet)
router.register('porfessors', PorfessorViewSet)
router.register('students', StudentViewSet)
router.register('comments', CommentViewSet)
router.register('recourses', RecourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]