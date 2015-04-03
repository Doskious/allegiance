from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import CharSheet

class CharPlugin(CMSPluginBase):
    model = CharSheet
    name = _("Character Stat Block")
    render_template = "char_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(CharPlugin)
