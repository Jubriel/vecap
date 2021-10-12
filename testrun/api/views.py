from django.shortcuts import render
from rest_framework import generics
from student.models import Student
from .serializers import StudentSerializer
# Create your views here.

class APIView1(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class APIView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer