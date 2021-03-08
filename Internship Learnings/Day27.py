#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:12:18 2021

@author: Shavilya Rajput
"""
import requests

from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

source = requests.get(wiki).text

soup = BeautifulSoup(source, "lxml")

right_table = soup.find('table', class_ = 'wikitable')

A = []
B = []
C = []
D = []
E = []
F = []





for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    
    #if in first row, th(count) = 7, td(count) = 0
    #for rest of rows, th(count) = 1, td(count) = 6
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
import pandas as pd
df = pd.DataFrame()

df['State or UT'] = A
df['Admin Cap'] = B
df['Legis Cap'] = C
df['Judi Cap'] = D
df['Year'] = E
df['Formar Cap'] = F
        

df.to_csv('states.csv', index = False)       
       

"""
file = open('test.txt', 'r')

print (file.read())
    
file.close()  
        
file = open('test.txt', 'r')
data = file.readlines()

data[2]  = 'Jodhpur\n'

file.close()

file = open('test.txt','w')



str1 = "".join(data)

file.write(str1)

file.flush()
"""

import sqlite3 as sql
import pandas as pd


conn = sql.connect('states.db')

df.to_sql('statetable', conn)


#reading the data from table
conn = sql.connect('states.db')

new_df = pd.read_sql('SELECT * FROM statetable', conn)


pd.read_sql('SELECT * FROM statetable WHERE Year == 1956', conn)



#how to read the data one record at a time
conn = sql.connect('states.db')
cursor = conn.cursor()

cursor.execute ("SELECT * FROM statetable")

for record in cursor:
    print (record)
