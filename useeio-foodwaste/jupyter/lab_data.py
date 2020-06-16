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

sns.set(style=”whitegrid”, palette=”pastel”, color_codes=True)
sns.mpl.rc(“figure”, figsize=(10,6))

%matplotlib inline

# Jake, need assistance 'Opening a Vector Map' for Cincinnati, OH.
# https://catalog.data.gov/dataset/tiger-line-shapefile-2016-state-ohio-current-county-subdivision-state-based
shp_path = “./jupyter/Vector Maps/tl_2016_39_cousub.shp”
sf = shp.Reader(shp_path)

len(sf.shapes())

