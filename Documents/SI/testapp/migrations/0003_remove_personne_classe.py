# Generated by Django 2.0.4 on 2018-04-15 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20180415_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personne',
            name='classe',
        ),
    ]
