from django.conf.urls import *

urlpatterns = patterns('pathpor.views',
    url(r'^(?P<por_file>.+\.por)$', 'por_view', name='view_por'),
    url(r'^$', 'por_list', name='app_main'),
)