# Generated by Django 2.2.11 on 2021-08-04 18:58

import crud.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20210805_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_updatedat',
            field=crud.models.AutoDateTimeField(default=datetime.datetime(2021, 8, 4, 18, 58, 57, 953594, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='user_created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 18, 58, 57, 953594, tzinfo=utc)),
        ),
    ]
