from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from . models import TimeLinePluginModel


@plugin_pool.register_plugin
class TimelinePlugin(CMSPluginBase):
    model = TimeLinePluginModel
    name = "Une super timeline"
    render_template = "timeline.html"
