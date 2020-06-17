# lab_data.py (jupyter)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Module to view lab results and site locations from .csv file.

Available functions:
- DataFrames = data in a frame/table or tabular data.
- Construct "geo map functions" using "Shapefiles" for site sampling locations.
"""

# https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f
# Create test in Jupyter Notebook
# In VS Code download extension "geo-data-viewer"

import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
# pylint: disable=no-name-in-module
from data_visualization import calc_color, plot_cities_data, \
    plot_map_fill_multiples_ids_tone, read_shapefile

# 3. Initialize visualization set:
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

# 4. Open a vector shape map:
shp_path = "./resources/Ohio/tl_2016_39_cousub.shp"
try:
    sf = shp.Reader(shp_path)
except:
    shp_path = "./data_visualization/resources/Ohio/tl_2016_39_cousub.shp"
    sf = shp.Reader(shp_path)

# Shape file headers/columns:
# STATEFP, COUNTYFP, COUSUBFP, COUSUBNS, GEOID, NAME, NAMELSAD, LSAD, CLASSFP,
# MTFCC, CNECTAFP, NECTAFP, NCTADVFP, FUNCSTAT, ALAND, AWATER, INTPTLAT, INTPTLON, coords

# For plotting data from this dataset, let's try a heatmap where intensity is
# a range of green for ALAND or a range of blue for AWATER

df = read_shapefile(sf)
title = 'AWATER in Ohio by County Subdivision'
data = df.AWATER
names = df.NAME

plot_cities_data(sf, title, names, data, 4, False)
