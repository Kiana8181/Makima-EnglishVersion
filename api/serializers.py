from rest_framework import serializers
from .models import Course, Rating,University,Porfessor,Student,Comments,Recourses
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'universityName','user','type','address','phoneNumber','email','logo')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'name', 'comment')

class RecourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recourses
        fields = ('id', 'recours')

class CourseSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,required=False)
    resourse=RecourseSerializer(many=True,required=False)
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'no_of_ratings', 'avg_rating','professorName','universityName','comments','resourse')

    def update(self, instance, validated_data):

        # Updating comments
        comments_data = validated_data.get('comments')
        instance.comments.clear()

        for comments_data in comments_data:
            comment = Comments.objects.get(**comments_data)
            instance.comments.add(comment)

        # Updating recourses
        resourse_data = validated_data.get('resourse')
        instance.resourse.clear()

        for resourse_data in resourse_data:
            resours= Recourses.objects.get(**resourse_data)
            instance.resourse.add(resours)

        # Updating other fields
        fields = [
            'name',
            'description',
            'professorName',
            'universityName',
        ]
        for field in fields:
            setattr(instance, field, validated_data[field])

        instance.save()
        return instance
class PorfessorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, required=False)
    class Meta:
        model = Porfessor
        fields = ('id', 'user','type','firstName','lastName','records','email','typeOfSpecialization','degreeOfEducation','university','encyclopedia','profileImage','verify','courses')
class StudentSerializer(serializers.ModelSerializer):
    favoriteCourse=CourseSerializer(many=True,required=False)
    class Meta:
        model = Student
        fields = ('id','user','firstName','lastName','nationalId','email','fieldOfStudy','phoneNumber','studentNumber','university','grade','favoriteCourse','type')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'course')