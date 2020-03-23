# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.
class TeamPluginModel(models.Model):
    first_name = models.CharField(null=True , max_length=100)
    last_name = models.CharField(null=True , max_length=100)
    role = models.CharField(null=True , max_length=100)
    picture  = models.ImageField()
    linkedink = models.CharField(null=True , max_length=255)
    facebook = models.CharField(null=True , max_length=255)
    twitter = models.CharField(null=True , max_length=100)

class TeamListPluginModel(CMSPlugin):
    teams = models.ManyToManyField(TeamPluginModel)

    def copy_relations(self, oldinstance):
        self.teams.set(oldinstance.teams.all())
