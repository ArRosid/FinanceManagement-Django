# Generated by Django 3.0.4 on 2020-03-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20200304_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='source',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='credit',
            old_name='destination',
            new_name='wallet',
        ),
        migrations.RenameField(
            model_name='debit',
            old_name='source',
            new_name='wallet',
        ),
    ]
