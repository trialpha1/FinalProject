# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import loader, render
from django.http import HttpResponse
from .models import *

# Create your views here.
	
def home(request):
    classes = Class.objects.all()
    races = Race.objects.all()
    t = loader.get_template('home.html')
    c = dict({'Class': Class, 'Race': Race})
    return HttpResponse(t.render(c))    
def clas(request, Name):
    classes = Class.objects.filter(Name=Name)
    t = loader.get_template('class.html')
    c = dict({'classes': classes})
    return HttpResponse(t.render(c))
def race(request, Name):
    races = Race.objects.filter(Name=Name)
    t = loader.get_template('race.html')
    c = dict({'races': races})
    return HttpResponse(t.render(c))
def raceS(request):
    races = Race.objects.all()
    t = loader.get_template('race.html')
    c = dict({'races': races})
    return HttpResponse(t.render(c))
def clasS(request):
    classes = Class.objects.all()
    t = loader.get_template('class.html')
    c = dict({'classes': classes})
    return HttpResponse(t.render(c))