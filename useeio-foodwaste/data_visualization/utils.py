# data_visualization.py (lab_data)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Module to view lab results and site locations from .csv file.

Available functions:
- DataFrames = data in a frame/table or tabular data.
- Construct "geo map functions" using "Shapefiles" for site sampling locations.
"""


import pandas as pd
import seaborn as sns

# 5. Converting shapefile data on Pandas dataframe
def read_shapefile(sf):
    """
    Read a shapefile.
    
    Into a Pandas dataframe with a 'coords' column holding the geometry
    information. This uses the pyshp package.
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

        # NOTE: Illinois had an issue with duplicate bins. We tried solving with
        # kwarg duplicate='raise' and duplicate='drop', but neither worked.
        # Another solution is to rank the data (in the except clause), as suggested:
        # https://stackoverflow.com/questions/20158597/how-to-qcut-with-non-unique-bin-edges/40548606#40548606
        try:
            new_data, bins = pd.qcut(data, 6, retbins=True, labels=list(range(6)))
        except:
            new_data, bins = pd.qcut(data.rank(method='first'), 6,
                                     retbins=True, labels=list(range(6)))

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
