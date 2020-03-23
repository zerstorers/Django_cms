# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TeamPluginModel

# Register your models here.
@admin.register(TeamPluginModel)
class TeamPluginModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'role')
