from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassViewSet, BookViewSet, AudioViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'books', BookViewSet)
router.register(r'audios', AudioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
