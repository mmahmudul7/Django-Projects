# Generated by Django 5.1.5 on 2025-02-01 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_taskdetail_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.project'),
        ),
    ]
