from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import PictureListPluginModel


@plugin_pool.register_plugin
class PictureListPluginModel(CMSPluginBase):
    model = PictureListPluginModel
    name = "picturelist"
    render_template = "picturelist.html"
