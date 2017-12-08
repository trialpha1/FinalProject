
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Race(models.Model):
	Name = models.CharField(max_length=100)
	picture =  models.CharField(max_length=250, default='')
    
	def __unicode__(self):
		return unicode(self.Name)

class Class(models.Model):
	Name = models.CharField(max_length=100)
	picture = models.CharField(max_length=250, default='')
	
	def __unicode__(self):
		return unicode(self.Name)

