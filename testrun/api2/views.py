from django.shortcuts import render
from rest_framework import generics
from schools.models import Client
from .serializers import ClientSerializer
# Create your views here.

class APIView1(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class APIView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer