#!/usr/bin/env python
# coding: utf-8



from os import path
def createfile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write("welcome i am abdo")
dest="a:\\ABDO\\FILE.TXT"  #THAT PATH
createfile(dest)




print("file created")


# # created by
# Abdulrahman Mohammed
