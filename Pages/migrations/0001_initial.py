# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(max_length=100)),
                ('access_token', models.CharField(max_length=300)),
                ('prefix', models.CharField(max_length=100)),
                ('post_count', models.IntegerField()),
            ],
        ),
    ]
