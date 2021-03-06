# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_information', models.TextField(verbose_name='Speaker_information')),
                ('title', models.TextField(verbose_name='Speech Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('audience', models.TextField(verbose_name='Audience')),
                ('skill_level', models.PositiveIntegerField(choices=[(1, 'everyone'), (2, 'novice'), (3, 'intermediate'), (4, 'advanced')], default=1, verbose_name='Skill level required')),
                ('notes', models.TextField(blank=True, verbose_name='Notes for audience')),
            ],
        ),
        migrations.CreateModel(
            name='SpeechType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='speech',
            name='speech_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposal.SpeechType', verbose_name='Speech Type'),
        ),
        migrations.AddField(
            model_name='speech',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposal.Topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='speech',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
