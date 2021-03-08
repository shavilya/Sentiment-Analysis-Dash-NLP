#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:41:30 2021

@author: Shavilya Rajput
"""
import requests

from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

source = requests.get(wiki).text

soup = BeautifulSoup(source , "lxml")

right_table = soup.find('table',class_ = 'wikitable')

A = []
B = []
C = []
D = []
E = []
F = []
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
import pandas as pd
df = pd.DataFrame()

df['States or UT '] = A
df['Admin Cap'] = B
df['Legis Cap'] = C
df['Judi Cap'] = D
df['Year'] = E 
df['Former Cap'] = F

df.to_csv('states.csv',index = False)       
