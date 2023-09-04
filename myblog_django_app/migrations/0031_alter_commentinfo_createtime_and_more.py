# Generated by Django 4.1 on 2023-09-04 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog_django_app", "0030_alter_commentinfo_createtime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentinfo",
            name="createTime",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 4, 16, 9, 47, 496123),
                verbose_name="时间",
            ),
        ),
        migrations.AlterField(
            model_name="postinfo",
            name="createTime",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 9, 4, 16, 9, 47, 492076),
                verbose_name="时间",
            ),
        ),
    ]
