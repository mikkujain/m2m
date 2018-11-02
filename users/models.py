# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.timezone import datetime
from datetime import date
# Create your models here.
class Site(models.Model):
	directory =models.CharField(max_length=250)
	folder = models.CharField(max_length=100)

	def __str__(self):
		return self.directory	

class Files(models.Model):
	site = models.ForeignKey(Site)
	date = models.DateField(default=date.today)

	def __str__(self):
		return '{}/{}'.format(self.site, self.date)

class Data(models.Model):
	file =models.ForeignKey(Files)
	volt = models.FloatField()
	level =models.FloatField()
	datetime = models.DateTimeField()

	def __str__(self):
		return '{} {} {} {}'.format(self.file, self.volt, self.level, self.datetime)
