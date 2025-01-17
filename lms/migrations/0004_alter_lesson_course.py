# Generated by Django 5.1.3 on 2024-12-10 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0003_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите курс",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lms.course",
                verbose_name="Курс",
            ),
        ),
    ]
