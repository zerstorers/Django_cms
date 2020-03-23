from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import TeamListPluginModel


@plugin_pool.register_plugin
class TeamListPlugin(CMSPluginBase):
    model = TeamListPluginModel
    name = "teamlist"
    render_template = "teamlist.html"
