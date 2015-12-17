# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_recipient_personalized_greeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='family_relationship',
            field=models.CharField(default=b"#davethecat's third-favorite", max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='personalized_greeting',
            field=models.TextField(default=b'Merry Christmas!'),
        ),
    ]
