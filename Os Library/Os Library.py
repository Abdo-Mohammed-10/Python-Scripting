#!/usr/bin/env python
# coding: utf-8

# # Os Library

# In[10]:


import os
def current_dir():
    cwd=os.getcwd()
    print(cwd)
def file_path(filename):
    path=os.path.abspath((filename)) 
    print(path)
current_dir()
filename="simple.txt"
file_path(filename)


# # Created by 
# Abdulrahman Mohammed
