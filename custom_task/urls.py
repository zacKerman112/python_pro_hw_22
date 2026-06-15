from django.urls import path
from .views import UserConfigListAPIView

urlpatterns = [
    path('my_endpoint/', UserConfigListAPIView.as_view(), name='endpoint'),
]