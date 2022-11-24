from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions

class CourseView(ModelViewSet):
    serializer_class = CoursesSerialier
    queryset = Courses.objects.all()

    permission_classes = [permissions.IsAdminUser]


class StudentView(ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        course = Courses.objects.get(id=1)
        serializer = StudentsSerializer(data=request.data, context={'user':request.user, 'course': course})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)