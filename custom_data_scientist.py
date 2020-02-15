# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:30:44 2019

@author: arosso
"""

import glob
import json
import pandas as pd

# %% Parameters

# TODO: move to config file
input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources/"
# input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources_test/"
output_base_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/"

# %% Main

if __name__ == '__main__':

    dict_json_files = glob.glob(output_base_folder + '*/**/.json', recursive=True)

    # %% Reads all recipes and load into dict_results file
    dict_results = {}

    for s_file in dict_json_files:
        # If exists improved file, read improved file, else read normal file and add info.

        with open(s_file, encoding='utf-8') as json_file:
            dict_recipe = json.load(json_file)

            # apply_time_cleaner(dict_recipe, 'time_prep')
            # apply_time_cleaner(dict_recipe, 'time_cook')
            # apply_time_cleaner(dict_recipe, 'time_total')

            s_name = dict_recipe['title']
            dict_results[s_name] = dict_recipe

    # %% Writes recipes summary csv file
    li_fields = ['title', 'yields', 'ratings', 'reviews', 'prep_time', 'cook_time', 'total_time', 'host', 'source']

    with open(output_base_folder + 'summary.csv', mode='w', newline='\n', encoding='windows-1252') as output_file:
        output_file_writer = csv.writer(output_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        output_file_writer.writerow(li_fields)
        # TODO: replace writerow by auxiliary function using li_fields
        for recipe in dict_results:
            output_file_writer.writerow([
                dict_results[recipe]['title'],
                # TODO: dict_results[recipe]['Author'],
                # TODO: dict_results[recipe]['recipeType'],
                # TODO: dict_results[recipe]['cuisine'],
                # TODO: count of ingredients
                # TODO: count of instructions
                dict_results[recipe]['yields'],
                dict_results[recipe]['ratings'],
                dict_results[recipe]['reviews'],
                dict_results[recipe]['prep_time'],
                dict_results[recipe]['cook_time'],
                dict_results[recipe]['total_time'],
                dict_results[recipe]['host'],
                dict_results[recipe]['source']
            ])
            # output_file_writer.writerow([recipe['Name'], recipe['time_prep'], recipe['time_cook'], recipe['time_total']])
            # print(dict_results[recipe]['Name'])#, recipe['time_prep'], recipe['time_cook'], recipe['time_total'])

    # %% Data analysis

    df = pd.read_csv(sFileIn + '.csv', sep=';', encoding='windows-1252') #'windows-1252')

    """
    # Remove rows with sweets and desserts
    s_flt = "almíbar|Batido|Brownie|Bizco|Cake|Caramel|Carbón|Chocolate|Coca|Dulce" + \
                "|Flan|Gallet|Gofre|Helado|Magdalena|Mermelada|Natilla|Navidad|Nocilla" + \
                "|Nugget|Palmer|Pan|Plumcake|Strudel|Sorbete|Tarta|Zumo"
    # df_flt = df[df['Name'].str.contains(s_flt, case=False)==False]
    # df_flt.to_csv(sFilePrefix + sFileIn + '_flt.csv', sep =';', encoding='windows-1252')

    # df_flt_neg = df[df['Name'].str.contains(s_flt, case=False)==True]
    # df_flt_neg.to_csv(sFilePrefix + sFileIn + '_flt_neg.csv', sep =';', encoding='windows-1252')
    """

    fields = ['total_time', 'prep_time', 'cook_time']
    for fld in fields:
        # remove outliers
        df = df[df[fld] < df[fld].quantile(.9)]
        # Remove rows with zeros:
        df = df[df.[fld] > 0]

    df.hist(column=fields, bins=40)

    df.hist(column=fields, bins=range(0, 80, 5))

    df.hist(column=fields, bins=40)

