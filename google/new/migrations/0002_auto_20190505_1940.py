# Generated by Django 2.0.13 on 2019-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='introduction',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
