#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:04:59 2021

@author: linux
"""

# IMPORTING LIBRARIES 

import pandas as pd 
 
import webbrowser 
import pickle

import dash 
import dash_html_components as html 
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input,Output,State
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer

# DECLARING GLOBAL VARIABLES

project_name = "Sentiment Analysis with Insight"
app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

# DEFINING MY FUNCTIONS

def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv("scrappedReviews.csv")
    
    global pickle_model 
    file = open('pickle_model.pkl' , 'rb')
    pickle_model = pickle.load(file)
    
    global vocab 
    file = open("feature.pkl" , 'rb')
    vocab = pickle.load(file)
    
    
def check_review(reviewText):
     
    transformer = TfidfTransformer()
    loaded_vect = CountVectorizer(decode_error = "replace" , vocabulary = vocab)
    vectorized_review = transformer.fit_transform(loaded_vect.fit_transform([reviewText]))
    
    return pickle_model.predict(vectorized_review)
     
def create_app_ui():
    main_layout = html.Div(
    [
    html.H1( id = "Main_Title" , children = "Sentiment Analysis with Insights"),
    dcc.Textarea(
       id = "textarea_review",
       placeholder = "Enter the review text here",
       style = {'width':'100%' , 'height':100}
    ),
    dbc.Button( id = "button_review" , 
                children = "Check Review",
                color = 'dark',
                style = {'width':'100%'},
                n_clicks = 0
    ),
    html.H1(id = "result" , children = None )
    ]
    )
    return main_layout

@app.callback(
    Output("result" , "children" ),
    [
    Input("button_review"  , "n_clicks")
    ],
    [
    State('textarea_review', 'value')    
    ]    
    )
 
def update_app_ui2(n_clicks , textarea_value):
   print("Data type == " , str(type(n_clicks)))
   print("Value ="  , str(n_clicks))
   
   print("Data type == " , str(type(textarea_value)))
   print("Value ="  , str(textarea_value))
   
   response = check_review(textarea_value)
   
   if(n_clicks > 0):
        if (response[0] == 0):
           result = "Negative"
           
        elif(response[0] == 1):
           result = "Positive"
   
        else:
           result = "Unknown"
        return result

   else:
       result = "Unknown"
    
"""
@app.callback(
    Output("result" , "children" ),
    [
    Input("textarea_review", "value")
    ]
    )

def update_app_ui(textarea_value):
   print("Data type == " , str(type(textarea_value)))
   print("Value ="  , str(textarea_value))
   
   
   response = check_review(textarea_value)
   
   if (response[0] == 0):
       result = "Negative"
      
   
   elif(response[0] == 1):
        result = "Positive"
   
   else:
        result = "Unknown"
   return result
 """       
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")
    
# MAIN FUNCTION FOR CONTROLLING FLOW OF WORK
    
def main():
    
    global project_name 
    global df 
    global app 
    
    print("Start of my project")   
    
    load_model()
    open_browser()
    
    print(project_name)
    
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server()
    
    print("End of my project")
    
    project_name = None
    df = None 
    app = None 

# CALLING MAIN FUNCTION
    
if __name__ == '__main__':
     main()


        
    