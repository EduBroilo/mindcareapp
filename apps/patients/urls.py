from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'patients'

router = routers.DefaultRouter()
router.register('', views.PatientViewSet, basename='patients')

urlpatterns = [
    path('', include(router.urls) )
]
