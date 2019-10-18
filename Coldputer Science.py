#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())
x = list(map(int,input().split()))
b = 0
for i in x:
    if i < 0:
        b+=1
print(b)
    
    

