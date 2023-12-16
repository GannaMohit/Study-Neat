# Generated by Django 4.1.2 on 2023-12-16 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weeks', to='courses.semester'),
        ),
    ]
