# Generated by Django 4.1.2 on 2023-11-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_semester_task_alter_course_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='subject',
        ),
        migrations.AlterField(
            model_name='course',
            name='nickname',
            field=models.CharField(max_length=32),
        ),
    ]
