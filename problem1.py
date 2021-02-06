#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math
y= str(input("Hi, What is your name:-"))
    
low = int(input("low limit:- ")) 
 
high = int(input("high limit:- "))  
 

x = random.randint(low, high)
print("\n\t ", round(math.log(high - low + 1, 2))," guess\n")

count = 0
 

while count < math.log(high - low + 1, 2):
    count += 1
     
 
    anynumber = int(input("guess:- ")) 
    
    if x == anynumber:  
       print(" Yeey! I got it in ", count, " tries!")
       print("do u wan to play it again")
    

       break
    elif x > anynumber:
       print("NO!")
    
    
    elif x < anynumber:
       print("no!")

if count >= math.log(high - low + 1, 2):

   print("\nThe number is %d"%x)
   print("\tBetter Luck Next time", y,"!")
    

