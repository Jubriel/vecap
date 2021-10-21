from django.urls import path
from .views import APIView1, APIView2

urlpatterns = [
    path('', APIView1.as_view()),
    path('', APIView2.as_view()),
]