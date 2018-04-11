# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20180410_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='url_larga',
            new_name='url_original',
        ),
    ]
