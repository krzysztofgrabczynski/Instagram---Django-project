# Generated by Django 4.1.5 on 2023-01-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1),
        ),
    ]
