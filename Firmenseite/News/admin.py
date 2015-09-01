# Encoding: utf-8
from Firmenseite.News.models import *
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News Titel',    {'fields': ['title']}),
        ('News Autor',    {'fields': ['author']}),
        ('Text',          {'fields': ['newstext']}),
        ('Datum',         {'fields': ['date']}),
    ]
    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Newsmodel, NewsAdmin)

# EOF admin.py
