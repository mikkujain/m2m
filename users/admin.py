# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Site, Files, Data

admin.site.register(Site)
admin.site.register(Files)
admin.site.register(Data)

# Register your models here.
