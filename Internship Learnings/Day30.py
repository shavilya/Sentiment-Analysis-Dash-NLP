#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:28:10 2021
@author: Shavilya Rajput
"""
# IMPORTING LIBRARIES 

import pandas as pd 
import dash 
import dash_html_components as html 
import webbrowser 
from dash.dependencies import Input,Output

# DECLARING GLOBAL VARIABLES

project_name = "Sentiment Analysis with Insight"
app = dash.Dash()

# DEFINING MY FUNCTIONS

def load_model():
    global df
    df = pd.read_csv("balanced_review.csv")

def create_app_ui():
    main_layout = html.Div(
    [
    html.H1( id = "MainHeading" , children = "Sentiment Analysis with Insights"),
    html.Button(id = "ReviewButton" , children = "Find Review" , n_clicks = 0)
    ]
    )
    return main_layout
    
@app.callback(
    Output("ReviewButton" , "children"),
    [
    Input("ReviewButton" , 'n_clicks' )
    ]
    )
def update_app_ui(n_clicks):
    print("Value passed == " , str(n_clicks))
    if (n_clicks > 0):
        return "Clicks = ",str(n_clicks)
    else:
        return "Find Review"
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
