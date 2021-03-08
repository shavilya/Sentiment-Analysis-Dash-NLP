#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:43:26 2021

@author: linux
"""

import pandas as pd 

df = pd.read_csv('balanced_review.csv')

df.isnull().any(axis = 0)

df[df.isnull().any(axis = 1)]

df.dropna(inplace = True)

df = df[df['overall'] !=3]

df.shape

df['overall'].value_counts()

import numpy as np 

df['positivity'] = np.where( df['overall'] > 3 , 1,0)

