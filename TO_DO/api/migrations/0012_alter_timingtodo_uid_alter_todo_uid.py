# Generated by Django 5.0.1 on 2024-02-06 06:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('ad0b565a-68d4-43d5-8424-c1da2cc7411b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('ad0b565a-68d4-43d5-8424-c1da2cc7411b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
