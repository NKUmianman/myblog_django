# Generated by Django 4.1 on 2023-08-03 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog_django_app", "0009_rename_articlepost_articleinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articleinfo",
            name="body",
            field=models.TextField(verbose_name="内容"),
        ),
        migrations.AlterField(
            model_name="articleinfo",
            name="createDate",
            field=models.DateField(default=datetime.date.today, verbose_name="创建日期"),
        ),
        migrations.AlterField(
            model_name="articleinfo",
            name="title",
            field=models.CharField(max_length=100, verbose_name="标题"),
        ),
        migrations.AlterField(
            model_name="articleinfo",
            name="updateDate",
            field=models.DateField(default=datetime.date.today, verbose_name="更新日期"),
        ),
    ]
