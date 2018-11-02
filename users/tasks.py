from __future__ import absolute_import, unicode_literals
from celery import shared_task

from datetime import timedelta

# CELERYBEAT_SCHEDULE = {
#     "runs-every-5-seconds": {
#         "task": "tasks.add",
#         "schedule": timedelta(seconds=30),
#         "args": (16, 16)
#     },
# }

import glob
import os

from celery.task import periodic_task

from .models import *

def getFile(s):
    path = s.get_FullPath()
    print("path is", path)
    list_of_files = glob.glob('{}.csv'.format(path)) # * means all if need specific format then *.csv
    print("list of files", list_of_files)
    if list_of_files != []:
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

@periodic_task(run_every=timedelta(seconds=30))
def ReadFileAndStore():
    st = Site.objects.all()
    for s in st:
        f = getFile(s)
        print("file is", f)