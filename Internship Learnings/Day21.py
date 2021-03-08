#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:25:40 2021

@author: linux
"""

# TF - IDF 
# V E R S I O N 2 

import pandas as pd 

df = pd.read_csv('balanced_review.csv')

df.dropna(inplace = True)

df = df[df['overall'] !=3]

df['overall'].value_counts()

import numpy as np 

df['positivity'] = np.where( df['overall'] > 3 , 1,0)

#Features - ReviewText
#Label - Positivity

# T R A I N - T E S T    S P L I T 
 
from sklearn.model_selection import train_test_split
features_train , features_test , label_train , label_test = train_test_split(df['reviewText'] , df['positivity'] ,test_size = 0.2 , random_state = 31) 


# TF - IDF 

from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(min_df = 5).fit(features_train)

vect.vocabulary_
features_train_vectorized = vect.transform(features_train)

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



#################### Saving this model into a pickle file ############

import pickle 

pkl_filename = "pickle_model.pkl"

with open(pkl_filename ,'wb') as file:
    pickle.dump(model, file)

# save the vocabulary file  
pickle.dump(vect.vocabulary_, open('feature.pkl' , 'wb'))

##################

with open(pkl_filename , 'rb') as file:
    pickle_model = pickle.load(file)


pred = pickle_model.predict(vect.transform(features_test))

roc_auc_score(label_test , pred)


