#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:40:19 2021

@author: Shavilya Rajput
"""


import numpy as np 
import matplotlib.pyplot as plt
list1 = [1,2,3,4,5,6,7,8,9]
x = np.array(list1)


print(x)

x.reshape(3,3)



print(x)


y = np.arange(5)

x = [1,2,3,4,5]

y = [1,8,27,67,125]


plt.scatter(x,y,color = 'g',alpha = 0.8)

plt.plot(x,y,color = 'r')






branches = ['cse','entc','electrical','it','chemical','mechanical']

studentscount = [15,30,25,10,12,12]

plt.pie(studentscount,labels = branches , explode = exp)

exp = (0,0,0,0.2,0,0)