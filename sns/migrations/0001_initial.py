# Generated by Django 3.0.8 on 2020-07-22 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'hashtags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('thumbnail_img', models.URLField(max_length=2000)),
                ('modal_video', models.URLField(max_length=2000, null=True)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.URLField(max_length=2000)),
                ('official', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='PostHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.Hashtag')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.Post')),
            ],
            options={
                'db_table': 'posts_hashtags',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.Staff'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='posts',
            field=models.ManyToManyField(through='sns.PostHashtag', to='sns.Post'),
        ),
    ]
