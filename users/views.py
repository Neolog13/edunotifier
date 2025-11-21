from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout, authenticate
from .serializers import UserRegistrationSerializer, UserProfileSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Регистрация через API"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        return Response({
            'message': 'Регистрация успешна',
            'user': UserProfileSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Вход через API"""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({
            'message': 'Вход успешен',
            'user': UserProfileSerializer(user).data
        })
    return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Выход через API"""
    logout(request)
    return Response({'message': 'Выход успешен'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    """Профиль пользователя"""
    return Response(UserProfileSerializer(request.user).data)
