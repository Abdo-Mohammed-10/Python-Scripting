#!/usr/bin/env python
# coding: utf-8

# # Function



def funcl(*arg,**kwarg):
    
     for i in kwarg.items():
    
            print(i)
        
        
funcl(a=10,x=20,c=30,d=40,n="abdo")


# # Nested Fun



def fun1():
    x=10
    def fun2(x):
        return x+1
    return fun2(x)
result=fun1()
print (result)




def fun1(calledfun):
    print ("first fun")
    def nest_fun(calledfun):
        print("nested fun")
        calledfun
    return nest_fun(calledfun)
def outer_fun():
    print("outer fun")

    
obj=fun1("example")


# # Factory



B=type("bass",(object,),{})
c1=type("c1",(B,),{"VAL":10})
c2=type("c2",(B,),{"VAL":5})
def classcreator(bool):
    if bool:
        return c1()
    else:
        return c2()
print( classcreator(True).VAL)
print( classcreator(False).VAL)


# # Created by
# Abdulrahman Mohammmed
