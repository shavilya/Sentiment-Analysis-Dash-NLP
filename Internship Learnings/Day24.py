#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:58:11 2021

@author: Shavilya Rajput
"""

# Requesting user to enter the city name
city = input("Enter the city name: ") 

#Setting api address 
api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=e6023907a536c28d558f876c23778630"

#importing required modules
import requests

# Using get method for receiving response 
response = requests.get(api)

# Saving the json data in jsondata
jsondata = response.json()

# Accessing only main json data from complete json object 
jsondata['main'] 