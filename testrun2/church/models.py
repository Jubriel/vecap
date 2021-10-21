from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Client(TenantMixin):
    schema_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=50, default='')
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

class Domain(DomainMixin):
    pass