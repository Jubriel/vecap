# Generated by Django 3.2.7 on 2021-10-20 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='domanin_url',
            new_name='domain_url',
        ),
    ]