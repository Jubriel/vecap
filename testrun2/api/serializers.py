from django.db import models
from rest_framework import serializers
from church.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('schema_name','name', 'domain','created_on')