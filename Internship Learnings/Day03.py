name = "Forsk"
len(name)

dir(str)
help(str.upper)

name_upper = name.upper()

#indexing
name[0] = 'f'
#strings are read only
#immutable

name[0:3]

name[1:4]

name[-1]


#25 -> 5
#include <math.h>

import math
dir(math)
help(math.sqrt)

#scanf

datastore = []

while (True):
    data = input("Enter the number: ")
    
    if not data:
        print ("Invalid input....leaving app..")
        break
    
    if (data.isdigit()):
        
        data = int(data)
        
        datastore.append(math.sqrt(data))
    else:
        datastore.append(len(data))
        


#input, result/ key value pair
        

datadict = {}

while (True):
    data = input("Enter the number: ")
    
    if not data:
        print ("Invalid input....leaving app..")
        break
    
    if (data.isdigit()):
        
        data = int(data)
        
        datadict[data] = math.sqrt(data)
        
    else:
        datadict[data] = (len(data))



#########################

list1 = [2,3,2,4,2,5,4,2]

#version 01
list2 = []


for x in list1:
    list2.append (x*x)
    
#version02
[x*x for x in list1] #list comprehension


{x:x*x for x in list1} #dict comprehension




list1 = [2,3,4,5,3,6,7,2,2,6,3,2]
#remove all the 2s from the list

list1.count(2)

list1.remove(2)
list1.remove(2)
list1.remove(2)
list1.remove(2)


list1 = [2,3,4,5,3,6,7,2,2,6,3,2]

while ( 2 in list1):
    list1.remove(2)

list1 = [2,3,4,5,3,6,7,2,2,6,3,2]

set1 = set(list1)

set1.remove(2)

list1 = list(set1)




