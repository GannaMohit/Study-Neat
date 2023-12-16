# Generated by Django 4.1.2 on 2023-12-16 08:53

from django.db import migrations, models
import django.db.models.deletion
import schedule.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('semester', models.ForeignKey(default=schedule.models.get_current_week, on_delete=django.db.models.deletion.CASCADE, related_name='weeks', to='courses.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Week_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='week_task', to='tasks.task')),
                ('week', models.ForeignKey(default=schedule.models.get_current_week, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='schedule.week')),
            ],
        ),
        migrations.CreateModel(
            name='Today_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('completed', models.BooleanField()),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='today_task', to='tasks.task')),
            ],
        ),
    ]
