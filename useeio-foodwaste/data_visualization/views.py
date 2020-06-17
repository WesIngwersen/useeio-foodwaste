# views.py (data_visualization)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of views for data_visualization module."""

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

from data_visualization.models import AVAILABLE_DATA, AVAILABLE_STATES
from data_visualization.utils import calc_color, plot_cities_data, \
    plot_map_fill_multiples_ids_tone, read_shapefile


@login_required
def index(request, *args, **kwargs):
    """
    Main page for the Data Visualization module. On this page, users should be
    able to select a US State (perhaps a subset of a state), select a parameter (or
    potentially multiple parameters), and generate maps of the selected parameters.
    """
    assert isinstance(request, HttpRequest)
    ctx = {'states': AVAILABLE_STATES, 'columns': AVAILABLE_DATA,
           'year': datetime.now().year}
    return render(request, 'data_visualization.html', ctx)


@login_required
def generate_map(request, *args, **kwargs):
    """
    Receives a POST from the main page of this module.
    Generates a map for the provided State and Datum (shp column header).
    """


@login_required
def ohio_map(request, *args, **kwargs):
    """Generate and return a matplotlib map of Ohio."""
    # 3. Initialize visualization set:
    sns.set(style="whitegrid", palette="pastel", color_codes=True)
    sns.mpl.rc("figure", figsize=(10,6))

    # 4. Open a vector shape map:
    shp_path = "./resources/Ohio/tl_2016_39_cousub.shp"
    sf = shp.Reader(shp_path)
    # try:
    #     sf = shp.Reader(shp_path)
    # except:
    #     shp_path = "./data_visualization/resources/Ohio/tl_2016_39_cousub.shp"
    #     sf = shp.Reader(shp_path)

    df = read_shapefile(sf)
    # TODO: Parse user input for AWATER or ALAND or some other option.
    title = 'AWATER in Ohio by County Subdivision'
    data = df.AWATER
    names = df.NAME

    plot_cities_data(sf, title, names, data, 4, False)