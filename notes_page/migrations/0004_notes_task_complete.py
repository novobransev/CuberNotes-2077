# Generated by Django 4.0.3 on 2022-10-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_page', '0003_remove_notes_user_notes_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='task_complete',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
