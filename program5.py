# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 13:12:49 2025

@author: Aakash
"""
weight = float(input("Enter weight"))
height = float(input("Enter height"))

class BMICalculator:
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
        
    def calculate(self):
        return weight / (height**2)
    
    
result = BMICalculator(weight, height)
print(f"the result of bmi calculator: {result.calculate():.2f}")