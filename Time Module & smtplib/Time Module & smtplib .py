#!/usr/bin/env python
# coding: utf-8


import time 
epc=time.time()
print(epc)
localtime= time.localtime(epc)
print(localtime)




print(localtime.tm_year)




print(time.ctime(epc))

#------------------------------------------
#   import smtplib
# 
# myemail = "myemail@gmail.com"
# 
# mypassword = "mypassword"
# 
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# 
# connection.starttls()
# 
# connection.login(user= myemail, password= mypassword)
# 
# 
# connection.sendmail(from_addr= myemail,
#                     to_addrs= "reciver@gmail.com",
#                     msg = "Subscribe")
# connection.close()
# 
#               /\                  
# -------------/  \-------------------------------------------------
#               ||
#               ||
# but that code || nolonger support gmail & yahoo 
# -------------------------------------------------------------------

# # created by
# Abdulrahman Mohammed
