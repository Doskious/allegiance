from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PorViewerApphook(CMSApp):
    name = _("PorViewer Apphook")
    urls = ["pathpor.urls"]

apphook_pool.register(PorViewerApphook)