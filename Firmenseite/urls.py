#Encoding: utf-8
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include('Firmenseite.News.urls')), #Nehmen die News mal als Indexseite
    (r'^news/', include('Firmenseite.News.urls')), #Explizit ist immer besser …
    (r'^member/', include('Firmenseite.Member.urls'))
)
