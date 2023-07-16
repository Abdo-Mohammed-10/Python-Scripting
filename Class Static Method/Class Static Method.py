#!/usr/bin/env python
# coding: utf-8

# In[43]:


class demo():
    #class method
    def addone(self,x):
        return x+1
    
    #static method
    def addtwo(y):
        return y+2


# In[44]:


obj=demo()


# In[49]:


obj=(demo.addone("self",20))


# In[50]:


obj1=(demo.addtwo(10))


# In[51]:


print(obj)
print(obj1)


# # Created by
# Abdulrahman Mohammed
