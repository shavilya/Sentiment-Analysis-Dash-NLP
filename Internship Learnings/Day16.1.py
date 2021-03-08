#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:53:54 2021

@author: Shavilya Rajput
"""


import pandas as pd 

df = pd.read_csv("Salary_Classification.csv")

df.info()

features = df.iloc[:,:4]
label = df.iloc[:,-1]

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

columntransformer = ColumnTransformer([('encoder',OneHotEncoder(),[0])],remainder = 'passthrough')

import numpy as np 
features = np.array(columntransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,label_train,label_test = train_test_split(features,label , test_size = 0.2)


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(features_train,label_train)

pred = model.predict(features_test)

tuple(zip(pred,label_test))

xx = ['Development', 1100, 0, 1]

xx = np.array(xx)

xx = xx.reshape(1,4)

xx = np.array(columntransformer.transform(xx), dtype = np.float32)

xx = xx[:,1:]

pred_xx = model.predict(xx)
