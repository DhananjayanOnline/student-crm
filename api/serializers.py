from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StudentsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    course = serializers.CharField(read_only=True)

    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('user')
        course = self.context.get('course')
        return Students.objects.create(**validated_data, user=user, course=course)


class CoursesSerialier(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Courses
        fields = '__all__'


class BatchesSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    course = serializers.CharField(read_only=True)

    class Meta:
        model = Batches
        fields = '__all__'

    def create(self, validated_data):
        course = self.context.get('course')
        return course.batches_set.create(**validated_data)


class PlacementsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    student = serializers.CharField(read_only=True)

    class Meta:
        model = Placements
        fields = '__all__'

    def create(self, validated_data):
        student = self.context.get('student')
        return student.placements_set.create(**validated_data)
