# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0002_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=512)),
                ('score', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField()),
                ('question', models.ForeignKey(to='question_answer.Question')),
            ],
        ),
    ]
