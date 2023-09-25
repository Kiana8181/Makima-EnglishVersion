from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Course, Rating,University,Porfessor,Student,Comments,Recourses
from .serializers import CourseSerializer, RatingSerializer, UserSerializer,UniversitySerializer,PorfessorSerializer,StudentSerializer,CommentSerializer,RecourseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (AllowAny,)

class PorfessorViewSet(viewsets.ModelViewSet):
    queryset = Porfessor.objects.all()
    serializer_class = PorfessorSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['PATCH'])
    def add_course_porfessor(self, request, pk=None):
        if 'courseId' in request.data:

            courseId = request.data['courseId']
            course = Course.objects.get(id=courseId)
            porfessor=Porfessor.objects.get(id=pk)

            porfessor.courses.add(course)
            serializer = PorfessorSerializer(porfessor, many=False)
            response = {'message': 'courses updated', 'result': serializer.data }
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide courseId'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['PATCH'])
    def add_favorute_course(self, request, pk=None):
        if 'courseId' in request.data:

            courseId = request.data['courseId']
            course = Course.objects.get(id=courseId)
            student = Student.objects.get(id=pk)

            student.favoriteCourse.add(course)
            serializer = StudentSerializer(student, many=False)
            response = {'message': 'courses updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide courseId'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['PATCH'])
    def add_comment_resource_course(self, request, pk=None):
        if 'commentId' in request.data:

            commentId = request.data['commentId']
            comment = Comments.objects.get(id=commentId)
            course = Course.objects.get(id=pk)

            course.comments.add(comment)
            serializer = CourseSerializer(course, many=False)
            response = {'message': 'courses updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        elif 'resourseId' in request.data:

            resourseId = request.data['resourseId']
            resourse1 = Recourses.objects.get(id=resourseId)
            course = Course.objects.get(id=pk)

            course.resourse.add(resourse1)
            serializer = CourseSerializer(course, many=False)
            response = {'message': 'courses updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide commentId or resourseId'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def rate_course(self, request, pk=None):
        if 'stars' in request.data:
            if 'user' in request.data:

                course = Course.objects.get(id=pk)
                stars = request.data['stars']
                user = request.data['user']

                try:
                    rating = Rating.objects.get(user=user, course=course.id)
                    rating.stars = stars
                    rating.save()
                    serializer = RatingSerializer(rating, many=False)
                    response = {'message': 'Rating updated', 'result': serializer.data }
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    myUser=User.objects.get(id=user)
                    rating = Rating.objects.create(user=myUser, course=course, stars=stars)
                    serializer = RatingSerializer(rating, many=False)
                    response = {'message': 'Rating created', 'result': serializer.data}
                    return Response(response, status=status.HTTP_200_OK)

            else:
                response = {'message': 'You need to provide user'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

class RecourseViewSet(viewsets.ModelViewSet):
    queryset = Recourses.objects.all()
    serializer_class = RecourseSerializer
    permission_classes = (AllowAny,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (AllowAny,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
