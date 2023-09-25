from django.contrib import admin

from .models import Course, Rating,University,Porfessor,Student,Comments,Recourses

admin.site.register(Course)
admin.site.register(Rating)
admin.site.register(University)
admin.site.register(Porfessor)
admin.site.register(Student)
admin.site.register(Comments)
admin.site.register(Recourses)

