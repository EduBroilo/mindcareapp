from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'appointments'

router = routers.DefaultRouter()
router.register('', views.AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls) )
]