#!/usr/bin/env python
# coding: utf-8

# In[13]:


email = input("Enter your e-mail: ")
list1 = list(email)
a = 0
b = 0
for i in list1:
    if i == '.':
        a = 1
for i in list1:
    if i == '@':
        b = 1
if a == 1 and b == 1:
    print("Your e-mail is valid.")
else:
    print("Your e-mail is invalid.")
    


# In[ ]:





# In[ ]:




