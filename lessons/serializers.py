from rest_framework import serializers
from .models import Lesson


class LessonWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'student', 'scheduled_at']
        read_only_fields = ['id']


class LessonReadSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.get_display_name', read_only=True)
    student_name = serializers.CharField(source='student.get_display_name', read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'status', 'scheduled_at', 'teacher_name', 'student_name']
        read_only_fields = ['teacher_name', 'status']
