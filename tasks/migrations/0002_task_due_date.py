# Generated by Django 4.1.2 on 2023-12-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2023-12-16'),
            preserve_default=False,
        ),
    ]