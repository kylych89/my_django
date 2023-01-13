# Generated by Django 4.1.5 on 2023-01-13 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
        ('student', '0002_faculty_alter_student_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty'),
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
    ]