# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.timezone import datetime
from datetime import date
# Create your models here.

# def Site(models.Model):
# 	site_name =models.CharField(max_length=250)
# 	folder = models.CharField(max_length=100)

# 	def __str__(self):
# 		return self.site_name

# def Files(models.Model):
# 	file_name=models.ForeignKey(Site)
# 	date = models.DateField(default=date.today)

# 	def __str__(self):
# 		return self.file_name
	

# def Data(models.Model):
# 	data =models.ForeignKey(Files)
# 	volt = models.FloatField()
# 	level =models.FloatField()
# 	datetime = models.DateTimeField()

# 	def __str__(self):
# 		return voltage {} level {} .format( self.volt, self.level)

class Site(models.Model):
	site_name =models.CharField(max_length=250)
	folder = models.CharField(max_length=100)

	def __str__(self):
		return self.site_name	

class Files(models.Model):
	file_name=models.ForeignKey(Site)
	date = models.DateField(default=date.today)

	def __str__(self):
		return '{} {}'.format(self.file_name, self.date)

class Data(models.Model):
	data =models.ForeignKey(Files)
	volt = models.FloatField()
	level =models.FloatField()
	datetime = models.DateTimeField()

	def __str__(self):
		return '{} {} {}'.format(self.data, self.volt, self.level)
