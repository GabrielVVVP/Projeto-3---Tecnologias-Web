# Generated by Django 3.2 on 2021-05-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='gabriel', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='gabrielvvvp@gmail.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='93839421', max_length=200),
        ),
    ]