# Generated by Django 2.0.4 on 2018-05-03 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='course',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='course',
            name='listcontent',
        ),
        migrations.RemoveField(
            model_name='course',
            name='listheader',
        ),
        migrations.RemoveField(
            model_name='course',
            name='objectives',
        ),
        migrations.RemoveField(
            model_name='course',
            name='objtext',
        ),
        migrations.RemoveField(
            model_name='course',
            name='target',
        ),
    ]
