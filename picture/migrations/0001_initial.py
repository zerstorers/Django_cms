# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-23 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='picture_picturelistpluginmodel', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PicturePluginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='picturelistpluginmodel',
            name='pictures',
            field=models.ManyToManyField(to='picture.PicturePluginModel'),
        ),
    ]
