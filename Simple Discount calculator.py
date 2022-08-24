# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:27:11 2022

@author: ghosh
"""


print("Hello there! Let's calculate your discount value shall we?")
c=input("Enter the cost: ")
d=int(c)
e=input("Enter your discount value % : ")
f=int(e)*0.01
discount= f*d
answer= d-discount
print("Your discounted value is : ", discount)
print("The cost after discount is : ", answer)