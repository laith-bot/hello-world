#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Nmaxelements(list1, N): 
    final_list = [] 
    for i in range(0, N):  
        max1 = 0  
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j];    
        list1.remove(max1); 
        final_list.append(max1) 
    listFinal = sum(final_list)
    return listFinal

n = int(input())

x = 0

l = []

case = 1
while x < n:
    redList = []
    blueList = []
    y = int(input())
    st = list(input().split())
    for k in st:
        i = k[len(k)-1]
        u = k[:len(k)-1]
        u = int(u)
        if i == 'B':
            blueList.append(u)
        else:
            redList.append(u)
    if blueList == [] or redList == []:
        l.append('Case #'+str(case)+': '+str(0))
    elif len(blueList) == len(redList):
        sumBlue = sum(blueList)
        sumRed = sum(redList)
        sumBoth = sumBlue + sumRed
        sumBoth = sumBoth - y
        l.append('Case #'+str(case)+': '+str(sumBoth))
    elif len(blueList) > len(redList):
        sumRed = sum(redList)
        modifiedBlueList = Nmaxelements(blueList, len(redList)) 
        sumBoth = sumRed + modifiedBlueList -(len(redList)*2)
        l.append('Case #'+str(case)+': '+str(sumBoth))
    elif len(blueList) < len(redList):
        sumBlue = sum(blueList)
        modifiedRedList = Nmaxelements(redList, len(blueList)) 
        sumBoth = sumBlue + modifiedRedList -(len(blueList)*2)
        l.append('Case #'+str(case)+': '+str(sumBoth))
    x+=1
    case+=1
    
for i in l:
    print(i)


# In[ ]:




