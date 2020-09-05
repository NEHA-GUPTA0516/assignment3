#!/usr/bin/env python
# coding: utf-8

# # ARMSTRONG NUMBER IN RANGE OF 1042000 TO 702648265 AND EXIT THE LOOP AFTER ENCOUNTERING THE FIRST ARMSTRONG NUMBER

# In[10]:


lower = 1042000
upper = 702648265

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   num=153000
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
   break
    


# In[11]:


print(num)

