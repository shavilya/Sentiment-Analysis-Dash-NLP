#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:15:04 2021

@author: Shavilya Rajput
"""


import pandas as pd


dataset = pd.read_csv("student_scores.csv")

features  = dataset['Hours'].values

labels = dataset['Scores'].values

import matplotlib.pyplot as plt
plt.scatter(features, labels)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression() #model

features = features.reshape(25, 1)
regressor.fit(features, labels)

m = regressor.coef_

c = regressor.intercept_

#y = mx + c

x = 9

regressor.predict([[9]])