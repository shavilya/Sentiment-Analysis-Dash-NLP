#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:32:24 2021

@author: linux
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


import matplotlib.pyplot as plt
plt.scatter(features, labels)

plt.plot(features, regressor.predict(features))


#train test split case
import pandas as pd


dataset = pd.read_csv("student_scores.csv")

features  = dataset['Hours'].values

labels = dataset['Scores'].values



from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression() #model

features_train = features_train.reshape(len(features_train), 1)
regressor.fit(features_train, labels_train)

features_test = features_test.reshape(len(features_test), 1)

pred = regressor.predict(features_test)

pd.DataFrame(zip(pred, labels_test))

tuple(zip(pred, labels_test))


#score - train score, test score

#train score
regressor.score(features_train, labels_train)

#test score
regressor.score(features_test, labels_test)


"""
#case 1
train score good, test score good - required case

#case 2

train score good, test score poor - overfitting


#case 3

train score poor, test score poor - underfitting

#case 4

train score poor, test score good - not possible

"""
