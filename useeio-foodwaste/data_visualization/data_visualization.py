# data_visualization.py (jupyter)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Module to view lab results and site locations from .csv file.

Available functions:
- DataFrames = data in a frame/table or tabular data.
- Construct "geo map functions" using "Shapefiles" for site sampling locations.
"""


import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

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


# 10. Creating 'Heat Maps'
def calc_color(data, color=None):
        if color == 1:
            color_sq =  ['#dadaebFF','#bcbddcF0','#9e9ac8F0',
                        '#807dbaF0','#6a51a3F0','#54278fF0']
            colors = 'Purples'

        elif color == 2:
            color_sq = ['#c7e9b4','#7fcdbb','#41b6c4',
                        '#1d91c0','#225ea8','#253494']
            colors = 'YlGnBu'

        elif color == 3:
            color_sq = ['#f7f7f7','#d9d9d9','#bdbdbd',
                        '#969696','#636363','#252525']
            colors = 'Greys'

        elif color == 9:
            color_sq = ['#ff0000','#ff0000','#ff0000',
                        '#ff0000','#ff0000','#ff0000']

        else:
            color_sq = ['#ffffd4','#fee391','#fec44f',
                        '#fe9929','#d95f0e','#993404']
            colors = 'YlOrBr'

        new_data, bins = pd.qcut(data, 6, retbins=True,
        labels=list(range(6)))
        color_ton = []
        for val in new_data:
            color_ton.append(color_sq[val])
        if color != 9:
            colors = sns.color_palette(colors, n_colors=6)
            sns.palplot(colors, 0.6)
            for i in range(6):
                print ("\n"+str(i+1)+': '+str(int(bins[i]))+
                       " => "+str(int(bins[i+1])-1), end =" ")
            print("\n\n   1   2   3   4   5   6")
        return color_ton, bins


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

    plot_map_fill_multiples_ids_tone(sf, title, city_ids, print_id, color_ton, bins,
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
