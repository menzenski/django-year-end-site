# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_recipient_family_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='personalized_greeting',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
