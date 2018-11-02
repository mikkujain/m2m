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

from celery.task import periodic_task

@periodic_task(run_every=timedelta(seconds=30))
def every_30_seconds():
    print("Hello Sachin how r u")