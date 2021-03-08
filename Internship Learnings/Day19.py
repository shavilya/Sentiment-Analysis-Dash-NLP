#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:42:48 2021

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

df['positivity'].value_counts()

df.columns.to_list()

#Features - ReviewText
#Label - Positivity

from sklearn.model_selection import train_test_split
features_train , features_test , label_train , label_test = train_test_split(df['reviewText'] , df['positivity'] ,test_size = 0.2 , random_state = 31) 

# B A G OF W O R D S 

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit(features_train)

len(vect.get_feature_names())

features_train_vectorized = vect.transform(features_train)

array = features_train_vectorized.toarray()
