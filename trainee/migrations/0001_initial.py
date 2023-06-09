# Generated by Django 4.2.1 on 2023-05-28 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trainee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField(max_length=20)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
        ),
    ]
