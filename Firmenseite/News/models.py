# Encoding: utf-8
from django.db import models

# Create your models here.
class Newsmodel(models.Model):
    title = models.CharField(max_length=200,verbose_name='Titel')
    author = models.CharField(max_length=200,verbose_name='Autor')
    date = models.DateTimeField(verbose_name='Datum',)
    newstext = models.TextField(verbose_name='Text',)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name='News'
        verbose_name_plural='News'

# EOF models.py
