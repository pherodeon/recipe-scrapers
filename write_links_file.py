# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:33:58 2020

@author: arosso
"""

# %% 
#Internet
from requests import get 
# from urllib.parse import urljoin
# from os import path, makedirs #, getcwd
from bs4 import BeautifulSoup as soup

# %% 
target_url = 'https://www.pressurecookrecipes.com/easy-instant-pot-recipes/'
target_tags = 'a' #['h3', 'a']
output_file = 'pressure_cook_recipes.txt'

# %% 
def get_page(base_url):
    # mask as a chrome user
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    req = get(base_url, headers=headers)
    
    #! ToDo: if != 200 raise exception, else, return req.text ?
    if req.status_code == 200:
        return req.text
    # logging.warning('http status_code: ' + req.status_code)
    raise Exception('Error {0}'.format(req.status_code))
    
def get_all_links(html, html_tag):
    bs = soup(html, 'html.parser')
    # TODO: improve bs to search inside 
    links = bs.findAll(html_tag)
    li_links = [link.get('href') for link in links]
    if len(links) == 0:
        # logging.warning('No links found on the webpage.')
        raise Exception('No links found on the webpage.')
    return li_links

def get_page_links(base_url, html_tag):
    html  = get_page(base_url)  #MISSING ARGUMENT
    li_links = get_all_links(html, html_tag)
    return li_links
        
def write_list_to_file(my_list, file_out):
    with open(file_out, 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)
        
    
# %% 


li_links = get_page_links(target_url,['h3', 'a'])
write_list_to_file(li_links, output_file)




























