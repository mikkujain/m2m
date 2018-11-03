# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# from graphos.sources.simple import SimpleDataSource
# from graphos.renderers.gchart import LineChart

from django.contrib.auth.models import User

from users.models import *
from django.utils.timezone import datetime #important if using timezones
from django.db.models import Max, Min, Avg
from datetime import date, datetime
# from django.contrib.auth.mixins import LoginRequiredMixin

from graphos.sources.simple import SimpleDataSource
from graphos.renderers import gchart

def Home(request):
    return render(request, 'home.html')


class Dashboard(LoginRequiredMixin, ListView):
    model = (Site, Files, Data)
    template_name = "users/dashboard.html"
    login_url = '/'

    def get_queryset(self):
		queryset = Data.objects.all()
		# print(queryset)
		return queryset

    def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		startd = self.request.GET.get('start-date')
		endd = self.request.GET.get('end-date')
		if self.request.GET.get('date'):
			try:
				today = datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d').date()
				context["data_list"] = context["data_list"].filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
				dv = Files.objects.all()
				context["device1"]   = context["data_list"].filter(file__name=dv[0].name)
				context["device2"] 	 = context["data_list"].filter(file__name=dv[1])
				print("context is ", context['device1'])
			except Exception as e:
				context['errors'] = ["Invalid Date Format Selected"]

		return context