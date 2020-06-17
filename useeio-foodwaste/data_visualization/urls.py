# urls.py (data_visualization)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of urls for data_visualization."""

from datetime import datetime
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.contrib import admin
from data_visualization import views


urlpatterns = [
    url(r'^$', views.index, name='data_visualization'),
]
