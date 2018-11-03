# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.timezone import datetime
from datetime import date
# Create your models here.
class Site(models.Model):
	site_id = models.IntegerField(default=0)
	directory = models.CharField(max_length=250)
	folder = models.CharField(max_length=100)

	def __str__(self):
		return '{} id {}/{}'.format(self.site_id, self.directory, self.folder)	

class Files(models.Model):
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	date = models.DateField(default=date.today)

	def __str__(self):
		return '{} at {}'.format(self.name, self.date)

class Data(models.Model):
	file = models.ForeignKey(Files, on_delete=models.CASCADE)
	volt = models.FloatField(null=True, blank=True, default=0)
	level = models.FloatField(null=True, blank=True, default=0)
	datetime = models.DateTimeField()

	def __str__(self):
		return '{} volt={} level={} at {}'.format(self.file, self.volt, self.level, self.datetime)
