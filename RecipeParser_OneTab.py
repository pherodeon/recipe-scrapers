# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:33:05 2019

@author: arosso
"""

from requests import get 
# from urllib.parse import urljoin
# from os import path, makedirs #, getcwd
from bs4 import BeautifulSoup as soup
import logging
from slugify import slugify
	
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
        
def custom_concat(s_in, s_add):
    if s_add is not None:
        s_in =  s_in + s_add
    return s_in

if __name__ == '__main__':
    base_url = r'https://www.one-tab.com/page/TcSGdgxWQIqxntf3Xt3RRw'
    html_tag = 'a'
    
    #links = get_page_links(base_url, 'a')
    html  = get_page(base_url)  #MISSING ARGUMENT
    links = get_all_links(html, html_tag)
    if len(links) == 0:
        logging.warning('No links found on the webpage.')
        raise Exception('No links found on the webpage.')

    for link in links:
        current_link = link.get('href')
        
        if len(current_link) > 25:      
            file_address = slugify(link.string) + '.csv'
            print('-'*60)
            print(current_link)
            
            # sub_links = get_page_links(link, 'a')
            html      = get_page(current_link)  #MISSING ARGUMENT
            bs = soup(html, 'html.parser')
            #sub_links = get_all_links(html, html_tag)
            sub_links = bs.find('div', attrs={'class':'article-content'}).findAll(html_tag)
            
            if len(sub_links) == 0:
                logging.warning('No links found on the webpage.')
                raise Exception('No links found on the webpage.')
            with open(file_address, 'w+') as file_out:
                for sub_link in sub_links:
                    s_aux = ''
                    s_aux = custom_concat(s_aux, sub_link.string) + ';' 
                    s_aux = custom_concat(s_aux, sub_link.get('href')) + ';'
                    s_aux = s_aux + '\n'
                    if s_aux is not None:
                        file_out.write(s_aux)
                        #curr_sub_link = sub_link.get('href')
                        #print(curr_sub_link)
                        #print(sub_link.string)



