from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('admins', AdminViewSet)
router.register('teacher', TeacherViewSet)
router.register('student', StudentViewSet)


urlpatterns = [
    path('', include(router.urls))
]