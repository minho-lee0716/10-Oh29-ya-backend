# Generated by Django 3.0.8 on 2020-07-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200726_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialorder',
            old_name='detail_image',
            new_name='background_image',
        ),
        migrations.RemoveField(
            model_name='specialorder',
            name='end',
        ),
        migrations.RemoveField(
            model_name='specialorder',
            name='start',
        ),
        migrations.RemoveField(
            model_name='specialorder',
            name='text',
        ),
        migrations.AddField(
            model_name='specialorder',
            name='subtitle',
            field=models.CharField(default=0, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialorder',
            name='time',
            field=models.CharField(default=0, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialorder',
            name='title',
            field=models.CharField(default=0, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]