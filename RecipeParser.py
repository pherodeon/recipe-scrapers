# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25

@author: arosso
"""

# %% Libraries

#Internet
from requests import get 
# from urllib.parse import urljoin
# from os import path, makedirs #, getcwd
from bs4 import BeautifulSoup as soup
#System
from os import path, makedirs #, getcwd 
from glob import glob
from slugify import slugify
import json
import logging
from time import sleep, time
# Math
import random as rn

# %% Auxiliary functions

def get_page(base_url):
    # mask as a chrome user
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    req = get(base_url, headers=headers)
    
    #! ToDo: if != 200 raise exception, else, return req.text ?
    if req.status_code == 200:
        return req.text
    logging.warning('http status_code: ' + req.status_code)
    raise Exception('Error {0}'.format(req.status_code))

def get_all_links(html, html_tag):
    bs = soup(html, 'html.parser')
    links = bs.findAll(html_tag)
    return links

def get_page_links(base_url, html_tag):
    html  = get_page(base_url)  #MISSING ARGUMENT
    links = get_all_links(html, html_tag)
    if len(links) == 0:
        logging.warning('No links found on the webpage.')
        raise Exception('No links found on the webpage.')

    return links
# %% Auxiliary functions
        
def custom_concat(s_in, s_add):
    if s_add is not None:
        s_in =  s_in + s_add
    return s_in

def check_dir(base_dir):
    '''Creates dir if not exists
    
    Requires path library'''
    if not path.exists(base_dir):
        makedirs(base_dir)
    return base_dir

# %% Recipe download functions
    
def recipe_find(base_url, recipe, s_div, s_item, s_prop):
    try:
        _ = recipe.find(s_div,  attrs={s_item:s_prop}).text
        return _
    except:
        return ''
        #print(base_url, s_div, s_item, s_prop)

def recipe_find_all(base_url, recipe, s_div, s_item, s_prop):
    try:
        aux = recipe.findAll(s_div,  attrs={s_item:s_prop})
        aux = [x.text for x in aux] # Parece que x.text funciona siempre y x.string a veces. ToDo: Revisar
        return aux
    except:
        #print(base_url, s_div, s_item, s_prop)
        return ''
    
def dump_recipe(base_url, s_type, s_subdir):
    dict_recipe = {}
    
    try:
        #links = get_page_links(base_url, 'a')
        html = get_page(base_url)  #MISSING ARGUMENT
        bs = soup(html, 'html.parser')
        
        d_conf = {}
        if s_type=='easyrecipe':
            
            d_conf['Name'         ] = (True  ,'div'  ,'class'    ,'ERSName'            )
            d_conf['Author'       ] = (True  ,'span' ,'itemprop' ,'author'             )
            d_conf['recipeType'   ] = (True  ,'span' ,'itemprop' ,'recipeCategory'     )
            d_conf['cuisine'      ] = (True  ,'span' ,'itemprop' ,'recipeCuisine'      )
            d_conf['serves'       ] = (True  ,'span' ,'itemprop' ,'recipeYield'        )
            d_conf['ratingValue'  ] = (True  ,'span' ,'itemprop' ,'ratingValue'        )
            d_conf['ratingCount'  ] = (True  ,'span' ,'itemprop' ,'ratingCount'        )
            d_conf['time_prep'    ] = (True  ,'time' ,'itemprop' ,'prepTime'           )
            d_conf['time_cook'    ] = (True  ,'time' ,'itemprop' ,'cookTime'           )
            d_conf['time_total'   ] = (True  ,'time' ,'itemprop' ,'totalTime'          )
            d_conf['Notes'        ] = (True  ,'div'  ,'class'    ,'ERSNotes'           )
            d_conf['ingredients'  ] = (False ,'li'   ,'itemprop' ,'ingredients'        )
            d_conf['instructions' ] = (False ,'li'   ,'itemprop' ,'recipeInstructions' )
            
            # pendiente!!!! No está dentro de la receta !!! hay que cogerlo de fuera
            #!d_conf['date'         ] = (True  ,'div'  ,'itemprop' ,'datePublished'      )
            
            recipe = bs.find('div', attrs={'class':'easyrecipe'})
            dict_recipe['Source' ] = base_url
            dict_recipe['s_type' ] = s_type
            
        elif  s_type=='mv-create-wrapper':
            
            d_conf['Name'         ] = (True  ,'div'  ,'class'    ,'mv-create-title mv-create-title-primary' )
            #d_conf['Author'       ] = (True  ,'span' ,'itemprop' ,'author'             )
            #d_conf['recipeType'   ] = (True  ,'span' ,'itemprop' ,'recipeCategory'     )
            #d_conf['cuisine'      ] = (True  ,'span' ,'itemprop' ,'recipeCuisine'      )
            #d_conf['serves'       ] = (True  ,'span' ,'itemprop' ,'recipeYield'        )
            #d_conf['ratingValue'  ] = (True  ,'span' ,'itemprop' ,'ratingValue'        )
            #d_conf['ratingCount'  ] = (True  ,'span' ,'itemprop' ,'ratingCount'        )
            d_conf['time_prep'    ] = (True  ,'div'  ,'class'    ,'mv-create-time mv-create-time-prep' )
            d_conf['time_cook'    ] = (True  ,'div'  ,'class'    ,'mv-create-time mv-create-time-active' )
            d_conf['time_total'   ] = (True  ,'div'  ,'class'    ,'mv-create-time mv-create-time-total'          )
            #d_conf['Notes'        ] = (True  ,'div'  ,'class'    ,'ERSNotes'           )
            # Pasar un beautiful soup y aplicar li
            #"mv-create-ingredients"
            d_conf['ingredients'  ] = (False ,'li'   ,'itemprop' ,'ingredients'        )
            #"mv-create-instructions"
            d_conf['instructions' ] = (False ,'li'   ,'itemprop' ,'recipeInstructions' )

            recipe = bs.find('div', attrs={'class':'mv-create-wrapper'})
            dict_recipe['Source' ] = base_url
            dict_recipe['s_type' ] = s_type
            
        else:
            raise Exception('Option not included in library')

        for fld in d_conf:
            if d_conf[fld][0]: 
                dict_recipe[fld] = recipe_find(    base_url ,recipe, d_conf[fld][1] ,d_conf[fld][2] ,d_conf[fld][3] ) # Single data
            else:
                dict_recipe[fld] = recipe_find_all(base_url ,recipe, d_conf[fld][1] ,d_conf[fld][2] ,d_conf[fld][3] ) # Lists of elements

        #Dealing with json in python:
        #https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
        if bool(dict_recipe) and bool(dict_recipe['ingredients']) : # and bool(dict_recipe['instructions']):
            #s_enc = 'iso-8859-1'
            #s_enc = 'windows-1252'
            #s_enc = 'utf-8'
            s_file_out = r'./' + s_subdir + r'/' + slugify(dict_recipe['Name']) + '_vcuch' + '_thmix' + '.json'
            with open(s_file_out, 'w', encoding='utf-8') as outfile: # 'iso-8859-1' 'windows-1252'
                json.dump(dict_recipe, outfile, indent=2, ensure_ascii=False)
            
            # Exit
            print('Success!! ' + base_url) #ToDo: Log?
            return True
        else:
            # Exit
            print('Miss.Data ' + base_url)
            return False
    except:
        # ToDo: capture error.
        with open('log_errors.txt', 'w+') as file_out:
             file_out.write(base_url)
             
        # Exit     
        print('Exception ' + base_url)
        return False

def read_links_file(S_LINKS_FILE):
    li_links = []
    with open(S_LINKS_FILE,'r',encoding='windows-1252') as input_file:
        for line in input_file:
            li_links.append(line.rstrip())
    return li_links

def scan_for_links(base_url):

    html = get_page(base_url)
    bs = soup(html, 'html.parser')
    columns = bs.findAll('div',  attrs={'class':'azindex'})

    li_links = []
    for column in columns:
        
        links = column.findAll(html_tag) 
    
        if len(links) == 0:
            s_message = 'No links found on the webpage.'
            logging.warning(s_message)
            print(s_message)
        else:
            li_links += [link.get('href') for link in links]

    return li_links

def get_url_from_file(filename):
    url = ''
    with open(filename, "r") as infile:
        for line in infile:
            if (line.startswith('URL')):
                url = line[4:]
                break
        return url

def scan_url_files(S_DIR='C:/Users/arosso/Dropbox/TEMP/RECETARIO/_2down'):
    
    S_FILE_EXT = ".URL"
    li_files_glob = glob(S_DIR + "/*" + S_FILE_EXT)
    li_links = [get_url_from_file(file) for file in li_files_glob]
    
    return li_links

# %% Main

if __name__ == '__main__':
    
    B_SCAN_WEB = False
    B_SCAN_FILE = False
    B_SCAN_URL_FILES = True
    
    li_links = []

    StartTime = time()
    
    #B_SCAN_FILE = True
    S_LINKS_FILE = 'FeedlySavedForLater1576052675954_vcuch.txt'
    
    # B_SCAN_WEB = True
    base_url = 'https://www.velocidadcuchara.com/indice-recetas-thermomix/'
    html_tag = 'a'
    s_type   = 'easyrecipe'
    s_subdir = 'Vcuch'
    
    
    
    # For debug
    #1
    #s_type   = 'easyrecipe'
    #base_url = li_links[0]
    #base_url = r'https://www.velocidadcuchara.com/crema-de-calabacin/'
    #base_url = r'http://www.velocidadcuchara.com/berenjenas-pollo-curry-thermomix/'
    #base_url = r'http://www.velocidadcuchara.com/hummus-de-pimientos-del-piquillo/'
    #2
    #s_type   = 'mv-create-wrapper'
    #base_url = r'https://www.pressurecookingtoday.com/pressure-cooker-mongolian-beef/'
    #s_subdir = 'Vcuch'
    #dict_recipe = dump_recipe(base_url, s_type, s_subdir)
    
    # %% Init
    check_dir(r'./' + s_subdir)
    
    # %% Accumulates sources of list of links
    print('-'*79)
    
    if B_SCAN_WEB:
        li_links += scan_for_links(base_url)

    if B_SCAN_FILE:
        li_links += read_links_file(S_LINKS_FILE)
    
    if B_SCAN_URL_FILES:
        li_links += scan_url_files()
    
    ScanTime = time() - StartTime
    print(f'url scan time {ScanTime}')
    
    # %% Download links
    print('-'*79)
    
    # Shuffle list
    rn.shuffle(li_links)
    
    li_success = []
    li_fail    = []
    for link_url in li_links:
        #sleep(2 + rn.random()*6)
        
        if bool(dump_recipe(link_url, s_type, s_subdir)):
            li_success.append(link_url)
        else:
            li_fail.append(link_url)
    
    with open('vcuch_missing.txt','w+') as outfile:
        for link_url in li_fail:
            outfile.write(f'{link_url}\n')
    
    ParsingTime = time() - ScanTime
    
    # %% Final summary
    
    print(f'Parsing time {ParsingTime}')
    print(f'Success : {len(li_success)}.')
    print(f'Fail    : {len(li_fail)}.')
    print(f'Total   : {len(li_links)}.')
    
    