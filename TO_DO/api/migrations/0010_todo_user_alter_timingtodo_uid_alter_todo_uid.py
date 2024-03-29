# Generated by Django 5.0.1 on 2024-02-06 05:50

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_timingtodo_uid_alter_todo_uid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d04e0887-3370-4dd0-980d-db9c81b7f766'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d04e0887-3370-4dd0-980d-db9c81b7f766'), editable=False, primary_key=True, serialize=False),
        ),
    ]
