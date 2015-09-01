# Encoding: utf-8
from django.db import models

# Create your models here.
class Membermodel(models.Model):
    name = models.CharField(max_length=200,verbose_name='Name')
    rank = models.CharField(max_length=200,verbose_name='Rang')
    since = models.DateTimeField(verbose_name='Seit wann dabei?')
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='Mitglied'
        verbose_name_plural='Mitglieder'

# EOF models.py
