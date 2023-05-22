# Generated by Django 4.1.5 on 2023-01-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_userprofile_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_img",
            field=models.ImageField(
                blank=True,
                default="profile_imgs/default_male.jpg",
                null=True,
                upload_to="profile_imgs",
            ),
        ),
    ]
