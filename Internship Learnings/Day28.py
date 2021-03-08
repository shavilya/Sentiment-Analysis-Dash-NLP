#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:18:01 2021

@author: Shavilya Rajput
"""

from selenium import webdriver

from time import sleep

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"

browser = webdriver.Firefox(executable_path ="geckodriver")
browser.get(url)

sleep(2)

school_code = browser.find_element_by_name("treg") 

school_code.send_keys('2000')

sleep(2)

get_school_result = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')

get_school_result.click()

html_page = browser.page_source

from bs4 import BeautifulSoup as BS

soup = BS(html_page)

import sys
print(sys.path)





