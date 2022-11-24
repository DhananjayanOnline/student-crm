from rest_framework import serializers
from .models import *

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
        model = '__all__'

class PlacementsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    student = serializers.CharField(read_only=True)
    class Meta:
        model = Placements
        fields = '__all__'


