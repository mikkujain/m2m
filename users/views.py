# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart

from django.contrib.auth.models import User

def Home(request):
    return render(request, 'home.html')


class Dashboard(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/dashboard.html"

