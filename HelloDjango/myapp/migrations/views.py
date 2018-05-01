# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
	return HttpResponse("Hello world")

# Create your views here.
