#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 12:35:25 2021

@author: linux
"""
# D A T A - A N A L Y S I S 

import pandas as pd 

df = pd.read_csv('balanced_review.csv')

# D A T A - C L E A N I N G 

df.dropna(inplace = True)

# D A T A - P R E P A R A T I O N 

df = df[df['overall'] !=3]

df['overall'].value_counts()

import numpy as np 

df['positivity'] = np.where( df['overall'] > 3 , 1,0)

#Features - ReviewText
#Label - Positivity

# T R A I N - T E S T    S P L I T 
 
from sklearn.model_selection import train_test_split
features_train , features_test , label_train , label_test = train_test_split(df['reviewText'] , df['positivity'] ,test_size = 0.2 , random_state = 31) 

# B A G OF W O R D S   M O D E L 
# V E C T O R I Z A T I O N 

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit(features_train)

len(vect.get_feature_names())

features_train_vectorized = vect.transform(features_train)

# array = features_train_vectorized.toarray()

# P R E P A R E - T H E - M O D E L 
#V E R S I O N 1 
#KNN , SVM , Naive Bayes , Logistic Regression etc

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(features_train_vectorized , label_train )

predictions = model.predict(vect.transform(features_test))

# CONFUSION MATRIX 

from sklearn.metrics import confusion_matrix

confusion_matrix(label_test , predictions)

# ROC AUC SCORE 

from sklearn.metrics import roc_auc_score
roc_auc_score(label_test , predictions)
