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

today = date.today()

def Home(request):
    return render(request, 'home.html')


class Dashboard(LoginRequiredMixin, ListView):
    model = (Site, Files, Data)
    template_name = "users/dashboard.html"
    login_url = '/'

    def get_queryset(self):
		queryset = Data.objects.all()
		print(queryset)
		return queryset

    def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)

		startd = self.request.GET.get('start-date')
		endd   = self.request.GET.get('end-date')
		if self.request.GET.get('date'):
			try:
				today = datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d').date()
				context["data_list"] = context["data_list"].filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
				dv = Site.objects.all()
				context["device1"]   = context["data_list"].filter(file__site=dv[0])
				context["device2"] 	 = context["data_list"].filter(file__site=dv[1])
			except Exception as e:
				context['errors'] = ["Invalid Date Format Selected"]
		elif startd and endd:
			try:
				startd = datetime.strptime(startd, '%Y-%m-%d').date()
				endd = datetime.strptime(endd, '%Y-%m-%d').date()
				context["data_list"] = context["data_list"].filter(datetime__date__range=[startd, endd])
				dv = Site.objects.all()
				context["device1"]   = context["data_list"].filter(file__site=dv[0])
				context["device2"] 	 = context["data_list"].filter(file__site=dv[1])
			except Exception as e:
				context['errors'] = ["Invalid Date Format Selected"]
		else:
			today = datetime.today()
			context["data_list"] = context["data_list"].filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
			dv = Site.objects.all()
			context["device1"] = context["data_list"].filter(file__site=dv[0])
			context["device2"] = context["data_list"].filter(file__site=dv[1])

		# # print(context)
		# if self.request.GET.get('date'):
		# 	try:
		# 		today = datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d').date()
		# 		context["data_list"] = context["data_list"].filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
		# 		# print(context['data_list'])
		# 		dv = Site.objects.all()
		# 		# print(dv)
		# 		print(context['data_list'])
		# 		context["device1"]   = context["data_list"].filter(file__name=dv[0].name)
		# 		context["device2"] 	 = context["data_list"].filter(file__name=dv[1])
		# 		print("context is ", context['device1'])
		# 	except Exception as e:
		# 		context['errors'] = ["Invalid Date Format Selected"]

		# return context

		data = []
		data1 = []
		r1 = []
		r2 = []
		r3 = []
		r4 = []
		if context['device1']:
			data = [['DateTime', 'Water_Level']]
			for i in context['device1']:
				data.append([i.datetime.strftime("%d/%m/%y %H:%I %p"), i.level])
			chart = gchart.ColumnChart(SimpleDataSource(data=data), options={'title': 'NHPC_Sewa'}, height=400, width=600)
			context["chart"] = chart
		# return context

		if context['device2']:
			data1 = [['DateTime','Water_Level']]
			for i in context['device2']:
				data1.append([i.datetime.strftime("%d/%m/%y %H:%I %p"),i.level])
			chart1 = gchart.ColumnChart(SimpleDataSource(data=data1), options={'title': 'NHPC_Sewa'}, height=400, width=600)
			context["chart1"] = chart1

		# if context['device3']:
		r1 = [['DateTime', 'Rain_Fall']]
		for i in range(5):
			r1.append([0, 0])
		chart2 = gchart.ColumnChart(SimpleDataSource(data=r1), options={'title': 'NHPC_Sewa'}, height=400, width=600)
		context["chart2"] = chart2


		# if context['device4']:
		r2 = [['DateTime', 'Rain_Fall']]
		for i in range(5):
			r2.append([0,0])
		chart3 = gchart.ColumnChart(SimpleDataSource(data=r2), options={'title': 'NHPC_Sewa'}, height=400, width=600)
		context["chart3"] = chart3

		# if context['device5']:
		r3 = [['DateTime', 'Rain_Fall']]
		for i in range(5):
			r3.append([0,0])
		chart4 = gchart.ColumnChart(SimpleDataSource(data=r3), options={'title': 'NHPC_Sewa'}, height=400, width=600)
		context["chart4"] = chart4

		# if context['device6']:
		r4 = [['DateTime', 'Rain_Fall']]
		for i in range(5):
			r4.append([0,0])
		chart5 = gchart.ColumnChart(SimpleDataSource(data=r4), options={'title': 'NHPC_Sewa'}, height=400, width=600)
		context["chart5"] = chart5

		return context		
