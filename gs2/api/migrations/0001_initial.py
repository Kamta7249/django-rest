# Generated by Django 5.0.1 on 2024-01-30 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
