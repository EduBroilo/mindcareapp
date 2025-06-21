from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'therapists'

router = routers.DefaultRouter()
router.register('', views.TherapistViewSet, basename='therapists')

urlpatterns = [
    path('', include(router.urls) )
]
