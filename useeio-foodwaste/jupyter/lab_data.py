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

# 3. Initialize visualization set:
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

# 4. Open a vector shape map:
shp_path = "./VectorMaps/tl_2016_39_cousub.shp"
sf = shp.Reader(shp_path)
# Print some of the contents of the shape file:
# print(len(sf.shapes()))
# print(sf.records()[1])
# print(sf.records()[1][5])
# print(sf.records()[25])

# 5. Converting shapefile data on Pandas dataframe
def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' column
    holding the geometry information. This uses the pyshp package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

df = read_shapefile(sf)
# print(df.shape)
print(df.sample(5))