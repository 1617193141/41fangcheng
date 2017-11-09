Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = 'localpth C:\code\cnkiCrawl'
>>> re.findall('[a-zA-z]:\\\\\w+\\\\\+w',y)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    re.findall('[a-zA-z]:\\\\\w+\\\\\+w',y)
NameError: name 're' is not defined
>>> re.findall('[a-zA-Z]:\\\\\w+\\\\\w+', y)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    re.findall('[a-zA-Z]:\\\\\w+\\\\\w+', y)
NameError: name 're' is not defined
>>> import re
>>> re.findall('[a-zA-Z]:\\\\\w+\\\\\w+', y)
['C:\\code\\cnkiCrawl']
>>> 
