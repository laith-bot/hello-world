#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = [int(x) for x in input().split()]

x.sort()

string = input()

if string == 'ABC':
    print(x[0], x[1], x[2])
elif string == 'ACB':
    print(x[0], x[2], x[1])
elif string == 'BAC':
    print(x[1], x[0], x[2])
elif string == 'BCA':
    print(x[1], x[2], x[0])
elif string == 'CAB':
    print(x[2], x[0], x[1])
elif string == 'CBA':
    print(x[2], x[1], x[0])


# In[ ]:




