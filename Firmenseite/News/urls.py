# Encoding: utf-8
from django.conf.urls.defaults import *

urlpatterns = patterns('Firmenseite.News.views',
    (r'^$','index'),
    (r'^index/$','index'), #Explizit ist besser, yadayada
    (r'^(?P<source_id>\d+)/$', 'Newsview'),
)

# EOF ddlseite.urls.py