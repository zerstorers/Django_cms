# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(null=True , max_length=100)
    evenement = models.CharField(null=True , max_length=255)
    date = models.DateTimeField(null=True)
    picture  = models.ImageField()

from cms.models.pluginmodel import CMSPlugin
class TimeLinePluginModel(CMSPlugin):
    text = models.CharField(null=True , max_length=100)
    events = models.ManyToManyField(Event)

    def copy_relations(self, oldinstance):
        self.events.set(oldinstance.events.all())