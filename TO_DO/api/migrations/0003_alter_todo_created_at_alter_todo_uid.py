# Generated by Django 5.0.1 on 2024-02-05 10:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('51332091-2548-422e-a261-a60fabc95a71'), editable=False, primary_key=True, serialize=False),
        ),
    ]
