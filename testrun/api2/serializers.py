from django.db import models
from rest_framework import serializers
from schools.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'description','created_on')