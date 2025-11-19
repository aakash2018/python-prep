# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 13:14:57 2025

@author: Aakash
"""
a=float(input("enter value of a"))
b=float(input("enter value of b"))
c=float(input("enter value of c"))

class arithmeticMeanThreeNumber:
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b 
        self.c=c
        
    def add(self):
        return round(self.a+self.b+self.c /3,2)
    
    def compute(self):
        return {
            "arithmeticThree":self.add()
            }
    

result = arithmeticMeanThreeNumber(a,b,c)
print("result is:",result.compute())

    
        