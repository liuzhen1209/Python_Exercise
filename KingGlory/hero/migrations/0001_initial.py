# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GloryPracice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('dialogue', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('glory_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GlorySkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('skill_name', models.CharField(max_length=20)),
                ('skill_type', models.CharField(max_length=20)),
                ('skill_desc', models.CharField(max_length=1000)),
                ('glory', models.ForeignKey(to='hero.GloryPracice')),
            ],
        ),
    ]
