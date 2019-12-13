from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import Hello
from krynncal.moon_magic import Moon_Magic
from krynncal.models import CampaignDate
from krynncal.krynndatetime import datetime as kdatetime, timedelta as ktimedelta
from kthrone.models import NonPlayerCharacter
import os
import re

class HelloPlugin(CMSPluginBase):
    model = Hello
    name = _("Hello Plugin")
    render_template = "hello_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(HelloPlugin)


class AllEntriesPlugin(CMSPluginBase):
    name = _("All Log Entries")
    render_template = "log_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(AllEntriesPlugin)


class DiscordNPCChatter(CMSPluginBase):
    name = _("Discord NPC Chatter")
    render_template = "krynn_npc_discord_hook.html"

    def render(self, context, instance, placeholder):
        npcs = NonPlayerCharacter.objects.all()
        context['instance'] = instance
        context['npcs'] = npcs
        return context


plugin_pool.register_plugin(DiscordNPCChatter)


class MoonMagicPlugin(CMSPluginBase):
    name = _("Krynn Moon Magic Plugin")
    render_template = "krynn_moon_magic.html"
    model = Hello
    cache = False

    def render(self, context, instance, placeholder):
        campaign_date = CampaignDate.objects.get(
            id=1).current_date
        one_day = ktimedelta(days=1)
        view_date = campaign_date.isoformat()[1:]
        prev_date = (campaign_date - one_day).isoformat()[1:]
        next_date = (campaign_date + one_day).isoformat()[1:]
        fordate = context['request'].GET.get(
            'date', campaign_date)
        use_default = True
        if type(fordate) is not kdatetime:
            use_default = False
            view_date = fordate
            re_dt = re.compile(
                r'(\d{3})-(\d{1,2})-(\d{1,2})'
                r'(?:[T ](\d{1,2})(?::(\d{1,2}))?(?::(\d{1,2}))?)?')
            fordate = tuple([
                int(term) for term in re_dt.match(fordate).groups() if term])
            prev_date = (kdatetime(*fordate) - one_day).isoformat()[1:]
            next_date = (kdatetime(*fordate) + one_day).isoformat()[1:]
        reveal_file = (
            os.path.isfile(
                '/home/www-data/webapps/allegiance/'
                'public/reveal/reveal-{}.png'.format(view_date)) and
            (use_default or kdatetime(*fordate) < campaign_date))
        context['instance'] = instance
        context['moon_magic'] = Moon_Magic(fordate)
        context['view_date'] = view_date.replace('T', ' ')
        context['reveal_file'] = reveal_file
        context['prev_date'] = prev_date.replace('T', ' ')
        context['next_date'] = next_date.replace('T', ' ')
        return context


plugin_pool.register_plugin(MoonMagicPlugin)

