# Generated by Django 4.1 on 2022-11-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_page', '0004_notes_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='task_complete',
            field=models.BooleanField(blank=True, default=False, verbose_name='Завершить задание'),
        ),
    ]
