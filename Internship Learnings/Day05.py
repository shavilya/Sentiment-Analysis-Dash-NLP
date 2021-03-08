import re

s = "aaa@xxx.com bbb@yyy.com ccc@zzz.com"

print (re.sub('[a-z]*@', 'ABC@', s))


str1 = 'hello123abc123xyz456_0'

re.findall('\d$', str1)


str1 = 'foobar456'

result = re.search('\d\d\d', str1)

result.start()
result.end()

if re.search('^\d\d\d', str1):
    print("found a match")
else:
    print ("no match")
    

str2 = "Forsk forsk coding school"

re.search('forsk', str2)
re.match('forsk', str2)

re.search('Forsk', str2)
re.match('Forsk', str2)  #^
"""
match       gives index if its in the beginining 

search      gives index if for first occurence anywhere in the string


"""

str1 = "yogendrasingh@zdrv.com 123 yogendra@mango.com Jaipur  ysingh@qualcomm.com yogendra@forsk.in covid19"

re.findall('\w+@\w+\.\w+', str1)



str1 = "yogendrasingh@zdrv.com 123 yogendra@mango.com Jaipur  ysingh@qualcomm.com yogendra@forsk.in covid19"

pattern = re.compile(r'\w+@\w+\.\w+')

pattern.findall(str1)











