# Encoding: utf-8
from Firmenseite.Member.models import *
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',             {'fields': ['name']}),
        ('Rang',             {'fields': ['rank']}),
        ('Seit wann dabei?', {'fields': ['since']}),
    ]
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Membermodel, MemberAdmin)

# EOF admin.py
