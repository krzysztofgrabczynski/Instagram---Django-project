# Generated by Django 4.1.5 on 2023-01-30 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0008_alter_userprofile_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_post",
                to="main.post",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
