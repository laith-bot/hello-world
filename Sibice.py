#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def pyTheorem(b,l):
    x = math.sqrt((b**2) + (l**2))
    return x



n,w,h = [int(i) for i in input().split()]

x = 0

A = []

while x < n:
    p = pyTheorem (w,h) 
    q = int(input())
    if q <= p:
        A.append('DA')
        
    else:
        A.append('NE')
        
    x+=1

for i in A:
    print(i)
