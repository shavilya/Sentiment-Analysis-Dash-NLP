#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:45:33 2021

@author: Shavilya Rajput
"""

#Importing Libraries 
import pandas as pd 
import dash 
import dash_html_components as html 
import webbrowser 

#Declaring Global Variables
project_name = "Sentiment Analysis with Insight"
app = dash.Dash()

#Defining My Own Function
def load_model():
    global df
    df = pd.read_csv("balanced_review.csv")

def create_app_ui():
    main_layout = html.Div()
    return main_layout

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")
    
#Main Function for controlling flow of project work
def main():
    
    global project_name 
    global df 
    global app 
    
    print("Start of my project")   
    
    open_browser()
    load_model()
    
    print(project_name)
    
    app.title = project_name
    app.layout = create_app_ui()
    
    print("End of my project")
    
    project_name = None
    df = None 
    app = None 

#Calling the Main Function
if __name__ == '__main__':
    main()
     