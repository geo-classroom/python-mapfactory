# -*- coding: utf-8 -*-
"""Hlamarisa_Multi_Chloro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uL4ppMPyY8S5fBJ1z5klIiKCjzGNlGmi
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install geopandas
# %pip install mapclassify

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import mapclassify as mc
from mpl_toolkits.axes_grid1 import make_axes_locatable

def multi_choro(path, col, map_title):
    path = path
    df = gpd.read_file(path)

    # Choropleth map (quantiles)
    quan_map1 = df.plot(column = col, cmap= 'autumn', scheme = 'quantiles', edgecolor = 'black', k = 3, legend = True)
    quan_map1.set_title(map_title + ' (Quantiles - 3 Classes)'),
    quan_map2 = df.plot(column = col, cmap = 'autumn', scheme = 'quantiles', edgecolor = 'black', k = 5, legend = True)
    quan_map2.set_title(map_title + ' (Quantiles - 5 Classes)'),
    quan_map3 = df.plot(column = col, cmap = 'autumn', scheme = 'quantiles', edgecolor = 'black', k = 7, legend = True)
    quan_map3.set_title(map_title + ' (Quantiles - 7 Classes)')

    
    # Choropleth maps (natural breaks)
    nb_map1 = df.plot(column = col, cmap = 'OrRd', scheme = 'natural_breaks', edgecolor = 'black', k = 3, legend = True)
    nb_map1.set_title(map_title + ' (Natural Breaks - 3 Classes)')
    nb_map2 = df.plot(column = col, cmap = 'OrRd', scheme = 'natural_breaks', edgecolor = 'black', k = 5, legend = True)
    nb_map2.set_title(map_title + ' (Natural Breaks - 5 Classes)')
    nb_map3 = df.plot(column = col, cmap = 'OrRd', scheme = 'natural_breaks', edgecolor = 'black', k = 7, legend = True)
    nb_map3.set_title(map_title + ' (Natural Breaks - 7 Classes)')

    # Choropleth maps (equal intervals)
    ei_map1 = df.plot(column = col, cmap = 'Greens', scheme = 'equal_interval', edgecolor = 'black', k = 3, legend = True)
    ei_map1.set_title(map_title + ' (Equal Interval - 3 Classes)')
    ei_map2 = df.plot(column = col, cmap = 'Greens', scheme = 'equal_interval', edgecolor = 'black', k = 5, legend = True)
    ei_map2.set_title(map_title + ' (Equal Interval - 5 Classes)')
    ei_map3 = df.plot(column = col, cmap = 'Greens', scheme = 'equal_interval', edgecolor = 'black', k = 7, legend = True)
    ei_map3.set_title(map_title + ' (Equal Interval - 7 Classes)')

    # Choropleth maps (percentiles)

    # prct_map1 = mc.Percentiles(df, pct = [25, 50, 75, 100])
    # prct_map1.set_title(map_title + ' (Percentiles - 3 Classes)')
    # count_values = df[col].sum()
    # df['percent'] = df[df[col]/count_values*100]
    prc_map1 = df.plot(column = 'percent', cmap = 'YlOrBr', scheme = 'percentiles', k = 3, legend = True)
    prc_map1.set_title(map_title + ' (Percentiles - 3 Classes)')
    prc_map2 = df.plot(column = 'percent', cmap = 'YlOrBr', scheme = 'percentiles', k = 5, legend = True)
    prc_map2.set_title(map_title + ' (Percentiles - 5 Classes)')
    prc_map3 = df.plot(column = 'percent', cmap = 'YlOrBr', scheme = 'percentiles', k = 7, legend = True)
    prc_map3.set_title(map_title + ' (Percentiles - 7 Classes)')
#test
#multi_choro('https://raw.githubusercontent.com/Hlamarisa/python-mapfactory/master/country_boundaries_v2.json', 'POP_EST', 'Population Countries')