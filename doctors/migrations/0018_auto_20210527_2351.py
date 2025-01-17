# Generated by Django 3.2 on 2021-05-27 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0017_user_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(max_length=200)),
                ('diseases', models.CharField(blank=True, max_length=500, null=True)),
                ('nota', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='additional',
        ),
        migrations.RemoveField(
            model_name='user',
            name='consultas',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nota',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usertype',
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.user')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('eventtype', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.user'),
        ),
    ]
