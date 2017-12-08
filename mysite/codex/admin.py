# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from codex.models import Class, Race

# Register your models here.
class ClassAdmin(admin.ModelAdmin):
	list_display = ('Name', )
	
class RaceAdmin(admin.ModelAdmin):
	list_display = ('Name', )
	
admin.site.register(Class, ClassAdmin)
admin.site.register(Race, RaceAdmin)

