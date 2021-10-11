from django.contrib import admin
from shared.models import Faith
# Register your models here.

@admin.register(Faith)
class FaithAdmin(admin.ModelAdmin):
    list_display = ('bornagain',)