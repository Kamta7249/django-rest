# Generated by Django 5.0.1 on 2024-01-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='sal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]