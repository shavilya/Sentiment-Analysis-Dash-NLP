#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:34:30 2021

@author: Shavilya Rajput
"""
""" Currency Converter Rest API"""
# Getting currencies for conversion 
From = input("Enter from currency abbrev: ")
To = input("Enter to currency abbrev: ")

# Creating api using url 
currencyapi = "https://free.currencyconverterapi.com/api/v6/convert?q="+From.upper()+"_"+To.upper()+"&compact=ultra&apiKey=7a276e3336d5cd40d295"

# Importing required modules
import requests

response = requests.get(currencyapi)

jsondata = response.json()

""" HTTP BINS REST API """

api = "https://httpbin.org/post"

import requests 
import json 

data = {
          'firstname':'john',
          'skills':'python'
       }

headers = {
            "Content-Type":"application/json",
            "Content-Length":len(data),
            "data": json.dumps(data)
          }
response = requests.post(api,data,headers)

jsondata = response.json()
print(jsondata)