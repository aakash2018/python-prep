# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 12:33:25 2025

@author: Aakash
"""
import math

n1 = float(input("Enter the value of num1"))
n2 = float(input("Enter the value of num2"))
n3 = float(input("Enter the value of num3"))

class geometricMean:
    def __init__(self,n1,n2,n3):
        self.num1 = n1
        self.num2 = n2
        self.num3 = n3
        
    def mean(self):
        product = self.num1 * self.num2 * self.num3
        
        return math.pow(product,1/3)
       
    def compute(self):
        return self.mean()
        
        
result = geometricMean(n1, n2, n3)
print(f"The sum is: {result.compute():.2f}");
print("The sum is", "{:.2f}".format(result.compute()))