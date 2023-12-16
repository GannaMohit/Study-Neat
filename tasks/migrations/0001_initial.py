# Generated by Django 4.1.2 on 2023-12-16 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Assignment', 'Assignment'), ('Reading', 'Reading'), ('Quiz', 'Quiz'), ('Exam', 'Exam')], max_length=64)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('difficulty', models.IntegerField()),
                ('estimated_time', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='courses.course')),
            ],
        ),
    ]
