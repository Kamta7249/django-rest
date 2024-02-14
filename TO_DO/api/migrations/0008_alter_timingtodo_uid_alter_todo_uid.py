# Generated by Django 5.0.1 on 2024-02-06 05:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('23ffc8db-3887-475b-a452-e15e23150ec2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('23ffc8db-3887-475b-a452-e15e23150ec2'), editable=False, primary_key=True, serialize=False),
        ),
    ]