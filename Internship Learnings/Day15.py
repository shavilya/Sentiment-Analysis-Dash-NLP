#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:03:25 2021

@author: linux
"""

import pandas as pd 

dataset = pd.read_csv('Salary_Classification.csv')

#features and columns
features = dataset.iloc[:,0:4].values
label = dataset.iloc[:,-1].values

# Converting features[0] into numerical data 

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')

import numpy as np
features = np.array(columnTransformer.fit_transform(features) , dtype = np.float32)

features = features[:,1:]

# Train-Test Split 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size = 0.2)

#Model Building
from sklearn.linear_model import LinearRegression

regressor = LinearRegression() #model

regressor.fit(features_train, labels_train)

pred = regressor.predict(features_test)

pd.DataFrame(zip(pred, labels_test))






