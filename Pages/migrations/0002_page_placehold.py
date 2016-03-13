# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='placehold',
            field=models.CharField(default='YEE?', max_length=30),
        ),
    ]
