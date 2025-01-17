# Generated by Django 3.2 on 2021-05-30 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0018_auto_20210527_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instance',
            name='symptoms',
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.instance')),
            ],
        ),
    ]
