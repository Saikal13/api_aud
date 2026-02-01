from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework.response import Response
from .models import Teacher, Class, Book, Audio
from .serializers import TeacherSerializer, ClassSerializer, BookSerializer, AudioSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]



class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [AllowAny]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['author']
    ordering_fields = ['description']

    # сортировка по умолчанию




class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [AllowAny]

    ordering_fields = ['id', 'created_at']
    ordering = ['-id']



    def perform_create(self, serializer):
        # проверяем, что book_id передан
        book = self.request.data.get('book_id')
        if not book:
            raise ValidationError({"book_id": "Это поле обязательно."})
        serializer.save(book_id=book)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
