# Generated by Django 5.1.5 on 2025-02-25 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.project'),
        ),
    ]
