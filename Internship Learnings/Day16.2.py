#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:57:51 2021

@author: linux
"""

import pandas as pd 

df = pd.read_csv("Salary_Classification.csv")

df.info()

features2 = df.iloc[:,:4]
label2 = df.iloc[:,-1]

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

columntransformer = ColumnTransformer([('encoder',OneHotEncoder(),[0])],remainder = 'passthrough')

import numpy as np 
features2 = np.array(columntransformer.fit_transform(features2), dtype = np.float32)

features2 = features2[:,1:]

from sklearn.model_selection import train_test_split
features_train2,features_test2,label_train2,label_test2 = train_test_split(features2,label2 , test_size = 0.2)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train2 = sc.fit_transform(features_train2)

features_test2 = sc.transform(features_test2)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(features_train2,label_train2)

pred2 = model.predict(features_test2)

tuple(zip(pred2,label_test2))

xx2 = ['Development', 1100, 0, 1]

xx2 = np.array(xx2)

xx2 = xx2.reshape(1,4)

xx2 = np.array(columntransformer.transform(xx2), dtype = np.float32)

xx2 = xx2[:,1:]

xx2 = sc.transform(xx2)
pred_xx2 = model.predict(xx2)









