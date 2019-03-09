# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-10 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('is_chosen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('is_multiple', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(choices=[(b'en', 'English'), (b'tr', 'Turkish')], max_length=5)),
                ('uid', models.PositiveIntegerField()),
                ('participant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey')),
            ],
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.ChoiceQuestion'),
        ),
    ]