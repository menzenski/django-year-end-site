# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='family_relationship',
            field=models.CharField(default=b"#davethecat's third-favorite", max_length=200, null=True, blank=True),
        ),
    ]
