# Encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from Firmenseite.Member.models import *

def index(request):
    member = Membermodel.objects.all().order_by('since')
    return render_to_response('Member/index.html',locals())

# EOF views.py