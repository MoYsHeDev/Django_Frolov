# Generated by Django 3.2.7 on 2021-09-28 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=40, unique=True)),
                ('discipline', models.CharField(blank=True, default='Programming', max_length=40, null=True)),
                ('curator', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='teachers.teacher')),
                ('headman', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('students', models.ManyToManyField(blank=True, default=None, max_length=10, related_name='students_in_group', to='students.Student')),
            ],
        ),
    ]
