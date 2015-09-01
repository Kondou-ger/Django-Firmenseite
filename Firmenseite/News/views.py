# Encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from Firmenseite.News.models import *

def index(request):
    article = Newsmodel.objects.all().order_by('-date')
    return render_to_response('News/index.html',locals())

def Newsview(request, source_id):
    article = get_object_or_404(Newsmodel, pk=source_id)
    return render_to_response('News/Artikel.html', locals())

# EOF views.py
