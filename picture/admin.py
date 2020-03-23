# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PicturePluginModel

# Register your models here.
@admin.register(PicturePluginModel)
class PicturePluginModelAdmin(admin.ModelAdmin):
    list_display = ['title']

