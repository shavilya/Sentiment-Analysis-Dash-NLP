
print ("Hello Guys...welcome to Forsk")

print (2+3) #F9, Shift+Enter

a  = 10

b = 2.3

c = "Forsk"

d = 'Forsk'

e = "F"

f = 'f'

g = False

h = None

#this is single line comment

"""
data types in Python
int
float
str
bool
NoneType


"""






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

while (True):
    data = input("Enter the number: ")
    
    if not data:
        print ("Invalid input....leaving app..")
        break
    
    data = int(data)
    
    print (math.sqrt(data))













