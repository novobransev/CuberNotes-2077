# Generated by Django 4.1 on 2022-11-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_page', '0006_alter_notes_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='descriptions',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='important',
            field=models.BooleanField(blank=True, verbose_name='Важно'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Заголовок'),
        ),
    ]
