# Generated by Django 3.2 on 2021-05-31 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0023_references'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='References',
            new_name='Reference',
        ),
    ]