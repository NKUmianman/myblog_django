# Generated by Django 4.1 on 2023-09-03 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog_django_app", "0026_friendsinfo_img_friendsinfo_intro_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postinfo",
            name="createTime",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 3, 20, 35, 19, 88332),
                verbose_name="时间",
            ),
        ),
    ]
