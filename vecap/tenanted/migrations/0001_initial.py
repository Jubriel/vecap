# Generated by Django 3.2.7 on 2021-10-05 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bornagain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.faith')),
            ],
        ),
    ]
