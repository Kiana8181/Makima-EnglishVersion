from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class University(models.Model):
    user =models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    type=models.CharField(max_length=10,default='university')
    universityName = models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    phoneNumber=models.CharField(max_length=20)
    email=models.EmailField()
    logo=models.FileField(upload_to='logos/')

class Comments(models.Model):
    name=models.CharField(max_length=20)
    comment=models.TextField(max_length=1000)


class Recourses(models.Model):
    recours=models.FileField(upload_to='recourses/')

class Course(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    professorName = models.CharField(max_length=50)
    universityName = models.CharField(max_length=50)
    comments=models.ManyToManyField(Comments,blank=True)
    resourse=models.ManyToManyField(Recourses,blank=True)
    def no_of_ratings(self):
        ratings = Rating.objects.filter(course=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(course=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'course'),)
        index_together = (('user', 'course'),)

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    type = models.CharField(max_length=10, default='student')
    lastName = models.CharField(max_length=50)
    nationalId = models.CharField(max_length=20)
    email = models.EmailField()
    fieldOfStudy = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)
    studentNumber = models.CharField(max_length=20)
    university = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    favoriteCourse=models.ManyToManyField(Course,blank=True)


class Porfessor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=50)
    type = models.CharField(max_length=10, default='porfessor')
    lastName=models.CharField(max_length=50)
    records=models.CharField(max_length=300)
    email=models.EmailField()
    typeOfSpecialization=models.CharField(max_length=300)
    degreeOfEducation = models.CharField(max_length=300)
    university=models.CharField(max_length=50)
    encyclopedia=models.FileField(upload_to='encyclopedias/')
    profileImage=models.FileField(upload_to='profileImages/')
    verify=models.BooleanField(default=False)
    courses=models.ManyToManyField(Course,blank=True)

