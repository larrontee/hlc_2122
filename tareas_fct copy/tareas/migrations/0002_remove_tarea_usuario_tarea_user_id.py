# Generated by Django 4.0.2 on 2022-02-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='usuario',
        ),
        migrations.AddField(
            model_name='tarea',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
    ]
