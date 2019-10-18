#!/usr/bin/env python
# coding: utf-8

# In[7]:


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


# In[ ]:


x = list(map(int,input().split()))
b = 0
for i in x:
    if i < 0:
        b+=1
print(b)
    


# In[ ]:


def multiplyElements(argument):
    x = 1
    for i in argument:
        x*=i
    return x


n = int(input())

q = []

for i in range(n):
    i = []
    i = input().split()
    i = [float(x) for x in i]
    i = multiplyElements(i)
    q.append(i)


q = round(sum(q),3)

