# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.timezone import datetime
from datetime import date
# Create your models here.
class Site(models.Model):
	directory = models.CharField(max_length=250)
	folder = models.CharField(max_length=100)

	def __str__(self):
		return '{}'.format(self.folder)

	def get_FullPath(self):
		return '{}/{}/*'.format(self.directory, self.folder)

class Files(models.Model):
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	date = models.DateField(default=date.today)

	unique_together = ('site', 'name')

	def __str__(self):
		return '{} {} at {}'.format(self.site, self.name, self.date)

class Data(models.Model):
	file = models.ForeignKey(Files, on_delete=models.CASCADE)
	volt = models.FloatField(null=True, blank=True, default=0)
	level = models.FloatField(null=True, blank=True, default=0)
	datetime = models.DateTimeField()

	unique_together = ('datetime', 'volt', 'level')

	def __str__(self):
		return '{} {} {} at {}'.format(self.file, self.volt, self.level, self.datetime.strftime("%d-%m-%Y %I:%M %p"))
