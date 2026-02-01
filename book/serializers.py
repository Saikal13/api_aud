from rest_framework import serializers
from .models import Teacher, Class, Book, Audio
from django.contrib.auth.models import User


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'bio', 'photo']


class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True
    )

    class Meta:
        model = Class
        fields = ['id', 'name', 'description', 'teacher', 'teacher_id']


class AudioSerializer(serializers.ModelSerializer):
    # book_id нужен для POST, чтобы избежать IntegrityError
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True
    )

    class Meta:
        model = Audio
        fields = ['id', 'book_id', 'title', 'audio_file', 'duration', 'uploaded_at']


class BookSerializer(serializers.ModelSerializer):
    audios = AudioSerializer(many=True, read_only=True)
    book_class = ClassSerializer(read_only=True)
    book_class_id = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(), source='book_class', write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'cover_image', 'description', 'book_class', 'book_class_id', 'audios']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user