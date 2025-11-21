from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonReadSerializer, LessonWriteSerializer


class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()

    def get_queryser(self):
        return Lesson.objects.filter(teacher=self.request.user) | Lesson.objects.filter(student=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LessonWriteSerializer
        return LessonReadSerializer

    def create(self, request, *args, **kwargs):
        if request.user.user_type != 'teacher':
            return Response(
                {'error': 'Только преподаватели могут создавать уроки'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        lesson = self.get_object()

        if lesson.student != request.user:
            return Response(
                {'error': 'У вас нет доступа к этому уроку'}, 
                status=status.HTTP_403_FORBIDDEN
            )

        if lesson.confirm():
            return Response({'status': 'confirmed', 'message': 'Урок подтвержден'})
        return Response(
            {'error': 'Невозможно подтвердить урок'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
