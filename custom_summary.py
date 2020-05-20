# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:30:44 2019

@author: arosso
"""

import glob
import json
import pandas as pd
import csv
import traceback
# %% Parameters

# TODO: move to config file
input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources/"
# input_sources_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/_sources_test/"
output_base_folder = r"C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/"

# %% Main

if __name__ == '__main__':

    dict_json_files = glob.glob(output_base_folder + '**/*.json', recursive=True)

    # %% Reads all recipes and load into dict_results file
    dict_results = {}

    for s_file in dict_json_files:
        # If exists improved file, read improved file, else read normal file and add info.

        with open(s_file, encoding='utf-8') as json_file:
            dict_recipe = json.load(json_file)
            try:
                # apply_time_cleaner(dict_recipe, 'time_prep')
                # apply_time_cleaner(dict_recipe, 'time_cook')
                # apply_time_cleaner(dict_recipe, 'time_total')
                print(s_file)
                s_name = dict_recipe['title']
                dict_results[s_name] = dict_recipe
            except Exception:
                print(dict_recipe)
                print(s_file)
                print('title not found')
                traceback.print_exc()
                _str = traceback.format_exc()
                print(_str)

    # %% Writes recipes summary csv file
    print('-'*60 + '\n' + 'Write summary file')
    li_fields = ['title', 'yields', 'ratings', 'reviews',
                 'prep_time', 'cook_time', 'total_time',
                 'ingredients_count','instructions_count',
                 'host', 'source']
    # TODO: check if all fields are in file??
    with open(output_base_folder + 'summary.csv', mode='w', newline='\n', encoding='windows-1252') as output_file:
        output_file_writer = csv.writer(output_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        output_file_writer.writerow(li_fields)
        # TODO: replace writerow by auxiliary function using li_fields
        for recipe in dict_results:
            print(dict_results[recipe]['title'])
            try:
                output_file_writer.writerow([
                    dict_results[recipe]['title'],
                    # TODO: dict_results[recipe]['Author'],
                    # TODO: dict_results[recipe]['recipeType'],
                    # TODO: dict_results[recipe]['cuisine'],
                    dict_results[recipe]['ingredients_count'],
                    dict_results[recipe]['instructions_count'],
                    dict_results[recipe]['yields'],
                    dict_results[recipe]['ratings'],
                    dict_results[recipe]['reviews'],
                    dict_results[recipe]['prep_time'],
                    dict_results[recipe]['cook_time'],
                    dict_results[recipe]['total_time'],
                    dict_results[recipe]['host'],
                    dict_results[recipe]['source']
                ])
            except Exception:
                print(dict_results[recipe])
                print('There is a problem with some field')
            # output_file_writer.writerow([recipe['Name'], recipe['time_prep'], recipe['time_cook'], recipe['time_total']])
            # print(dict_results[recipe]['Name'])#, recipe['time_prep'], recipe['time_cook'], recipe['time_total'])



