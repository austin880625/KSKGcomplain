# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Submissions', '0002_submission_submit_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('submit_type', models.IntegerField(default=0)),
                ('post_id', models.IntegerField()),
                ('fb_post_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('reporter', models.CharField(default='S', choices=[('S', 'Submitter'), ('R', 'Related'), ('F', 'Friend'), ('O', 'Other')], max_length=10)),
                ('reason', models.TextField()),
                ('post_hashtag', models.IntegerField()),
                ('fb_post_id', models.TextField()),
            ],
        ),
    ]
