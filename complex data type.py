# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:37:06 2021

@author: Bhagya Lakshmi
"""

print('using string literal')
rules='''rules
     1. here in complex numbers we have to use only j variable
     2. and it should be after imaginary number 
     3. here square of j is -1
     4.by default real and imaginary num of comlex is float 
     5. we can perform any operations on complex numbers 
 except modular division
 
 '''
print(type(rules))
print(rules)
print('complex data type')
a=19+8j
print(a)
print(a.real)
print(a.imag)
print(type(a))
print(id(a))

b=0+1j
c=4.2+4.5j
d=7.5+5j
print(b+c+d)
print(b+c-d)
print(b*c)
print(c/d)
#print(c%d)




