# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:17:40 2019

@author: arosso

TODO: review recipe-scraper repo to see if time cleaning function needs any idea from this repo
"""

#import os
import glob
#import pandas as pd
import json
import csv
import re
# %%

s_json_recipe_dir = r'C:/Users/arosso/Dropbox/TEMP/RECETARIO/json/'
s_host = '101cookbooks-com'
s_cur_dir = s_json_recipe_dir + s_host + r'/'

# %%
def time_cleaner(s_time):
    """Gets hour and time from time field, and converts to minutes.

    # For debug in https://regex101.com/
    # print(time_cleaner('4 min' ))
    # print(time_cleaner(' 4min' ))
    # print(time_cleaner(' 4 min' ))
    #print(time_cleaner('1h4 min' ))
    #print(time_cleaner('1h 4 min' ))
    #print(time_cleaner('1h4min' ))
    #print(time_cleaner('1h 4min' ))
    #print(time_cleaner(' 1h4 min' ))
    #print(time_cleaner(' 1h 4 min' ))
    #print(time_cleaner(' 1h4min' ))
    #print(time_cleaner(' 1h 4min' ))
    """
    def apply_regex(s_pat ,s_str):
        s_aux = re.findall(s_pat, s_str)
        # if success gets number in pattern : 
        if s_aux:
            s_aux = int(re.findall('[0-9]+',s_aux[0])[0])
        else:
            s_aux = 0
        return s_aux
    
    i_min   = apply_regex('[0-9]+\s*m' ,s_time)
    i_hours = apply_regex('[0-9]+\s*h' ,s_time)
    
    return i_min + i_hours*60

# Auxiliary function to use time_cleaner
    # if dict has no time info, writes a '0'
def apply_time_cleaner(dict_recipe, s_field):
    if bool(dict_recipe[s_field]): 
        dict_recipe['i_' + s_field ] = time_cleaner(dict_recipe[s_field])
    else:
        dict_recipe['i_' + s_field ] = 0
        dict_recipe[       s_field ] = '0'
# %%    
if __name__ == '__main__':    

    dict_json_files = glob.glob(s_cur_dir + '*.json')
    print()
    
    #for debug
    #dict_recipe['Name'] = 'hola'
    #dict_recipe['time_prep'  ] = 10
    #dict_recipe['time_cook'  ] =  5
    #dict_recipe['time_total' ] = 20
    
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

    with open(s_json_recipe_dir + s_host + '.csv', mode='w', newline='\n', encoding='windows-1252') as output_file:
        output_file_writer = csv.writer(output_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        output_file_writer.writerow(li_fields)
        # TODO: replace writerow by auxiliary function using li_fields
        for recipe in dict_results:
            output_file_writer.writerow([ \
                dict_results[recipe]['title'], \
                # TODO: dict_results[recipe]['Author'], \
                # TODO: dict_results[recipe]['recipeType'], \
                # TODO: dict_results[recipe]['cuisine'], \
                # TODO: count of ingredients
                # TODO: count of instructions
                dict_results[recipe]['yields'], \
                dict_results[recipe]['ratings'], \
                dict_results[recipe]['reviews'], \
                dict_results[recipe]['prep_time'], \
                dict_results[recipe]['cook_time'], \
                dict_results[recipe]['total_time'], \
                dict_results[recipe]['host'], \
                dict_results[recipe]['source'] ])
            #employee_writer.writerow([recipe['Name'], recipe['time_prep'], recipe['time_cook'], recipe['time_total']])
            #print(dict_results[recipe]['Name'])#, recipe['time_prep'], recipe['time_cook'], recipe['time_total'])
