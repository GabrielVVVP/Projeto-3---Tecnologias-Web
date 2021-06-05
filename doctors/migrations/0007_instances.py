# Generated by Django 3.2 on 2021-05-22 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_alter_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=10000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.user')),
            ],
        ),
    ]
