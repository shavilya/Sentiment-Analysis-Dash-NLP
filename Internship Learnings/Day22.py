#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:59:22 2021

@author: linux
"""
import pandas as pd 

df = pd.read_csv('balanced_review.csv')

df.dropna(inplace = True)

df = df[df['overall'] !=3]

df['overall'].value_counts()

import numpy as np 

df['positivity'] = np.where( df['overall'] > 3 , 1,0)

# NLTK ( Natural langugage tool kit)

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
import re 

df['reviewText'][0] 
df.iloc[0,1]

for i in range(0,527347):
    corpus = []
    review = re.sub('[^a-zA-z]' , ' ' , df.iloc[i,1])

    review = review.lower()

    review = review.split()

    review = [word for word in review if not word in stopwords.words('english')]

    ps = PorterStemmer()

    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]

    review = " ".join(review)

    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit_transform(corpus)
features_corpus_vectorized = vect.transform(corpus)

labels = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
features_train , features_test , label_train , label_test = train_test_split(df['reviewText'] , df['positivity'] ,test_size = 0.2 , random_state = 31) 

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(features_corpus_vectorized , label_train )
predictions = model.predict(vect.transform(features_test))


#vader
#textblob