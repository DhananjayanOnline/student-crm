from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import action

class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

class CourseView(ModelViewSet):
    serializer_class = CoursesSerialier
    queryset = Courses.objects.all()
    permission_classes = [permissions.IsAdminUser]


class BatchView(ModelViewSet):
    serializer_class = BatchesSerializer
    queryset = Batches.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        course_id = request.query_params.get('course')
        course = Courses.objects.get(id=course_id)
        serializer = BatchesSerializer(
            data=request.data, context={'course': course})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class StudentView(ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        user_id = request.query_params.get('user')
        try:
            user=User.objects.get(id=user_id)
        except:
            return Response('No user in this User ID')
        course = Courses.objects.get(id=1)
        serializer = StudentsSerializer(data=request.data, context={
                                        'user': user, 'course': course})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=['GET'], detail=True)
    def add_batch(self, request, *args, **kwargs):
        student = self.get_object()
        batch_code = request.query_params.get('batch_code')
        try:
            batch = Batches.objects.get(batch_code=batch_code)
        except:
            return Response('No batch with this batch code')
        student.batchstudents_set.create(batch=batch)
        return Response('created')

    @action(methods=['POST'], detail=True)
    def add_placement(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = PlacementsSerializer(
            data=request.data, context={'student': student})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
