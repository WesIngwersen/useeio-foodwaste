# urls.py (useeio-foodwaste)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of urls for useeio-foodwaste."""

from datetime import datetime
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.contrib import admin
from useeio_foodwaste import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/?$', views.home, name='dashboard'),
    url(r'^contact/?$', views.contact, name='contact'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^lab_data/?$', views.lab_data, name='lab_data'),
    url(r'^sdmp/?$', views.sdmp, name='sdmp'),

    # Begin other module import URLs.
    url(r'^accounts/', include('accounts.urls')),
    url(r'^data_visualization/', include('data_visualization.urls')),
    url(r'^support/', include('support.urls')),
    url(r'^teams/', include('teams.urls')),
]
