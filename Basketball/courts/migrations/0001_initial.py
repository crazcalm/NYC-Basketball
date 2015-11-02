# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('num_of_courts', models.IntegerField()),
                ('accessible', models.CharField(max_length=1)),
                ('longitude', models.TextField()),
                ('latitude', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
