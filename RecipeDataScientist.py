# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:30:44 2019

@author: arosso
"""

import pandas as pd

sFileIn = 'RecipesList_v4'
sFilePrefix = 'Thmix_vcuch_'

# Remove rows with sweets and desserts
s_flt = "almíbar|Batido|Brownie|Bizco|Cake|Caramel|Carbón|Chocolate|Coca|Dulce" + \
            "|Flan|Gallet|Gofre|Helado|Magdalena|Mermelada|Natilla|Navidad|Nocilla" + \
            "|Nugget|Palmer|Pan|Plumcake|Strudel|Sorbete|Tarta|Zumo"

df = pd.read_csv( sFileIn + '.csv', sep=';', \
                         encoding='windows-1252') #'windows-1252')


# remove outliers
df = df[df.i_time_prep  < df.i_time_prep.quantile(.9) ]
df = df[df.i_time_cook  < df.i_time_cook.quantile(.9) ]
df = df[df.i_time_total < df.i_time_total.quantile(.9) ]

# Remove rows with zeros:
df = df[df.i_time_prep  > 0 ]
df = df[df.i_time_cook  > 0 ]
df = df[df.i_time_total > 0 ]



df_flt = df[df['Name'].str.contains(s_flt, case=False)==False]
df_flt.to_csv(sFilePrefix + sFileIn + '_flt.csv', sep =';', encoding='windows-1252')

df_flt_neg = df[df['Name'].str.contains(s_flt, case=False)==True]
df_flt_neg.to_csv(sFilePrefix + sFileIn + '_flt_neg.csv', sep =';', encoding='windows-1252')


#df.hist(column=['i_time_prep','i_time_cook','i_time_total'], bins=40) 
df.hist(column=['i_time_prep','i_time_cook','i_time_total'], bins=range(0, 80, 5))

df.hist(column=['ratingValue', 'ratingCount'], bins=40)
# hay algunas recetas con un rating value/count muy alto !! Revisar!!

# ToDo: get count of 'recipeType' and 'cuisine'
# Cuantas recetas no son de Rosa Ardá ??

