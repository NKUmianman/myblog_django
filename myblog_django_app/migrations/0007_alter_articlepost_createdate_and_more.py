# Generated by Django 4.1 on 2023-08-03 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myblog_django_app", "0006_articlepost_delete_articleinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlepost",
            name="createDate",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name="articlepost",
            name="updateDate",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
