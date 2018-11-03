from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import timedelta, date, datetime
from celery.task import periodic_task
import glob
import os
import csv

from .models import *

def readCSV(site, f):
	print("csv file is", f)
	with open(f, 'rb') as csvfile:
		fl = True
		spamreader = csv.reader(csvfile, delimiter=str(u',').encode('utf-8'), quotechar=str(u'|').encode('utf-8'))
		for row in spamreader:
			if fl:
				fl = False
				continue	
			InsertData(site,f, row)


def InsertData(site, file, row):
	try:
		dt = datetime.strptime(row[0], "%d-%m-%Y %H:%M:%S")
	except Exception as e:
		return e
	if not Files.objects.filter(site=site, name=file).exists():
		fl = Files.objects.create(site=site, name=file)
		fl.save()
	else:
		fl = Files.objects.get(site=site, name=file)

	print("file object", fl)

	if not Data.objects.filter(datetime=dt).exists():
		try:
			row[1] = float(row[1])
		except:
			row[1] = 0
		try:
			row[2] = float(row[2])
		except:
			row[2] = 0
		dt = Data.objects.create(file=fl, volt=row[1], level=row[2], datetime=dt)
		dt.save()

def getTodayTagFile():
	today = date.today()
	file = 'tag{:02d}{:02d}{}.csv'.format(today.day, today.month, today.year)
	return file

def ReadTagFile(s, file):
	path = s.get_FullPath()
	csv_file = '{}/{}/{}'.format(s.directory,s.folder, file)
	print("gettng file ",csv_file)
	if not os.path.isfile(csv_file):
 		raise Exception('Path does not exists')
	return csv_file

@periodic_task(run_every=timedelta(seconds=20))
def ReadFileAndStore():
	st = Site.objects.all()
	for s in st:
		file = getTodayTagFile()
		try:
			csv_file = ReadTagFile(s, file)
		except Exception as e:
			print(e)
			continue
		if csv_file:
			row = readCSV(s, csv_file)
