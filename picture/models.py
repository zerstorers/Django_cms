# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cms.models.pluginmodel import CMSPlugin

# Create your models here.
class PicturePluginModel(models.Model):
    image = models.ImageField()
    title = models.CharField(null=True , max_length=255)
    description = models.CharField(null=True , max_length=255)

class PictureListPluginModel(CMSPlugin):
    pictures = models.ManyToManyField(PicturePluginModel)

    def copy_relations(self, oldinstance):
        self.pictures.set(oldinstance.pictures.all())


