# views.py (data_visualization)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of views for data_visualization module."""

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

from base64 import b64encode
from datetime import datetime
from io import BytesIO
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from os.path import join
import pandas as pd
import shapefile as shp
import seaborn as sns
from urllib import parse

from data_visualization.models import AVAILABLE_DATA, AVAILABLE_STATES
from data_visualization.utils import calc_color, read_shapefile
from useeio_foodwaste.settings import SHAPE_FILE_DIR


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
    if request.method == 'POST':
        state = request.POST.get('stateSelect', None)
        datum = request.POST.get('datumSelect', None)
        if state and datum:
            ctx['map'] = generate_map(state, datum)

    return render(request, 'data_visualization.html', ctx)


def get_shape_path(state):
    """Returns absolute path to the proper shape file for the provided state."""
    filename = 'tl_2016_39_cousub.shp'
    return join(SHAPE_FILE_DIR, state, filename)


def generate_map(state, datum):
    """Receives state and datum, then generates a matplotlib map to be rendered."""
    # Get the proper shape file based on the provided state:
    shp_path = get_shape_path(state)
    # Load the shape file into a pandas dataframe.
    sf = shp.Reader(shp_path)
    df = read_shapefile(sf)
    # Get the names (subdivisions) and data to be mapped.
    names = df.NAME
    if datum == 'AWATER':
        title = f'AWATER in {state} by County Subdivision'
        data = df.AWATER
        color_num = 2
    else:
        title = f'ALAND in {state} by County Subdivision'
        data = df.ALAND
        color_num = 4

    # Initialize visualization set:
    sns.set(style="whitegrid", palette="pastel", color_codes=True)
    sns.mpl.rc("figure", figsize=(10,6))

    # Plot the data
    t_plt = plot_cities_data(sf, title, names, data, color_num, False)

    # Render the map into memory
    fig = t_plt.gcf()
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = b64encode(buf.read())
    t_plt.close()
    # Return the memory string:
    return parse.quote(string)


def plot_cities_data(sf, title, cities, data=None, color=None, print_id=False):
    """Plot map with selected cities, using specific color"""
    color_ton, bins = calc_color(data, color)
    df = read_shapefile(sf)
    city_ids = []
    for i in cities:
        indices = df[df.NAME == i].index
        if indices.any():
            id = indices[0]
            city_ids.append(id)
            # for id in indices:
            #     city_ids.append(id)

    return plot_map_fill_multiples_ids_tone(
        sf, title, city_ids, print_id, color_ton, bins,
        x_lim = None, y_lim = None, figsize = (11,9))


def plot_map_fill_multiples_ids_tone(sf, title, cities, print_id, color_ton, bins,
                                     x_lim = None, y_lim = None, figsize = (11,9)):
    """Plot map with lim coordinates"""

    plt.figure(figsize = figsize)
    fig, ax = plt.subplots(figsize = figsize)
    fig.suptitle(title, fontsize=16)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    for id in cities:
        shape_ex = sf.shape(id)
        x_lon = np.zeros((len(shape_ex.points),1))
        y_lat = np.zeros((len(shape_ex.points),1))
        for ip in range(len(shape_ex.points)):
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        # Get the corresponding index of city with id:
        index = cities.index(id)
        try:
            ax.fill(x_lon, y_lat, color_ton[index])
            if color_ton[index] == '#FFFFFF':
                print(f'{id}, {color_ton[index]}')
                print('White!')
        except:
            print("Out of range!")
            pass
        if print_id != False:
            x0 = np.mean(x_lon)
            y0 = np.mean(y_lat)
            plt.text(x0, y0, id, fontsize=10)
    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)
    return plt
